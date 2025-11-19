// Live digital clock - Format: HH:MM:SS AM/PM
(function () {
  function pad(n) { return String(n).padStart(2, '0'); }

  function getFormattedTime(date) {
    let hours = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();
    const ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // convert 0 -> 12
    return `${pad(hours)}:${pad(minutes)}:${pad(seconds)} ${ampm}`;
  }

  function updateClock() {
    const now = new Date();
    const clockEl = document.getElementById('clock');
    if (!clockEl) return;
    clockEl.textContent = getFormattedTime(now);
  }

  // Align updates to the start of each second to avoid drift
  function tick() {
    updateClock();
    const now = new Date();
    const delay = 1000 - now.getMilliseconds();
    setTimeout(tick, delay);
  }

  // Start the ticking loop
  tick();
})();
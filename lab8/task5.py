def convert_date_format(date_str):
    # Must be a string
    if not isinstance(date_str, str):
        return "Invalid format"

    parts = date_str.split('-')
    if len(parts) != 3:
        return "Invalid format"
    year, month, day = parts

    # All parts must be non-empty and numeric
    if not year or not month or not day:
        return "Invalid format"
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return "Invalid format"

    # Preserve leading zeros if they are present in input (length 2),
    # otherwise output single-digit values without padding
    day_out = day if len(day) == 2 else str(int(day))
    month_out = month if len(month) == 2 else str(int(month))

    return f"{day_out}-{month_out}-{year}"
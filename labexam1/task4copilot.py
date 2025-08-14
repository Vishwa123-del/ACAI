def generate_emails(names):
    emails = []
    for name in names:
        parts = name.strip().split()
        if len(parts) < 2:
            continue  # Skip if not enough parts
        first_letter = parts[0][0].lower()
        last_name = parts[-1].lower()
        email = f"{first_letter}{last_name}@sru.edu.in"
        emails.append(email)
    return emails

# Example usage:
students = ["Anita Sharma", "Rahul Verma", "Priya Singh"]
emails = generate_emails(students)
for email in emails:
    print(email)
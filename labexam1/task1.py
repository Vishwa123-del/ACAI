import re

# Take input from user
text = input("Enter the text: ")

# Regular expression pattern for URLs
url_pattern = r'(https?://[^\s]+)'

# Find all URLs in the text
urls = re.findall(url_pattern, text)

# Print the extracted URLs
print("Extracted URLs:")
for url in urls:
    print(url)

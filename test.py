import re
import csv

# Define a regular expression pattern to match names and emails
pattern = r'(.*?)<(.*?)>;'

# Initialize a list to store the extracted data
data = []

# Read the text file with UTF-8 encoding
with open('emails.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(text)

# Use the regular expression pattern to find matches in the text
matches = re.findall(pattern, text, re.MULTILINE | re.UNICODE)

# Extracted data will be a list of tuples with (name, email)
for match in matches:
    name = match[0].strip()
    email = match[1].strip()
    print(name)
    data.append((name, email))

# Write the extracted data to a CSV file
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Name', 'Email'])  # Write header row
    csv_writer.writerows(data)
    print(data)

print('Data extracted and written to output.csv')

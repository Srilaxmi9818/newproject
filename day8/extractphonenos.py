import re

def extract_phone_numbers(text):
    pattern = r'\(\d{3}\) \d{3}-\d{4}'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers

# Example usage
text = "Contact us at (123) 456-7890 or (456) 789-0123 for assistance."
phone_numbers = extract_phone_numbers(text)
print("Phone numbers found:", phone_numbers)

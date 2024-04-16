import re

def validate_email(email):
    pattern = r'^\w+@\w+\.\w+$'
    if re.match(pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

# Example usage
validate_email("example@email.com")
validate_email("invalid.email@domain.")

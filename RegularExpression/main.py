import re

#Validation without Regular Expressions

email = input("What`s your email? ").strip()
username, domain = email.split("@")

print(domain)
print(username)


if username and "." in domain:
    print("Valid")
else:
    print("Invalid")

#Validation with RE library

if re.search("^\w+@(\w\.)?\w+\.edu$", email): # <- this is not full pattern to cover all cases
    print("Valid")
else:
    print("Invalid")

#Format
name = input("What is your name? ").strip()


if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")

#Extracting from string

url = input("URL: ").strip()

if matches := re.search(r"https?://(?:www\.)?twitter\.com/([a-z0-9_])$", url, re.IGNORECASE):
    print(f"Username", matches.group(1))
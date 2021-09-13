print("Email Validator")
email = input("Enter Your Email: ")
valid_email_domains = ["gmail.com", "hotmail.com", "aol.com", "ymail.com"]
name, domain = email.split("@")
if domain in valid_email_domains:
    print(f"Hello {name} you have a valid domain name of {domain}")
else:
    print(f"Hello {name} you have a less known domain name of {domain}")

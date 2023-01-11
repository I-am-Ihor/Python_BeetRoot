import re


class Validate:
    def __init__(self, email) -> None:
        self.email = email
        self.validate_email(email)

    def validate_email(self, email):
        pattern = r"[\w]+[\w\.-]+@[\w\.\-]+\.[\w\.]+"
        if re.match(pattern, email):
            print("Email validated")
        else:
            print("Email not validated")


my_email = Validate("1234567----@gmail.com")

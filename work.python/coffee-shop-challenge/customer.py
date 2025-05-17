class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_email(self, new_email):
        self.email = new_email

    def get_info(self):
        return {
            "name": self.name,
            "email": self.email
        }
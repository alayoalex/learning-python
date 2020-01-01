class Contact:
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone = phone
        self.address = address
        self.email = email

    def __str__(self):
        return ("Name: " + self.name + "\nAddress: " + self.address + "\nPhone: " + str(self.phone) + 
            "\nE-mail: " + self.email)

    @property
    def get_name(self):
        return self.name

    @property
    def get_phone(self):
        return self.phone

    @property
    def get_addres(self):
        return self.address

    @property
    def get_email(self):
        return self.email

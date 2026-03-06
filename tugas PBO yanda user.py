class User:
    def __init__(self,firts_name,last_name,age,phone_number):
        self.firt_name = firts_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
    def describe_user(self):
        print(f"nama lengkap : {self.firt_name} {self.last_name}")
        print(f"umur : {self.age}")
        print(f"nomor handphone : {self.phone_number}")
    def great_user(self):
        print(f"Hallo, {self.firt_name} selamat datang di program ini.")

user1 = User("Zikri", "Fitriyanda", "19", "089786545543")
user1.describe_user()
user1.great_user()
print()


user2 = User("Icah","Tapasyah", "19", "082287652345")
user2.describe_user()
user2.great_user()
print()
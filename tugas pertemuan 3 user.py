class User:
    def __init__(self,firts_name,last_name,age,phone_number):
        self.firt_name = firts_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.login_attempts = 0
    def describe_user(self):
        print(f"nama lengkap : {self.firt_name} {self.last_name}")
        print(f"umur : {self.age}")
        print(f"nomor handphone : {self.phone_number}")
    def great_user(self):
        print(f"Hallo, {self.firt_name} selamat datang di program ini.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Zikri", "Fitriyanda", "19", "089786545543")   
user1.describe_user()
user1.great_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"jumlah percobaan login :" ,user1.login_attempts)

user1.reset_login_attempts()
print(f"jumlah percobaan login setelah reset :" ,user1.login_attempts)
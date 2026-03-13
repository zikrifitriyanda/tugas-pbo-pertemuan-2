class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} adalah restoran yang menyediakan makanan {self.cuisine_type} ")
    def open_restaurant(self):
        print(f"{self.restaurant_name} ini sedang buka")
    def set_number_served(self, jumlah):
        self.number_served = jumlah
    def increment_number_served(self, tambahan):
        self.number_served += tambahan

restoran = Restaurant("yanda resto" , "melayu")

print(f"Nama restoran ini adalah  {restoran.restaurant_name}")
print(f"Jumlah pelanggan yang telah di layani :" ,restoran.number_served)
restoran.number_served = 15
print(f"Jumlah pelanggan setelah di ubah :" ,restoran.number_served)
restoran.set_number_served (25)
print(f"Pelanggan yang di layani :" ,restoran.number_served)
restoran.increment_number_served (10)
print(f"pelanggan yang di layani setelah satu hari :", restoran.number_served)
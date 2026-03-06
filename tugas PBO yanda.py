class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.restaurant_name} adalah restoran yang menyediakan makanan {self.cuisine_type} ")
    def open_restaurant(self):
        print(f"{self.restaurant_name} ini sedang buka")

restoran = Restaurant("yanda resto" , "melayu")

print(f"Nama restoran ini adalah  {restoran.restaurant_name}")
print(f"restoran ini menyediakan makanan {restoran.cuisine_type} ")
restoran.describe_restaurant()
restoran.open_restaurant()
print()

restoran_apis = Restaurant("apis resto" , "padang")

print(f"Nama restoran ini adalah  {restoran_apis.restaurant_name}")
print(f"restoran ini menyediakan makanan {restoran_apis.cuisine_type} ")
restoran_apis.describe_restaurant()
restoran_apis.open_restaurant()
print()

restoran_mila = Restaurant("mila resto" , "hits")

print(f"Nama restoran ini adalah  {restoran_mila.restaurant_name}")
print(f"restoran ini menyediakan makanan {restoran_mila.cuisine_type} ")
restoran_mila.describe_restaurant()
restoran_mila.open_restaurant()
print()

import unittest 

def tambah(a,b):
    return a + b
def kurang(a,b):
    return a - b
def kali(a,b):
    return a * b
def bagi(a,b):
    if b == 0:
        return "tidak bisa di bagi nol"
    return a / b

class TesKalkaltor(unittest.TestCase):

    def test_tambah(self):
        self.assertEqual(tambah (10,5), 15)
    
    def test_kurang(self):
        self.assertEqual(kurang(5,2), 3)
    
    def test_kali(self):
        self.assertEqual(kali(5,5), 25)
    
    def test_bagi(self):
        self.assertEqual(bagi(10,2), 5)

if __name__ == "__main__":
    unittest.main()

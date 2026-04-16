import json
import time



class Dream_Sweet:
    def __init__(self, json_file):
        self.json_file = json_file
        self.total_bill = 0
        self.buyurtma = []
        self.data = {"menu": []}
        self.load_data()
        
        
    def load_data(self):
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            print("Json file topilmadi yoki bosh yengi file ishlatiladi ")
            self.data = {"menu": []}

    def write_new_data(self):
        with open(self.json_file, 'w', encoding= 'utf-8') as f:
            json.dump(self.data, f, indent= 4, ensure_ascii = False)

    def menu(self):
        print("\n" + "-" *40)
        print("       ☕ Dream Sweet Cafe Menu")
        print("-" * 40)

        if not self.data["menu"]:
            print("Menyu Bosh!")
            return
        for i in self.data["menu"]:
            print(f"{i['id']}. {i['nomi']} - {i['narxi']} som")
        print('-'*40)

    def payment_sysytem(self, total):
        print("\n💳 Toloov usulini tanlang")
        payment = int(input("Naqd (1)  Karta va Qr (2): "))
        if payment == 1:
            cash = float(input("Naqd pul: "))
            if cash >= total:
                print(f"Qaytim: {cash - total} som")
                print("Tolov muvaffaqiyatli kafeyimizga keilib turing☺️")
            else:print("PUl yetarli emas!")
        elif payment == 2:
            print("Karta Raqam\n")
            print("💳Humo: 9860 2566 0650 9592\nDaminov M")
            print("💳Visa: 4916 9903 0150 2511\nDaminov M")
            print("QR KOD \n")
            print("""
    █▀▀▀▀▀█ ▄ ▄▄ ▄ █▀▀▀▀▀█
    █ ███ █ ▀█▀▀ ▄ █ ███ █
    █ ▀▀▀ █ ▄▀█▀▄  █ ▀▀▀ █
    ▀▀▀▀▀▀▀ █ ▀ █ ▀▀▀▀▀▀▀
    ▀▀▄▀▄▀▀▀█▀▄▄▀▀▄▀▄▀▀▀█
    █▀▀▀▀▀█ ▀ █▀▄  ▀█▀█▀▀
    █ ███ █ █▀▀▀▄▀ ▀▀▀▀▀█
    █ ▀▀▀ █ ▄ █▀▄ █▀ █ ▀ 
    ▀▀▀▀▀▀▀ ▀▀▀   ▀▀  ▀▀
    """)
            
    def buyurtma_jarayoni(self, product_id, miqdor):
        
        for i in self.data["menu"]:
            stock = i['stok']
            if i["id"] == product_id:
                if i['stok'] == 0 and i['stok'] < miqdor:
                    i['stok'] = stock          
                    return False
                
                i['stok'] -= miqdor
                self.total_bill += i["narxi"]*miqdor
                self.buyurtma.append(f"{i['nomi']} x{miqdor}")
                return True
        
        print("Bunday Id topilmadi!")
        return False
    
    def cooking(self, sec=5):
        print("\n\nTayyorlanmoqda...")
        for i in range(sec, 0, -1):
            print(f"⌛ {i}s", end="\r")
            time.sleep(1)
        print("\n Buyurtma Tayor✅")

    def start_service(self):
        print(" Dream Sweets kafesiga hush kelibsiz!☺️")

        service = int(input("Shu yerda (1) || Olib ketish (2): "))

        while True:
            self.menu()

            try:
                menu_id = int(input("Zakaz qilmoqchi bolgan narsangizni Id raqamini kiriting: "))
                quantity = int(input("Nechta: "))

                if self.buyurtma_jarayoni(menu_id, quantity):
                    print("\nBuyurtma Qoshildi!")
            except ValueError:
                print("Faqat son kiriting!")
                continue

            tanlov = input("Yana buyurtma qilasizmi? (ha/yoq): ").strip().lower()
            if tanlov != "ha":
                break

        print("\n Buyurtma Royhati: ")
        for i in self.buyurtma:
            print("-", i)

        print(f"\n jami: {self.total_bill} som")

        self.payment_sysytem(self.total_bill)

        self.write_new_data()

        self.cooking(5)

        if service == "2":
            print("Buyurtma Tayyor Olib Ketishingiz Mumkin!")

        else: print("🍽️ Yoqimli Ishtaha")



kafe = Dream_Sweet("dream_sweets.json")
kafe.start_service()

                
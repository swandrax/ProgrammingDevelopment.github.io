class MerchandiseItem:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

class MerchandiseMarket:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item.nama} added to the merchandise market.")

    def update_item(self, kode, new_nama, new_harga):
        for item in self.items:
            if item.kode == kode:
                item.nama = new_nama
                item.harga = new_harga
                print(f"{item.nama} updated successfully.")
                return
        print("Item not found.")

    def delete_item(self, kode):
        for item in self.items:
            if item.kode == kode:
                self.items.remove(item)
                print(f"{item.nama} deleted successfully.")
                return
        print("Item not found.")

    def display_items(self):
        print("|==================================================|")
        print("|                MERCHANDISE MARKET                |")
        print("|==================================================|")
        print("|  Kode  |           Nama           |    Harga    |")
        print("|==================================================|")
        for item in self.items:
            print(f"|   {item.kode}   |  {item.nama.ljust(23)} | Rp. {item.harga}  |")
        print("|==================================================|")

def clear_screen():
    # Function to clear the console screen
    pass

def process_buy_football_jersey(merchandise_market):
    print("|==================================================|")
    print("|============== BELI KAOS BOLA ===================|")
    print("|==================================================|")
    print("|  Kode  |         Tim          |    Harga        |")
    print("|==================================================|")
    print("|   1.   |  Liverpool           | Rp. 150000       |")
    print("|   2.   |  Manchester United   | Rp. 120000       |")
    print("|   3.   |  Barcelona           | Rp. 130000       |")
    print("|   4.   |  Real Madrid          | Rp. 140000       |")
    print("|==================================================|")

    pilih_jersey = int(input("\nPilih kode tim: "))
    jml_jersey = int(input("Masukkan jumlah jersey yang ingin dibeli: "))

    harga_jersey = 0
    if pilih_jersey == 1:
        harga_jersey = 150000
    elif pilih_jersey == 2:
        harga_jersey = 120000
    elif pilih_jersey == 3:
        harga_jersey = 130000
    elif pilih_jersey == 4:
        harga_jersey = 140000
    else:
        print("Pilihan tidak valid")

    subtotal = jml_jersey * harga_jersey
    tax = subtotal * 0.1  # 10% tax
    total = subtotal + tax
    return subtotal, total

def process_buy_football_ball(merchandise_market):
    print("|==================================================|")
    print("|============== BELI BOLA BOLA ===================|")
    print("|==================================================|")
    print("|  Kode  |       Jenis Bola      |    Harga       |")
    print("|==================================================|")
    print("|   1.   |  Bola Sepak           | Rp. 50000       |")
    print("|   2.   |  Bola Futsal          | Rp. 60000       |")
    print("|   3.   |  Bola Basket          | Rp. 70000       |")
    print("|==================================================|")

    pilih_bola = int(input("\nPilih jenis bola: "))
    jml_bola = int(input("Masukkan jumlah bola yang ingin dibeli: "))

    harga_bola = 0
    if pilih_bola == 1:
        harga_bola = 50000
    elif pilih_bola == 2:
        harga_bola = 60000
    elif pilih_bola == 3:
        harga_bola = 70000
    else:
        print("Pilihan tidak valid")

    subtotal = jml_bola * harga_bola
    tax = subtotal * 0.1  # 10% tax
    total = subtotal + tax
    return subtotal, total

def process_buy_football_accessory(merchandise_market):
    print("|==================================================|")
    print("|=========== BELI AKSESORIS SEPAKBOLA =============|")
    print("|==================================================|")
    print("|  Kode  |        Jenis Aksesoris         |  Harga |")
    print("|==================================================|")
    print("|   1.   |  Sarung Tangan               | Rp. 25000|")
    print("|   2.   |  Kaus Kaki                   | Rp. 20000|")
    print("|   3.   |  Pelindung Mata              | Rp. 30000|")
    print("|   4.   |  Pelindung Gigi              | Rp. 35000|")
    print("|==================================================|")

    pilih_aksesoris = int(input("\nPilih jenis aksesoris: "))
    jml_aksesoris = int(input("Masukkan jumlah aksesoris yang ingin dibeli: "))

    harga_aksesoris = 0
    if pilih_aksesoris == 1:
        harga_aksesoris = 25000
    elif pilih_aksesoris == 2:
        harga_aksesoris = 20000
    elif pilih_aksesoris == 3:
        harga_aksesoris = 30000
    elif pilih_aksesoris == 4:
        harga_aksesoris = 35000
    else:
        print("Pilihan tidak valid")

    subtotal = jml_aksesoris * harga_aksesoris
    tax = subtotal * 0.1  # 10% tax
    total = subtotal + tax
    return subtotal, total

def main():
    merchandise_market = MerchandiseMarket()

    while True:
        print(" ")
        print("\t\t\t|============================================|")
        print("\t\t\t\tSELAMAT DATANG DI TOKO SEPATU BOLA      ")
        print("\t\t\t|============================================|")
        print("\t\t\t\t| PRESS ENTER TO CONTINUE |               ")
        input()

        clear_screen()

        print("\t\t\t==============================================")
        print("\t\t\t               PEMBELIAN SEPATU BOLA           ")
        print("\t\t\t==============================================")
        print("\t\t\t                NO. ANTRIAN : ", end="")
        no_antrian = int(input())

        clear_screen()

        while True:
            print(" ")
            print("\t\t\t|==================================================|")
            print("\t\t\t\t    SILAHKAN PILIH MENU BELANJA SEPATU BOLA")
            print("\t\t\t|==================================================|")
            print("\t\t\t|  1. Beli Jersey Bola           |  2. Beli Bola    |")
            print("\t\t\t|  3. Beli Aksesoris Bola        |  4. Keluar       |")
            print("\t\t\t|==================================================|")
            print()

            pilih_menu = int(input("\t\t\t  Pilih menu yang ingin di pilih : "))

            clear_screen()

            if pilih_menu == 1:
                subtotal, total = process_buy_football_jersey(merchandise_market)
                print(f"\nSubtotal harga: Rp {subtotal}")
                print(f"Total (including 10% tax): Rp {total}")
            elif pilih_menu == 2:
                subtotal, total = process_buy_football_ball(merchandise_market)
                print(f"\nSubtotal harga: Rp {subtotal}")
                print(f"Total (including 10% tax): Rp {total}")
            elif pilih_menu == 3:
                subtotal, total = process_buy_football_accessory(merchandise_market)
                print(f"\nSubtotal harga: Rp {subtotal}")
                print(f"Total (including 10% tax): Rp {total}")
            elif pilih_menu == 4:
                print("semoga senang dengan pesanannya")
                break
            else:
                print("Pilihan tidak valid")

        lagi = input("\nApakah Anda ingin melakukan transaksi lagi? (y/n): ")
        if lagi.lower() != 'y':
            print("Terima kasih, sampai jumpa!")
            break

if __name__ == "__main__":
    main()
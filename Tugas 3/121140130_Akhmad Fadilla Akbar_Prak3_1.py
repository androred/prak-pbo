class AkunBank:
    list_pelanggan = []
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.list_pelanggan.append(self)
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo

    def menu(self):
        print("** Selamat datang di Bank Jago **")
        print("Halo ", self.__nama_pelanggan, " ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")
    
    def tarik_tunai(self):
        saldoMin = False
        while(not saldoMin):
            tarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
            if(self.__jumlah_saldo < tarik):
                print("Nominal saldo yang anda punya tidak cukup!")
            else:
                self.__jumlah_saldo -= tarik
                print("Saldo berhasil ditarik!")
                saldoMin = True
    
    def transfer(self):
        jumlahTransfer = int(input("Masukkan nominal yang ingin ditransfer: "))
        rekTujuan = int(input("Masukkan no rekening tujuan: "))
        status = 0
        for i in self.list_pelanggan:
            if(rekTujuan == self.__no_pelanggan):
                status = 3
            elif(rekTujuan == i.__no_pelanggan):
                if(jumlahTransfer > self.__jumlah_saldo):
                    status = 2
                else:
                    status = 0
                break
                self.__jumlah_saldo -= jumlahTransfer
            elif (rekTujuan != i.__no_pelanggan):
                status = 1

        if(status == 1):
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama ...")
            status = 0
        elif(status == 2):
            print("Nominal saldo yang Anda punya tidak cukup! Kembali ke menu utama ...")
            status = 0
        elif(status == 3):
            print("No rekening tujuan anda masukan adalah no rekening saat ini! Kembali ke menu utama ...")
            status = 0
        else:
            print(f"Transfer Rp {jumlahTransfer} ke {rekTujuan} sukses!")
            status = 0

Akun1 = AkunBank(1234, "Akhmad Fadilla Akbar", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 66666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

Akun1.menu()
berhenti = False

menu = int(input("Pilih menu : "))
print("\n")
while(not berhenti):
    if (menu == 1):
        Akun1.lihat_saldo()
        print("\n")
        Akun1.menu()
        menu = int(input("Pilih menu : "))
        print("\n")
    elif(menu == 2):
        Akun1.tarik_tunai()
        print("\n")
        Akun1.menu()
        menu = int(input("Pilih menu : "))
        print("\n")
    elif(menu == 3):
        Akun1.transfer()
        print("\n")
        Akun1.menu()
        menu = int(input("Pilih menu : "))
        print("\n")
    elif(menu == 4):
        berhenti = True
    else:
        menu = int(input("Pilih menu : "))
        print("\n")
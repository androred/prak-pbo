from abc import ABC, abstractmethod

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo

    def lihat_saldo(self):
        print("Saldo " + self.nama + " : " + "Rp " + str(self.saldo))

    @abstractmethod
    def transfer_saldo(self, jumlah):
        pass

    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def transfer_saldo(self, jumlah):
        self.tahun_daftar = 2023 - self.tahun_daftar
        if self.tahun_daftar < 3 and jumlah > 100000:
            biaya_administrasi = 2000
        else:
            biaya_administrasi = 0
        self.saldo -= jumlah + biaya_administrasi
        print("Transfer saldo berhasil. " + " Biaya administrasi: Rp " + str(biaya_administrasi))

    def lihat_suku_bunga(self):
        self.tahun_daftar = 2023 - self.tahun_daftar
        if self.tahun_daftar >= 3 and self.saldo >= 1000000000:
            bunga = 0.01
        elif self.tahun_daftar < 3 and self.saldo >= 1000000000:
            bunga = 0.02
        else:
            bunga = 0.03
        print("Suku bunga: " + str(bunga * 100) + "% per bulan")

class AkunSilver(AkunBank):
    def transfer_saldo(self, jumlah):
        self.tahun_daftar = 2023 - self.tahun_daftar
        if self.tahun_daftar < 3 and jumlah > 100000:
            biaya_administrasi = 5000
        elif self.tahun_daftar >= 3 and jumlah > 100000:
            biaya_administrasi = 2000
        else:
            biaya_administrasi = 0
        self.saldo -= jumlah + biaya_administrasi
        print("Transfer saldo berhasil. " + " Biaya administrasi: Rp " + str(biaya_administrasi))

    def lihat_suku_bunga(self):
        self.tahun_daftar = 2023 - self.tahun_daftar
        if self.tahun_daftar >= 3 and self.saldo >= 10000000:
            bunga = 0.01
        elif self.tahun_daftar < 3 and self.saldo >= 10000000:
            bunga = 0.02
        else:
            bunga = 0.03
        print("Suku bunga: " + str(bunga * 100) + "% per bulan")

akun1 = AkunGold("Akhmad",2020,10000000)

akun1.lihat_saldo()
akun1.lihat_suku_bunga()
akun1.transfer_saldo(50000)
akun1.lihat_saldo()

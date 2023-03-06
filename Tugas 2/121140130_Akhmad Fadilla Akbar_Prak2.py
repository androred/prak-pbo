class Biodata:
   
    def __init__(self, nama, NIM, Kelas, sks):
       self.nama = nama
       self.NIM = NIM
       self.Kelas = Kelas
       self.sks = sks
       
       
    def Bio (self):
        print("Nama Mahasiswa: ", self.nama)
        print("NIM Mahasiswa: ", self.NIM)
        print("Kelas: ", self.Kelas)
        print("Jumlah Sks: ", self.sks)
        
bio1 = Biodata("Akbar", 121140130, "RB", 20)

bio1.Bio()

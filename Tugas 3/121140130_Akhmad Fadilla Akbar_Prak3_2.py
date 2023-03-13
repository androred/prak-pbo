class Manusia:
    # atribut global
    suku = 'Jawa'
    
    def __init__(self, nama, umur, jurusan):
        # atribut publik
        self.nama = nama
        self.jurusan = jurusan
        # atribut protected
        self._umur = umur
        # atribut private
        self.__alamat = '-'
    
    # fungsi publik
    def get_umur(self):
        return self._umur
    
    # fungsi protected
    def _ubah_umur(self, umur_baru):
        self._umur = umur_baru   
    def _ubah_alamat(self, alamat_baru):   
        # mengubah atribut private (tidak dapat diakses langsung pada main program)
        # misal orang1.__alamat = 'Jakarta'
        # akan menyebabkan AttributeError: 'Manusia' object has no attribute '__alamat'
        self.__alamat = alamat_baru
    
    # fungsi instance private
    # fungsi ini hanya dapat di akses di dalam class tidak dapat di akses di luar class atau di main program
    def __print_alamat(self):
        print(f"Alamat {self.__alamat}")
    
    def info(self):
        print('Nama:', self.nama)
        print('Umur:', self._umur)
        self.__print_alamat()
        print('Suku:', self.suku)
        print("")
        
        
        
# membuat objek dari class 
mhs1 = Manusia('Akbar', 20, "Teknik Informatika")
mhs1.info()

# mengakses atribut kelas
print('Suku:', Manusia.suku)
print("")

# mengakses atribut instance publik
print('Nama:', mhs1.nama)
print("")

# mengubah atribut instance protected
mhs1._ubah_umur(26)
print('Umur:', mhs1.get_umur())
print("")

mhs1._ubah_alamat("Cirebon")
mhs1.info()
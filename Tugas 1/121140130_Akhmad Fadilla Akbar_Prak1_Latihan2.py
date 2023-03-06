username = ("informatika")
password = ("12345678")

i = 1

while(i <= 3):
    user = input("masukkan username : ")
    pw = input("maskukkan password: ")

    if(user == username and pw == password):
        print("Berhasil login!")
        break
    elif(i == 3):
        print("Akun diblokir!!!")
        break
    else:
        print("Username atau password yang anda masukkan salah, coba lagi")
        i += 1
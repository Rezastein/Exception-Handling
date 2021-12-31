while True:
        try:
            nama = input("Masukan NAMA : ")
            if nama == "":
                print("NAMA tidak boleh kosong")
            else:
                break
        except:
            print("Harap Masukan Angka")
        else:
            break
        finally:
            print(nama)
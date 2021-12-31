from datetime import datetime as dtm

tanggal_valid = False
while not tanggal_valid:
  dt_input = input('Masukkan tanggal lahir anda dengan format seperti contoh berikut: 05-03-2001\n:')
  try:
    tanggal_lahir = dtm.strptime(dt_input,'%d-%m-%Y')
    tanggal_valid = True
  except:
    print('Anda memasukkan nilai dengan format yang salah')
print(tanggal_lahir)


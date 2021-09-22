print("\n\n\n\n\tTolong Masukkan Data Diri Anda Dengan Baik Dan Benar\n\n")

nama_lengkap = raw_input("Nama Lengkap : ")
jenis_kelamin = raw_input("Jenis Kelamin : ")
tempat_tanggal_lahir = raw_input("Tempat/tanggal lahir : ")
status = raw_input("Status : ")
alamat = raw_input("Alamat : ")
tlp = raw_input("Telp/Hp : ")
agama = raw_input("agama : ")
pendidikan = raw_input("Pendidikan : ")

#tinggal di tambah sesuai keinginan kalian

teks = "\n----------------- {}\nNama Lengkap : {}\nJenis Kelamin : {}\nTempat/tanggal lahir : {}\nStatus : {}\nAlamat : {}\nTelepon/No Hp : {}\nAgama : {}\nPendidikan : {}\n-----------------".format(nama_lengkap, jenis_kelamin, tempat_tanggal_lahir, status, alamat, tlp, agama, pendidikan)
file_bio = open("membiodata.txt", "a")
file_bio.write(teks)
file_bio.close()

print("\n\t code by @riskiakabr279\n")
print("\n\tNote : Biodata sudah selesai file telah disimpan dengan nama membiodata.txt\n")
print("\n\tTerimakasih")





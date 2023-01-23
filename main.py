print ("Halo Dunia")

#compile python agar lebih cepat prosesnya
#tulis di terminal
#python -m py_compile namafile.py
#maka akan muncul __pycache__, lalu jalankan file didalamnya

#Variabel adalah tempat menyimpan data
#a = variabel
# = == assigment
# 2 = value
a = 2
print("Nilai a = ", a)

#di python tidak ada deklarasi, contoh
#int a

a = 4
#assigment indirect
b = a
print("Nilai b = ", b)

#tipe data: angka satuan (integer)
data_integer = 1
print("data = ", data_integer, ", bertipe = ", type(data_integer))

#tipe data : angka dengan coma / desimal (float)
data_float = 2.5
print("data = ", data_float, ", bertipe = ", type(data_float))

#tipe data : kumpulan karakter (string)
data_string = "putra"
print("data = ", data_string, ", bertipe = ", type(data_string))

#tipe data : biner true/false (boolean)
data_boolean = True
print("data = ", data_boolean, ", bertipe = ", type(data_boolean))

#tipe data khusus = bilangan data kompleks
#real di depan, imaginer di belakang
data_complex = complex(5,6)
print("data = ", data_complex, ", bertipe = ", type(data_complex))

#tipe data khusus = tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data = ", data_c_double, ", bertipe = ", type(data_c_double))

#Belajar casting
#casting adalah merubah dari satu tipe ke tipe lain
#tipe data = int, float, str, bool

data_int = 9;
print("data = ", data_int, ", type =", type(data_int))

data_flt = float(data_int)
print("data = ", data_flt, ", type =", type(data_flt))

data_str = str(data_int)
print("data = ", data_str, ", type =", type(data_str))

data_bool = bool(data_int) #akan bernilai false jika value = 0
print("data = ", data_bool, ", type =", type(data_bool))

data_floats = 9.9;
data_ints = int(data_floats) #akan dibulatkan ke bawah
print("data = ", data_ints, ", type =", type(data_ints))

data_str = "test";
data_bool = bool(data_str) #akan bernilai false jika string bernilai kosong
print("data = ", data_bool, "type = ", type(data_bool))
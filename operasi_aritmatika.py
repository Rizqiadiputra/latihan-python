a = 11
b = 5

#tambah
hasil = a + b
print(a,'+',b,'=',hasil)

#kurang
hasil = a - b
print(a,'-',b,'=',hasil)

#perkalian
hasil = a * b
print(a,'*',b,'=',hasil)

#pembagian
hasil = a / b
print(a,'/',b,'=',hasil)

#eksponen (pangkat)
hasil = a ** b
print(a,'**',b,'=',hasil)

#modulus (sisa pembagian)
hasil = a % b
print(a,'%',b,'=',hasil)

#floor division (kebalikan dari modulus) pembagian dibulatkan kebawah
hasil = a // b
print(a,'//',b,'=',hasil)

#prioritas operasi, operational precedence

'''
1.()
2.exponen **
3.perkalian * / ** %
4.pertambahan dan pengurangan
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'* (',z,'+',x,') /',y,'-',y,'%',z,'//',x,"hasil",hasil)
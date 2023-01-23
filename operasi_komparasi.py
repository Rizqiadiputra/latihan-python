#setiap hasil dari komparasi adalah boolean

# >,<,>=,<=,==,!=, #sintak literal
# a == 4; a (ada nilainya(memakan memory)); 4(literal(tidak ada variabel,langsung nilai))
# is,is not ;#membandingkan memory atau object
#a is b (perbandingan variabel)

a = 4
b = 2

#lebih besari dari >
print('====Lebih besar dari (>)====')
hasil = a > b
print(a,'>',b,'=',hasil)

#kurang dari >
print('====Kurang dari (<)====')
hasil = a < b
print(a,'<',b,'=',hasil)

#lebih besar dari sama dengan >
print('====Lebih besar dari (>=)====')
hasil = a >= b
print(a,'>',b,'=',hasil)

#kurang dari sama dengan >
print('====Kurang dari (<=)====')
hasil = a <= 4
print(a,'<=',4,'=',hasil)

#sama dengan >
print('====Sama dengan dari (==)====')
hasil = a == 4
print(a,'==',4,'=',hasil)

#tidak sama dengan >
print('====Tidak sama dengan dari (!=)====')
hasil = a != 4
print(a,'!=',4,'=',hasil)

#tidak sama dengan >
print('====Tidak sama dengan dari (!=)====')
hasil = a != 4
print(a,'!=',4,'=',hasil)


#'is' sebagai komparasi object identity
x = 5 #ini adalah assigment membuat object
y = 5
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai x =",y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 #ini adalah assigment membuat object
y = 6
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai x =",y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

#'is not' sebagai komparasi object identity
x = 5 #ini adalah assigment membuat object
y = 5
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai x =",y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)

x = 5 #ini adalah assigment membuat object
y = 6
print("nilai x =",x,',id = ',hex(id(x)))
print("nilai x =",y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =',hasil)
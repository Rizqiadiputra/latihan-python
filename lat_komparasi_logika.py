#membuat gabungan area rentang dari angka

#++++3-----10++++
inputUser = float(input('Masukkan nilai \nkurang dari 3 \natau lebih besar dari 10\n : '))

isKurangDari = inputUser < 3
print(inputUser,'kurang dari 3 = ',isKurangDari)

isLebihDari = inputUser > 10
print(inputUser,'lebih dari 10 = ',isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('angka yang anda masukkan',isCorrect)


#----3+++10----
#kasus irisan

inputUser = float(input('Masukkan nilai \nlebih besar dari 3 \ndan kurang dari 10\n : '))

isLebihDari = inputUser > 3
print(inputUser,'lebih dari 3 = ',isLebihDari)

isKurangDari = inputUser < 10
print(inputUser,'kurang dari 10 = ',isKurangDari)


isCorrect = isKurangDari and isLebihDari
print('angka yang anda masukkan',isCorrect)
def deret_aritmatika(a, b, N):
    deret = []
    for i in range(N):
        suku = a + i * b
        deret.append(suku)
    return deret

a = 2  #Suku pertama
b = 3  #Beda deret
N = 4  #Jumlah

hasil = deret_aritmatika(a, b, N)
print("Jadi, deret bilangan aritmatika:", hasil)
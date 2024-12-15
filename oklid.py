def euclideanDistance(x, y):
    oklid = 0
    for k in range(len(x)):
        oklid += (x[k] - y[k]) ** 2  
    oklid = oklid ** (1 / 2) 
    return oklid  
matris_str = input("giriniz")
matris1_str = input("2 giriniz")

matris = [int(x) for x in matris_str.split(",")]
matris1 = [int(x) for x in matris1_str.split(",")]

sonuc = euclideanDistance(matris, matris1)
print("sonuç:", sonuc)

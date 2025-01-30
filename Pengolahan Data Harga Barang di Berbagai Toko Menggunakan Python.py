#fungsi untuk membaca file 
file = open("DictOsaTubes.txt","r")
lines = file.readlines()

harga =[]
sementara ={}
for data in lines:
    split = data.split()
    sementara = {
        split[0]:[split[1],split[2],split[3],split[4],split[5],split[6]]
        }
    harga.append(sementara)
    
#fungsi untuk mencari dictionary
def dictionary(toko):
    for data in toko:
        for k,v in data.items():
            print(k,v)

#fungsi untuk mencari harga termurah
def termurah(toko):
    for data in toko:
        for k,v in data.items():
            print(k,min(v))

#fungsi untuk mereport harga
def report(toko):
    for data in toko:
        for k,v in data.items():
            for idx,ele in enumerate(v):
                v[idx] = int(float(ele.replace(".","")))
            jumlah = (sum(v))/(float(len(v)))
            print(k,jumlah)

#Membuat main program
print("Barang : Toko 1 | Toko 2 | Toko 3 | Toko 4 | Toko 5 | Toko 6 |")
print("=============================================================")
def main():
    dictionary(harga)
    print()
    print("Harga Termurah")
    print("===============")
    termurah(harga)
    print()
    print("Report Rata-rata semua barang")
    print("===============================")
    report(harga)
#menampilkan semua fungsi yang telah dibuat
main()


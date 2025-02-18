# Latihan 1
print("Latihan 1")
NPM = [2420506031, 2420506032, 2420506033, 2420506034, 2420506035]
print("Array NPM: ", NPM)

# Latihan 2
print("\nLatihan 2")
NPM = [2420506031]
angka = [89, 21, 34, 56, 78]
print("\nNPM: ", NPM)
print("Array angka: ", angka)
angka.append(31)
print("Array angka setelah ditambah 2 digit terakhir: ", angka)
angka.pop(0)
print("Array angka setelah dihapus elemen pertama: ", angka)

# Latihan 3
print("\nLatihan 3")
fakultas= ["EKONOMI", "ILMU SOSIAL DAN ILMU POLITIK", "KEGURUAN DAN ILMU PENDIDIKAN", "PERTANIAN, TEKNIK"]
print("\nFakultas di Universitas Tidar: ", fakultas)
for f in fakultas:
    print("Fakultas: ", f)

# Latihan 4 
print("\nLatihan 4")
harga= [1500, 250, 7000, 43000, 115000]
print("\nArray harga(RP): ", harga)
print("Jumlah harga(RP): ", sum(harga))

# Latihan 5
print("\nLatihan 5")
matriks= [
    [-10, 19, 82, 1],
    [-1, 2, 29, 32],
    [3, 231, 0, 8]
]
print("\nArray Matriks: ",)
for baris in matriks:
    print(baris)
for i, baris in enumerate(matriks, start=1):
    print(f"Baris {i}: ")
    for j, nilai in enumerate(baris, start=1):
        print(f"Kolom {j}: {nilai}")

# Latihan 6
print("\nLatihan 6")
matriks= [
    [-10, 19, 82, 1],
    [-1, 2, 29, 32],
    [3, 231, 0, 8]
]
print("\nArray Matriks: ",)
for baris in matriks:
    print(baris)
print("Elemen baris ke-2 kolom ke-4: ", matriks[1][3])

# Latihan 7
print("\nLatihan 7")
matriks= [
    [-10, 19, 82, 1],
    [-1, 2, 29, 32],
    [3, 231, 0, 8]
]
print("\nArray Matriks Awal: ",)
for baris in matriks:
    print(baris)
append= [12, 10, 20, 5]
matriks.append(append)
print("\nArray Matriks setelah ditambah: ",)
for baris in matriks:
    print(baris)

# Latihan 8
print("\nLatihan 8")
matriks= [
    [-10, 19, 82, 1],
    [-1, 2, 29, 32],
    [3, 231, 0, 8],
    [12, 10, 20, 5]
]
print("\nArray Matriks Awal: ",)
for baris in matriks:
    print(baris)
matriks[3].pop(2) # Menghapus elemen 3 pada baris ke-4
print("\nArray Matriks setelah dihapus: ")
for baris in matriks:
    print(baris)

# Latihan 9
print("\nLatihan 9")
matriks= [
    [-10, 19, 82, 1],
    [-1, 2, 29, 32],
    [3, 231, 0, 8],
    [12, 10, 20, 5]
]
print("\nArray Matriks Awal: ",)
for baris in matriks:
    print(baris)
matriks[3][3]= 14 # Mengubah elemen 5 pada baris ke-4 kolom ke-4
print("\nArray Matriks setelah diubah: ",)
for baris in matriks:
    print(baris)

# Latihan 10
print("\nLatihan 10")
List_Belanjaam= ["Sabun", "Shampo", "Pasta Gigi", "Sikat Gigi", "Bolpoint", "Kertas"]
print("\nList Belanjaan: ", List_Belanjaam)
List_Belanjaam[1]= "Sapu"
print("List Belanjaan setelah diubah: ", List_Belanjaam)

# Treasure Hunt
import colorama
from colorama import Fore, Style, init

print(Style.BRIGHT + Fore.CYAN + "\nTreasure Hunt" + Style.RESET_ALL)

# Peta
size= int(input(f"Masukkan ukuran peta: "))
treasure_map = ["-" for _ in range(size)] # Membuat peta dengan ukuran 10x10 dan menyembunyikan treasure

# Menentukan posisi treasure secara manual
print(Style.BRIGHT + Fore.GREEN + f"Selamat datang di Treasure Hunt! Peta memiliki {size} lokasi (0 hingga {size-1}).")
treasure_index= int(input(f"Masukkan posisi treasure (0-{size-1}): "))

while treasure_index < 0 or treasure_index >= size:
    print(Fore.RED + "Posisi treasure tidak valid!" + Style.RESET_ALL)
    treasure_index= int(input(f"Masukkan posisi treasure (0-{size-1}): ")) # Meminta input posisi treasure

treasure_map[treasure_index]= "X" # Menyimpan treasure pada peta

# Memulai permainan
def play_treasue_hunt():
    print(Style.BRIGHT + Fore.GREEN + "\nHarta karun telah disembunyikan di peta! Mulai permainan!" + Style.RESET_ALL)
    print(Style.BRIGHT + "Silahkan tebak posisi treasure (0-9)." + Style.RESET_ALL)

    # Loop permainan
    while True:
        # Menampilkan peta saat ini
        print("\nPeta saat ini:", ["_" for _ in range(size)]) # Peta tersembunyi

        # Meminta tebakan
        try:
            guess= int(input(Style.BRIGHT + f"Masukkan tebakanmu (0-{size-1}): "))
        except ValueError:
            print(Fore.RED + "Tebakan tidak valid!" + Style.RESET_ALL)
            continue

        # Validasi tebakan
        if guess < 0 or guess >= size:
            print(Fore.RED + "Tebakan tidak valid!" + Style.RESET_ALL)
            continue

        # Validasi tebakan benar/salah
        if treasure_map[guess]== "X":
            print(Fore.GREEN + "Selamat! Kamu menemukan harta karun!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Tebakanmu salah! Coba lagi." + Style.RESET_ALL)
    
    print(Style.BRIGHT + Fore.CYAN + "Permainan selesai!" + Style.RESET_ALL)

# Memulai permainan
play_treasue_hunt()
#Import modul TeganganArusResistansi

import vir

def main():
    #Rumus Tegangan (V)
    R = float(input("Masukkan nilai Resistansi: "))
    I = float(input("Masukkan nilai Arus: "))

    Tegangan = vir.Tegangan(R, I)

    print("R : ", R)
    print("I : ", I)
    print("Tegangan(R * I) = ", Tegangan)

    #Rumus Arus (I)
    V = float(input("\nMasukkan nilai Tegangan: "))
    R = float(input("Masukkan nilai Resistansi: "))

    Arus = vir.Arus(V, R)

    print("V : ", V)
    print("R : ", R)
    print("Arus(V / R ) = ", Arus)

    #Rumus Resistansi (R)

    V = float(input("\nMasukkan nilai Tegangan: "))
    I = float(input("Masukkan nilai Arus: "))
    Resistansi = vir.Resistansi(V, I)

    print("V : ", V)
    print("I : ", I)
    print("Resistansi(V / I ) = ", Resistansi)

if __name__ == "__main__":
    main()


from crypto_module import (
    menu_caesar,
    menu_rot13,
    menu_vigenere,
    menu_transposition,
    menu_exhaustive,
)


def tampilkan_menu():
    print("\n" + "=" * 60)
    print("           PROGRAM KRIPTOGRAFI KLASIK")
    print("=" * 60)
    print("1. Caesar Cipher")
    print("2. ROT13 Cipher")
    print("3. Vigenere Cipher")
    print("4. Transposition Cipher")
    print("5. Exhaustive Key Search (Caesar)")
    print("0. Keluar")
    print("=" * 60)


def clear_terminal():
    import os

    os.system("cls" if os.name == "nt" else "clear")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            menu_caesar()
        elif pilihan == "2":
            menu_rot13()
        elif pilihan == "3":
            menu_vigenere()
        elif pilihan == "4":
            menu_transposition()
        elif pilihan == "5":
            menu_exhaustive()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan program ini!")
            break
        else:
            print("\nPilihan tidak valid!")

        print("\n" + "-" * 60)
        lanjut = input(
            "Tekan Enter untuk lanjut (atau ketik 'c' untuk clear): "
        ).lower()

        if lanjut == "c":
            clear_terminal()


if __name__ == "__main__":
    main()

import string

uppercase: str = string.ascii_uppercase


def vigenereEncrypt(plaintext: str, key: str, show_process: bool = False):
    encrypt = ""
    plaintext_clean = plaintext.replace(" ", "").upper()
    key_upper = key.upper()
    key_index = 0
    process = []

    if show_process:
        process.append(f"Plaintext (tanpa spasi): {plaintext_clean}")
        process.append(f"Key: {key_upper}")
        process.append(f"Panjang key: {len(key_upper)}")
        process.append(f"Rumus: E(p) = (p + k) mod 26")
        process.append("\nProses enkripsi per karakter:")

    for index, char in enumerate(plaintext_clean):
        if char in uppercase:
            key_char = key_upper[key_index % len(key_upper)]
            shift = uppercase.index(key_char)
            char_index = uppercase.index(char)
            new_index = (char_index + shift) % 26
            encrypted_char = uppercase[new_index]

            if show_process:
                process.append(
                    f"  '{char}' (index {char_index}) + '{key_char}' (shift {shift}) "
                    f"= ({char_index} + {shift}) mod 26 = {new_index} → '{encrypted_char}'"
                )

            encrypt += encrypted_char
            key_index += 1
        else:
            if show_process:
                process.append(f"  '{char}' (bukan huruf) → '{char}'")
            encrypt += char

    if show_process:
        process.append(f"\nCiphertext: {encrypt}")

    return (encrypt, process) if show_process else encrypt


def vigenereDecrypt(ciphertext: str, key: str, show_process: bool = False):
    decrypt = ""
    cipher_clean = ciphertext.upper()
    key_upper = key.upper()
    key_index = 0
    process = []

    if show_process:
        process.append(f"Ciphertext: {cipher_clean}")
        process.append(f"Key: {key_upper}")
        process.append(f"Panjang key: {len(key_upper)}")
        process.append(f"Rumus: D(c) = (c - k) mod 26")
        process.append("\nProses dekripsi per karakter:")

    for index, char in enumerate(cipher_clean):
        if char in uppercase:
            key_char = key_upper[key_index % len(key_upper)]
            shift = uppercase.index(key_char)
            char_index = uppercase.index(char)
            new_index = (char_index - shift) % 26
            decrypted_char = uppercase[new_index]

            if show_process:
                process.append(
                    f"  '{char}' (index {char_index}) - '{key_char}' (shift {shift}) "
                    f"= ({char_index} - {shift}) mod 26 = {new_index} → '{decrypted_char}'"
                )

            decrypt += decrypted_char
            key_index += 1
        else:
            if show_process:
                process.append(f"  '{char}' (bukan huruf) → '{char}'")
            decrypt += char

    if show_process:
        process.append(f"\nPlaintext: {decrypt}")

    return (decrypt, process) if show_process else decrypt


def menu_vigenere():
    print("\n--- VIGENERE CIPHER ---")
    pilihan = input("Pilih (1=Enkripsi, 2=Dekripsi): ")

    if pilihan == "1":
        plaintext = input("Masukkan plaintext: ")
        key = input("Masukkan key (string): ")

        ciphertext, process = vigenereEncrypt(plaintext, key, show_process=True)

        print("\n--- PROSES ENKRIPSI ---")
        print(f"Rumus: E(p) = (p + k) mod 26")
        print(f"Plaintext: {plaintext}")
        print(f"Key: {key}")
        print("\nProses per karakter (10 pertama):")
        for p in process[:10]:
            print(f"  {p}")
        if len(process) > 10:
            print(f"  ... dan {len(process)-10} karakter lainnya")
        print(f"\nCiphertext: {ciphertext}")

    elif pilihan == "2":
        ciphertext = input("Masukkan ciphertext: ")
        key = input("Masukkan key (string): ")

        plaintext, process = vigenereDecrypt(ciphertext, key, show_process=True)

        print("\n--- PROSES DEKRIPSI ---")
        print(f"Rumus: D(c) = (c - k) mod 26")
        print(f"Ciphertext: {ciphertext}")
        print(f"Key: {key}")
        print("\nProses per karakter (10 pertama):")
        for p in process[:10]:
            print(f"  {p}")
        if len(process) > 10:
            print(f"  ... dan {len(process)-10} karakter lainnya")
        print(f"\nPlaintext: {plaintext}")

def transposEncrypt(plaintext: str, key: int, show_process: bool = False):
    encrypt = ""
    plaintext_clean = plaintext.replace(" ", "").upper()
    process = []

    if show_process:
        process.append(f"Plaintext (tanpa spasi): {plaintext_clean}")
        process.append(f"Jumlah kolom: {key}")
        process.append("\nMengisi baris (kiri ke kanan):")

    num_rows = (len(plaintext_clean) + key - 1) // key
    
    rows = []
    char_index = 0
    
    for row_num in range(num_rows):
        row = ""
        for col_num in range(key):
            if char_index < len(plaintext_clean):
                char = plaintext_clean[char_index]
                row += char
                if show_process:
                    process.append(f"  Karakter '{char}' (index {char_index}) → Baris {row_num}, Kolom {col_num}")
                char_index += 1
            else:
                row += "Ø"
                if show_process:
                    process.append(f"  Padding 'Ø' → Baris {row_num}, Kolom {col_num}")
        rows.append(row)

    if show_process:
        process.append(f"\nJumlah baris: {num_rows}")
        process.append("\nMatriks setelah pengisian:")
        for i, row in enumerate(rows):
            process.append(f"  Baris {i}: {row}")

    columns = [""] * key
    for col_num in range(key):
        for row in rows:
            columns[col_num] += row[col_num]
    
    if show_process:
        process.append("\nMembaca per kolom (vertikal):")
        for i, col in enumerate(columns):
            process.append(f"  Kolom {i}: {col}")

    encrypt = "".join(columns)

    if show_process:
        process.append(f"\nCiphertext: {encrypt}")

    return encrypt, process if show_process else encrypt
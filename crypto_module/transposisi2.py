def transposEncrypt2(plaintext: str, key: int):
    encrypt = ""
    plaintext = plaintext.replace(" ", "").upper()

    rows = [plaintext[i : i + key] for i in range(0, len(plaintext), key)]

    for col in range(key):
        for row in rows:
            if col < len(row):
                encrypt += row[col]
    return encrypt


def transposDecrypt2(ciphertext: str, key: int):
    decrypt = ""
    num_rows = len(ciphertext) // key
    extra = len(ciphertext) % key

    col_lengths = [num_rows + 1 if i < extra else num_rows for i in range(key)]

    columns = []
    start = 0
    for length in col_lengths:
        columns.append(ciphertext[start : start + length])
        start += length

    for i in range(max(col_lengths)):
        for col in columns:
            if i < len(col):
                decrypt += col[i]
    return decrypt


# def transposEncrypt(plaintext: str, key: int):
#     encrypt = ""
#     columns = [""] * key
#     plaintext = plaintext.replace(" ", "").upper()

#     for index, char in enumerate(plaintext):
#         column = index % key
#         columns[column] += char

#     max_len = max(len(col) for col in columns)

#     for i in range(key):
#         if len(columns[i]) < max_len:
#             columns[i] += "Ø" * (max_len - len(columns[i]))

#     encrypt = "".join(columns)
#     return encrypt


# def transposDecrypt(ciphertext: str, key: int):
#     decrypt = ""
#     total_chars = len(ciphertext)
#     num_rows = total_chars // key

#     columns = []
#     for i in range(key):
#         start = i * num_rows
#         end = start + num_rows
#         columns.append(ciphertext[start:end])

#     for i in range(num_rows):
#         for col in columns:
#             if i < len(col):
#                 decrypt += col[i]

#     decrypt = decrypt.replace("Ø", "")

#     return decrypt

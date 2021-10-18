# a = kunci1
# b = kunci2
# m = panjang karakter(26)
def egcd(a, b):  # menentukan nilai gcd
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b  # gcd adalah b
    return gcd, x, y  # mengembalikan nilai gcd, x, dan y


def modinv(a, m):  # menemukan nilai Modular Multiplicative Inverse (MMI)
    gcd, x, y = egcd(a, m)
    if gcd != 1:  # jika gcd tidak bernilai 1 maka
        return None  # tidak ada kembalian modulo
    else:
        return x % m  # mengembalikan nilai dari x yang di modulo


def affine_encrypt(text, key1):  # fungsi enkripsi affine cipher dengan parameter text dan key1
    # berikut adalah fungsi enkripsi affine cipher
    '''
    C = (a*P + b) % 26
    '''
    # mengembalikan cipher text
    # fungsi join untuk mengubah array list menjadi string
    # method chr berfungsi untuk mengembalikan nilai ascii, kemudian mencari karakter dari nilai ascii tersebut
    # ord berfungsi untuk mengubah sebuah karakter menjadi nilai ascii
    # nilai ascii dari variabel t dikurangi dengan nilai ascii dari A
    # key index [0] dikali dengan hasil pengurangan sebelumnya kemudian ditambahkan dengan key index[1]
    # hasil dari operasi perhitungan diatas kemudian di modulo 26 dan ditambahkan dengan nilai ascii dari A
    # fungsi text.upper().replace adalah untuk mengganti text yang diinputkan dengan huruf kapital semua
    return ''.join([chr(((key1[0]*(ord(t) - ord('A')) + key1[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


def main():
    # deklarasi text dan key
    text = 'SUCCESS IS NOT FINAL FAILURE IS NOT FATAL IT IS THE COURAGE TO CONTINUE THAT COUNTS'
    key1 = [3, 9]  # kunci1 = 3, kunci2 = 9

    # memanggil fungsi enkripsi
    affine_encrypted_text = affine_encrypt(text, key1)

    # menampilkan fungsi enkripsi
    print("\n--------------------------------ENKRIPSI 1----------------------------------")
    print('Plain Text: ', text)  # menampilkan plaintext
    print('Key: ', key1)  # menampilkan key untuk affine cipher
    # menampilkan hasil enkripsi affine cipher
    print('Affine Encrypted Text: {}'.format(affine_encrypted_text))


if __name__ == '__main__':
    main()


def generateKey(string, key):  # menggenerate key
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def vigenere_encryption(string, key):  # fungsi enkripsi vigenere cipher
    encrypt_text = []  # hasil enkripsi disimpan dalam variabe encrypt_text
    for i in range(len(string)):
        # ord berfungsi untuk mengubah sebuah karakter menjadi nilai ascii
        # nilai ascii dari string ditambah dengan nilai ascii dari key, kemudian di modulo 26
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')  # hasilnya akan ditambahkan dengan nilai ascii dari 'A'
        encrypt_text.append(chr(x))  # mengubah menjadi karakter
    # mengubah array list text yang dienkripsi menjadi string
    return("" . join(encrypt_text))


def vigenere_decryption(encrypt_text, key):  # fungsi dekripsi vigenere cipher
    decrypt_text = []  # hasil dekripsi disimpan dalam variabe decrypt_text
    for i in range(len(encrypt_text)):
        # ord berfungsi untuk mengubah sebuah karakter menjadi nilai ascii
        # nilai ascii dari encrypt_text dikurang dengan nilai ascii dari key lalu ditambahkan 26. Kemudian di modulo 26
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')  # hasilnya akan ditambahkan dengan nilai ascii dari 'A'
        decrypt_text.append(chr(x))  # mengubah menjadi karakter
    # mengubah array list text yang didekripsi menjadi string
    return("" . join(decrypt_text))


if __name__ == "__main__":
    print("\n--------------------------------ENKRIPSI 2----------------------------------")
    # menginputkan hasil enkripsi dari affine cipher (sebagai plaintext)
    string = input('Affine to Vigenere: ')
    keyword = input("Keyword: ")  # menginputkan keyword
    # menjalankan fungsi generateKey dan disimpan pada variabel key
    key = generateKey(string, keyword)
    # menjalankan fungsi enkripsi vigenere
    encrypt_text = vigenere_encryption(string, key)
    # menampilkan hasil enkripsi vigenere cipher
    print("Vigenere Encrypted Text:", encrypt_text)
    print("\n--------------------------------DEKRIPSI 1----------------------------------")
    # menampilkan hasil dekripsi vigenere cipher
    # ciphertextnya adalah hasil enkripsi dari vigenere cipher
    print("Vigenere Decrypted Text:", vigenere_decryption(encrypt_text, key))


# fungsi enkripsi dengan parameter decryption dan key
def affine_decrypt(decryption, key1):
    # berikut adalah fungsi dekripsi affine cipher
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    # mengembalikan plain text
    # fungsi join untuk mengubah array list menjadi string
    # method chr berfungsi untuk mengembalikan nilai ascii, kemudian mencari karakter dari nilai ascii tersebut
    # ord berfungsi untuk mengubah sebuah karakter menjadi nilai ascii
    # fungsi modinv untuk menemukan nilai mmi
    # key index[0] di modulo 26 kemudian dikali dengan hasil pengurangan nilai ascii variabel c dengan nilai ascii A dan dikurangi dengan key index [1]
    # nilai ascii dari variabel t dikurangi dengan nilai ascii dari A
    # hasil perhitungan tersebut kemudian di modulo 26 dan selanjutnya ditambah lagi dengan nilai ascii A
    return "".join([chr(((modinv(key1[0], 26)*(ord(c) - ord('A') - key1[1]))
                         % 26) + ord('A')) for c in decryption])


def main():
    affine_decryption = vigenere_decryption(encrypt_text, key)
    key1 = [3, 9]
    print("\n--------------------------------DEKRIPSI 2----------------------------------")
    # menampilkan hasil dekripsi affine cipher
    # ciphertextnya adalah hasil dekripsi dari vigenere cipher
    print('Affine Decrypted Text: ', (affine_decrypt(affine_decryption, key1)))


if __name__ == '__main__':
    main()

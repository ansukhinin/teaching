# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
# Вам необходимо установить библиотеку simplecrypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.
import simplecrypt

passwords = open("passwords.txt","r")

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

for password in passwords:
    password = password[:-1]
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(password, 'is wrong')
    else:
        print(password, 'is correct')

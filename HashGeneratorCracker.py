#Angel Cervera Ronda
#Password Hasher and Cracker

import hashlib
import itertools
import time

def hashear_contraseña(contraseña):
    print("Seleccione el modo de hashing")
    print("1- MD5")
    print("2- SHA1")
    print("3- SHA256")
    print("4- SHA512")

    opcion = int(input("Opcion: "))

    if opcion == 1:
        hash_object = hashlib.md5(contraseña)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
    elif opcion == 2:
        hash_object = hashlib.sha1(contraseña)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
    elif opcion == 3:
        hash_object = hashlib.sha256(contraseña)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
    elif opcion == 4:
        hash_object = hashlib.sha512(contraseña)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)
    else:
        print("Opcion no valida")

def crack_md5_fuerzabruta(charset, max_length, target_hash):
    print("Crackeando MD5 con fuerza bruta...")
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            word = "".join(guess)
            if hashlib.md5(word.encode()).hexdigest() == target_hash:
                print("Texto encontrado:", word)
                return
    print("No encontrado con fuerza bruta.")

def crack_sha1_fuerzabruta(charset, max_length, target_hash):
    print("Crackeando SHA1 con fuerza bruta...")
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            word = "".join(guess)
            if hashlib.sha1(word.encode()).hexdigest() == target_hash:
                print("Texto encontrado:", word)
                return
    print("No encontrado con fuerza bruta.")

def crack_sha256_fuerzabruta(charset, max_length, target_hash):
    print("Crackeando SHA256 con fuerza bruta...")
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            word = "".join(guess)
            if hashlib.sha256(word.encode()).hexdigest() == target_hash:
                print("Texto encontrado:", word)
                return
    print("No encontrado con fuerza bruta.")

def compareall():
    contraseña = input("Introduce la contraseña: ").encode('utf-8')
    maxlength = len(contraseña)
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    
    # Generar los hashes
    hash_md5 = hashlib.md5(contraseña).hexdigest()
    hash_sha1 = hashlib.sha1(contraseña).hexdigest()
    hash_sha256 = hashlib.sha256(contraseña).hexdigest()
    
    # Crackear MD5 y medir el tiempo
    start_time = time.time()
    crack_md5_fuerzabruta(charset, maxlength, hash_md5)
    md5_time = time.time() - start_time
    
    # Crackear SHA1 y medir el tiempo
    start_time = time.time()
    crack_sha1_fuerzabruta(charset, maxlength, hash_sha1)
    sha1_time = time.time() - start_time
    
    # Crackear SHA256 y medir el tiempo
    start_time = time.time()
    crack_sha256_fuerzabruta(charset, maxlength, hash_sha256)
    sha256_time = time.time() - start_time
    
    # Mostrar los tiempos
    print(f"Tiempo para crackear MD5: {md5_time:.2f} segundos")
    print(f"Tiempo para crackear SHA1: {sha1_time:.2f} segundos")
    print(f"Tiempo para crackear SHA256: {sha256_time:.2f} segundos")

def main():
    print("\nConvertidor contraseña a Hash")
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    while True:
        print("\nOpciones:")
        print("1. Hashear una contraseña")
        print("2. Crackear un hash MD5 con fuerza bruta")
        print("3. Crackear un hash SHA1 con fuerza bruta")
        print("4. Crackear un hash SHA256 con fuerza bruta")
        print("5. Comparar el tiempo de cracking de los distintos hash")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            contraseña = input("Introduce la contraseña a cifrar: ").encode('utf-8')
            hashear_contraseña(contraseña)
        elif opcion == "2":
            target_hash = input("Introduce el hash MD5 a crackear: ")
            crack_md5_fuerzabruta(charset, 5, target_hash)
        elif opcion == "3":
            target_hash = input("Introduce el hash SHA1 a crackear: ")
            crack_sha1_fuerzabruta(charset, 5, target_hash)
        elif opcion == "4":
            target_hash = input("Introduce el hash SHA256 a crackear: ")
            crack_sha256_fuerzabruta(charset, 5, target_hash)
        elif opcion == "5":
            compareall()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
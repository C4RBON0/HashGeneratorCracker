#Angel Cervera Ronda
#Password Hasher and Cracker
import hashlib
import itertools

def hashear_contraseña():
  contraseña = input("Introduce la contraseña a cifrar: ").encode('utf-8')

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

def crack_md5_fuerzabruta(charset, max_length):
    md5_hash = input("Introduce el hash MD5 a crackear: ")
    print("Crackeando con fuerza bruta...")
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            word = "".join(guess)
            if hashlib.md5(word.encode()).hexdigest() == md5_hash:
                print("Texto encontrado:", word)
                return
    print("No encontrado con fuerza bruta.")
    
def crack_sha1_fuerzabruta(charset, max_length):
    md5_hash = input("Introduce el hash SHA1 a crackear: ")
    print("Crackeando con fuerza bruta...")
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            word = "".join(guess)
            if hashlib.sha1(word.encode()).hexdigest() == md5_hash:
                print("Texto encontrado:", word)
                return
    print("No encontrado con fuerza bruta.")


def main():


  print("\nConvertidor contraseña a Hash")
  charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"



  while True:
    print("\nOpciones:")
    print("1. Hashear una contraseña")
    print("2. Crackear un hash MD5 con fuerza bruta")
    print("3. Crackear un hash SHA1 con fuerza bruta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
      hashear_contraseña()
    elif opcion == "2":
      crack_md5_fuerzabruta(charset,5)
    elif opcion == "3":
      crack_sha1_fuerzabruta(charset,5)
    elif opcion == "4":
      break
    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")



if __name__ == "__main__":
    main()


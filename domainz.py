import requests
import argparse

def iterar_sobre_archivo(path, funcion):
    try:
        with open(path, 'r') as f:
            for linea in f:
                elemento = linea.strip()  # Elimina espacios en blanco y saltos de línea
                funcion(elemento)
    except FileNotFoundError:
        print(f"El archivo {path} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def add_http(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url

def comprobar_enlace(url, file="enlaces_accesibles.txt"):
    url = add_http(url)
    try:
        response = requests.get(url, timeout=5)
        print(f"[{response.status_code}] - {url}")
        write_file(response.status_code, url, file)
    except requests.exceptions.RequestException as e:
        print(f"[Error] - {url}")
        write_file("Error", url, file)

def write_file(code, url, file="enlaces_accesibles.txt"):
    with open(file, 'a') as f:
        f.write(f"{code} - {url}\n")

def domainz(input):
    iterar_sobre_archivo(input, comprobar_enlace)
    print("Proceso finalizado.")

def parse_args():
    parser = argparse.ArgumentParser(description="Domainz")
    parser.add_argument("-f","--file", help="Ruta del archivo")
    return parser.parse_args()


if __name__ == "__main__":
    input = parse_args()
    domainz(input.file)

PALABRAS = ["api_key", "apikey", "token", "secret", "password"]

archivo = open("ventas.json", "r", encoding="utf-8")
contenido = archivo.read().lower()
archivo.close()

encontradas = []
for palabra in PALABRAS:
    if palabra in contenido:
        encontradas.append(palabra)

if len(encontradas) > 0:
    print("ERROR: posibles claves expuestas en ventas.json: " + ", ".join(encontradas))
    exit(1)

print("OK: no se han encontrado claves API expuestas.")
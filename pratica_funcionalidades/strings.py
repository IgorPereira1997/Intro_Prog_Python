name = "Igor"
surname = "Pereira"

frase = "O rato roeu a roupa do rei de Roma"

lista = frase.split(" ")

result = frase.find("rei")

fullName = name + " " + surname

print(fullName)

print(len(fullName))

print(fullName.lower())

print(fullName.upper())

print(fullName.strip())

print(lista)

print(result)

print(frase.replace("rei", "gay"))
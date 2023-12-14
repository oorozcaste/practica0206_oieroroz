import urllib.request
url = "http://textfiles.com/adventure/aencounter.txt"
file = (urllib.request.urlopen(url))
print(file)
texto = file.read()

lista_palabras = texto.split()
print(len(lista_palabras))








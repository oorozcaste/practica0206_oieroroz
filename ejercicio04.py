import urllib.request
url = "http://textfiles.com/adventure/aencounter.txt"
file = (urllib.request.urlopen(url))
print(file)
texto = file.read()
testua = str(texto)
lista_palabras = testua.split(" ")
print(len(lista_palabras))








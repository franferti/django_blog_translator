"""Vamos a construir un programa que sea un diccionario en inglés en python. Tenemos un archivo json llamado data asi que vamos a empezar abriéndolo"""

import json
import difflib #difflib es una libreria para encontrar palabras similares
from difflib import SequenceMatcher # con esto podemos saber el ratio de diferencia entre dos palabras. Pej - SequenceMatcher(None, "rain", "rainn").ratio() nos daría 0.8888888888888
from difflib import get_close_matches #con  esto nos devuelve una lista de palabras similares. Pej - get_close_matches(word, possibilities, n=3, cutoff=0.6) 
#en posibilities podemos pasar palabras o en nuestro caso el archivo data con todas las palabras. n sería el número de palabras que queremos y cutoff el ratio que queremos

data = json.load(open("data.json")) #se puede poner "r" para que lo abra en read mode pero si no se pone se abre asi por defecto

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #si el usuario mete delhi, la función buscará también Delhi
        return data[w.title()]
    elif w.upper() in data: 
        return data[w.upper()] 
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]) #el %s es como si fuera una variable y al poner % después, 
    #lo que hace es sustituir el %s por lo que va despues del %. Pej - Si a = 1 y ponemos "Hey %s there" % a el resultado será "Hey 1 there"
    #en nuestro caso concreto le estamos preguntando si quiso decir la primera palabra que nos da como palabra más parecida a la que escribió.
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. Please double check it"
        else:
            return "We didn`t understand your entry"
    else:
        return "The word does not exist. Please double check it"

word = input("Enter word: ")

output = translate(word)
"""
for item in output:
    print(item) #haciendo esto las definiciones aparecen una debajo de la otra y sin [""]. Lo malo es que si ponemos una palabra que no existe nos devuelve la frase en
    #columnas ya que la funcion tiene listas y str objects. Para ello vamos a crear una funcion:"""

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


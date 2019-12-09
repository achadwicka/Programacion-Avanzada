import Funciones as func
from Lectura import genotipos, todos, datos

# aca creo un diccionario al igual que con los genomas anteriores,
# pero ahora con los fenotipos de cada persona
fenotipos = {todos[i]: {"Altura": func.altura(genotipos[todos[i]]), "Ojos":
             func.ojos(genotipos[todos[i]]),
             "Pelo": func.pelo(genotipos[todos[i]]),
             "Piel": func.piel(genotipos[todos[i]]),
             "Nariz": func.nariz(genotipos[todos[i]]),
             "Pies": func.pies(genotipos[todos[i]]),
             "Vello": func.vello(genotipos[todos[i]]),
             "Guata": func.guata(genotipos[todos[i]]),
             "Problemas": func.problemas(genotipos[todos[i]])} for i in
             range(len(datos))}


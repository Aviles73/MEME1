import random 
meme_dict = {   
            "CRINGE": "Algo muy vergonzoso",
            "LOL": "Respuesta a algo gracioso",
            "XD" : "risa",
            "Parcero" : "amigo o conocido",
            "coquette" : "algo que es bonito y de color rosita"
            }

word = input("Escribe una palabra que no comprendas")

if word in meme_dict:
    print(word+ ":", meme_dict[word])
    
else:
    print("no tengo la definición de esa palabra,")
    clave = random.choise( meme_dict.keys() )
    print(clave+ ":", meme_dict[clave])

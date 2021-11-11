# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''

from random import randint
import numpy as np

if __name__ == '__main__':
    print("Ahora sí! buena suerte :)")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda

    suma = 0
    
    print("Comienza el Juego")
    
    tiro_1 = [randint(1, 10) for x in range(2)]
    
    print("El primer tiro es:", tiro_1)
    
    suma_tiro = np.sum(tiro_1)
    
    print("En Total suma", suma_tiro)
    eleccion = ""
    
    while True and eleccion !="N":
        if suma_tiro == 21:
            print("Gano!!")
        
        elif suma_tiro < 21:
            while suma_tiro <= 21:
                print("quiere elejir una carta mas?")
                eleccion = input("Y/N\n")
                if eleccion == str("Y"):
                    tiro_2 = randint(1, 10)
                    tiro_1.append(tiro_2)
                    suma_tiro += tiro_2
                    print("Tus cartas son",tiro_1,"En total suman",np.sum(tiro_1))
                elif eleccion ==str("N"):
                    print("El total de puntos obtenidos es",suma_tiro)
                    print("Fin del Juego")
                    break
                    
        else:
            print ("Perdío, Fin del Juego")
            break
            
    
    

from functools import reduce

def run():
    
    # print("funciones anonimas")
    # # a = lambda argumentos: expresion
    
    # palindromo = lambda string : string == string[::-1]
    # print(palindromo('ana'))
    
    #HIGH ORDER FUNCTIONS: FILTER, MAP, REDUCE
    # filter --> devuelve True or False según el valor esté dentro de los criterios
    # buscados o no. En caso de que no cumpla con la condición, no será devuelto 
    # y la lista se verá reducida por este filtro.
    # Map --> funciona muy parecido, pero su diferencia radica en que no puede eliminar 
    # valores de la lista del array entregado. Es decir, el output tiene la misma 
    # cantidad de valores que el input.
    # Cómo funciona reduce:

    # Reduce --> toma 2 valores entregados como parámetros y el iterador como 
    # otro parámetro. Realiza la función con estos 2 valores, y luego con el
    # resultado de esto y el valor que le sigue en el array. Y así hasta pasar
    # por todos los valores de la lista.
    
    #FILTER -------------------
    #lista de numero aleatorios, traes solo impares
    #lista comprehensions
    # lista=[1,43,23,76,4,2,7,-2,3]
    # odd = [i for i in lista if i%2!=0]
    # print(odd)
    
    #lista con
    # lista=[1,43,23,76,4,2,7,-2,3]
    
    # odd=[list(filter(lambda x : x%2!=0, lista))]
    
    # print(odd)
    
    #MAP  ------------------
    
    # lista=[1,2,3,4,5]
    #CON COMPREHENSIONS
    # odd = [i**2 for i in lista]
    # print(odd)

    #CON FUNCION ANONIMA
    
    # lista=[1,2,3,4,5]
    # odd=list(map(lambda x : x**2, lista))
    # print(odd)
    
    #REDUCE ----------------
    lista=[2,2,2,2,2]
    
    odd = reduce(lambda a, b : a*b, lista)
    print(odd)
    
    
    

    
    




if __name__=='__main__':
    run()
    
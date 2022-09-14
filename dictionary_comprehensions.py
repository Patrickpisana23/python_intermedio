import math
def run():
    
    #RETO
    # crear diccionario $cuyas llaves sean los 100 primeros numeros
    # naturales $valores sean esos numeros elevados al cubo
    #diccionario={}
    
    # for i in range(1,101):
    #     diccionario[i] = i**3
    # print(diccionario)
    
    
    #RETO 
    # numeros que no sean divisibles por 3
    # squares = [i**2 for i in range(1,101) if i%3!=0]
    # diccionario={}
    
    # # for i in range(1,101):
    # #     if i%3!=0:
    # #         diccionario[i]=i**3
    
    # # print(diccionario)
     
    
    # #mi MODO
    # diccionario=[ i**3 for i in range(1,101) if i%3!=0]
    # print(diccionario)
    
    #el PROFE
    
    # diccionario={i : i**3 for i in range(1,101) if i%3!=0}
    # print(diccionario)
    
    diccionario={i: math.sqrt(i) for i in range(1,1001)}
    print(diccionario)
    


if __name__=='__main__':
    run()
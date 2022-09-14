 
#LISTAS COMPRENHENSIONS
 

def run():
    #import math
    
    # lista = [1,2,3,4,5,7,8,9,10]
    
    # for i in range(1,101):
    #     listacuadrada=[]
    #     if i%3 != 0:
    #         listacuadrada.append(pow(i,2))
    #     print(listacuadrada)
    
    # squares = [i**2 for i in range(1,101) if i%3!=0]
    # print(squares)   
    
    lista = [i for i in  range(1,100000) if i%4==0 and i%18==0    ]
    print(lista)



if __name__=='__main__':
    run()


#DICCIONARIOS



# Crear una lista de los 10 primeros numeros naturales al cuadrado
#de los primeros 100



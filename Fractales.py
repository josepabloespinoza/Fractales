from turtle import*
import random
from math import*

### Hexagono ###
#Funcion Hexagono 
#Entradas:
#   lado = Un entero que sera el tamaño de un lado del hexagono
#   prof = Un entero que sera la profunidad con la que se ejecutara el hexagono
#Salidas:
#   El dibujo de un hexagono
#Restricciones: 
#   lado y prof deben ser enteros positivos
def Hexagono(prof,lado):
    #Funcion HexagonoAux
    #Entradas:
    #   lado = Un entero que sera el tamaño de un lado del hexagono
    #   prof = Un entero que sera la profunidad con la que se ejecutara el hexagono
    #Salidas:
    #   dibuja una linea
    #Restricciones: 
    #   lado y prof deben ser enteros positivos
    def HexagonoAux(prof,lado):
        if prof == 0:
            return
        if prof == 1: 
            for i in range(6):              
                HexagonoAux(prof -1,lado/3)
                forward(lado)
                right(60)           
        else:      
            for i in range(6):    
                HexagonoAux(prof -1,lado/3)
                penup()
                forward(lado/3)       
                forward(lado/3)     
                forward(lado/3)
                right(60)
                pendown()

    if not isinstance(lado,int) or not isinstance(prof,int) or lado < 0 or prof <= 0 :
        return "Debe ser numeros enteros"
    reset()
    tracer(0,0)
    colormode(255)
    hideturtle()
    penup()
    left(90)
    back((lado**2 - (lado/2)**2)**(1/2)/2)
    right(90)
    back(lado/2)
    pendown()
    left(60)
    HexagonoAux(prof,lado)
    update()

### Circulo de Ravel ###
def ravel(profundidad,radio):
    # Funcion que dibuja un circulo de ravel
    # Entradas: Profundidad, Radio
    # Restricciones : La profundidad es un entero positivo y el radio un numero real positivo
    # Salidas : El fractal del Circulo de Ravel
    if not isinstance (profundidad,int) or profundidad <= 0:
        return "La profundidad debe ser un numero entero positivo"   
    if not isinstance(radio,(float,int))  or radio <= 0 :
        return "El Radio un numero Real Positivo"
    def ravelAux(profundidad,radio):
        ### Subfuncion recursiva
        # Entradas : profundidad, radio
        # Restricciones: La profundidad es un entero positivo y el radio un numero real positivo
        # Salidas :  El fractal del Circulo de Ravel
        if profundidad == 1 :            
            circle(radio,360)
            return
        for i in range(3):                 
            ravelAux(profundidad-1,radio/2.15)           
            circle(radio,60)            
            ravelAux(profundidad-1,radio/2.15/2.075)            
            circle(radio,60)
    reset()
    tracer(0,0)
    hideturtle()
    speed(0)
    penup()
    right(90)
    forward(radio)
    right(270)
    circle(radio,30)
    pendown()
    ravelAux(profundidad,radio)
    update()



### Curva de Satie ###
#Funcion satie
#Entradas:
#    profundidad = Un entero que sera la profunidad con la que sera la Curva de satie
#    tamaño = Un entero que sera el tamaño de un lado
#Salidas:
#   El dibujo de la curva de satie
#Restricciones: 
#   profunididad y tamaño deben ser enteros positivos
def satie(profundidad,tamaño):
    #Funcion Auxsatie
    #Entradas:
    #    profundidad = Un entero que sera la profunidad con la que sera la Curva de satie
    #    tamaño = Un entero que sera el tamaño de un lado
    #Salidas:
    #   El dibujo de la curva de satie
    #Restricciones: 
    #   profunididad y tamaño deben ser enteros positivos
    def Auxsatie(profundidad,tamaño):
        
        x = ((tamaño/2)**2+(tamaño/4)**2)**(1/2)
        if profundidad==0:
            return
        if profundidad==1:
            left(26)
            forward(x)
            right(116)
            forward(tamaño/2) 
            left(116)
            forward(x)
            right(26)
        else:
            left(26)
            Auxsatie(profundidad-1,x)
            right(116)
            Auxsatie(profundidad-1,tamaño/2)
            left(116)
            Auxsatie(profundidad-1,x)
            right(26)
    if not isinstance(profundidad,int) or not isinstance(tamaño,int) or tamaño <= 0 or profundidad <= 0:
            return "Debe ser numeros enteros y mayores que 0"
    reset()
    tracer(0,0)
    hideturtle()
    Auxsatie(profundidad,tamaño)
    update()


###Funcion de la estrella de debussy###
def debussy(prof,lado,n,rela):
    #Dibuja la estrella de Debussy
    # Entradas: Lado(medida del lado), Profundidad(cantidad de veces que repite),
    # n(numero de picos), Relacion(parametro con el que se va disminuyendo el lado)
    # Restricciones : Profundidad, n, lado son numeros enteros positivos y relacion puede ser flotante
    # Salidas: Fractal de la estrella de Debussy
    if not isinstance(rela,(int,float)) or prof < 0:
        return "La relacion debe ser un numero positivo mayor que 0(Puede ser flotante)"
    if not isinstance(n,int) or n < 1:
        return "El numero de picos debe ser un entero positivo"
    if not isinstance(lado,int) or lado < 1:
        return "El lado debe ser un entero positivo"
    if not isinstance(prof,int) or prof < 1:
        return "La profundidad debe ser un entero positivo"
    costa = 0
    def debussyAux(prof,lado,n,rela,costa):
    # Subfuncion recursiva
    # Entradas: profundidad, lado, n , relacion, costa(variable contador)
    # Restricciones: Profundidad, n, lado son numeros enteros positivos y relacion puede ser flotante
    # Salida : Fractal de la estrella de Debussy
        if prof == 0:
            return
        elif prof == 1:
            for i in range(n):
                angulo = 360/(n+1)
                forward(lado )
                right(180)
                debussyAux(prof-1,lado * rela,n,rela,costa)
                right(180)
                back(lado)
                right(360/n)
            return 
        else :
            if costa == 0:
                costa+=1
                for i in range(n):
                    angulo = 360/n
                    forward(lado )
                    right(180)
                    right(angulo)
                    debussyAux(prof-1,lado * rela,n,rela,costa)
                    left(angulo)
                    right(180)
                    back(lado)
                    right(360/n)                    
            else:            
                for i in range(n-1):
                    angulo = 360/n
                    forward(lado )
                    right(180)
                    right(angulo)
                    debussyAux(prof-1,lado * rela,n,rela,costa)
                    right(180)
                    left(angulo)
                    back(lado)
                    right(360/n)
                right(angulo)
    reset()
    tracer(0,0)
    hideturtle()
    speed(0)
    debussyAux(prof,lado,n,rela,costa)
    update()

### Curva del Dragon ###
#Funcion dragon
#Entradas:
#    profundidad = Un entero que sera la profunidad con la que sera la Curva de satie
#    tamaño = Un entero que sera el tamaño de un lado
#Salidas:
#   El dibujo de la Curva del dragon
#Restricciones: 
#   profunididad y tamaño deben ser enteros positivos
def dragon(profundidad,tamaño):
    #Funcion dragonAux
    #Entradas:
    #    tamaño = Un entero que sera el tamaño de un lado
    #    lista = una lista de string que determinan la dirección del giro
    #Salidas:
    #   El dibujo de la Curva del dragon
    #Restricciones: 
    #   tamaño deben ser enteros positivos
    def dragonAux(tamaño,lista):
        if len(lista) == 0:
            forward(tamaño)
            return 
        if len(lista) == 1:
            forward(tamaño)
            if lista[0] == "D":
                right(90)
            else:
                left(90)
            dragonAux(tamaño,lista[1:])
        if len(lista) != 1 :
            forward(tamaño)
            if lista[0] == "D":
                right(90)
            else:
                left(90)
            dragonAux(tamaño,lista[1:])
    
    #Funcion listaC
    #Entradas:
    #    veces: cantidad de iteraciones que debe realizar para generar la lista
    #Salidas:
    #   lista: Una lista con los movimientos 
    #Restricciones: 
    #   veces debe ser un numero entero
    def listaC(veces):
        lista = ["D"]
        nuevalista = ["D"]
        contador = 2
        sumaRonda = 4
        for i in range(veces):
            posicionesD = 0
            posicionesI = 2
            ciclo= len(lista) + contador
            for j in range(len(lista)): 
                if (len(nuevalista)) < ciclo:            
                    nuevalista.insert(posicionesD,"D")                
                    nuevalista.insert(posicionesI,"I")
                    posicionesD+=sumaRonda
                    posicionesI+=sumaRonda 
            lista = nuevalista
            contador = contador*2 
        return lista
    
    if not isinstance(profundidad,int) or not isinstance(tamaño,int) or tamaño <= 0 or profundidad < 0:
            return "Debe ser numeros enteros y tamaño mayor  que 0"
    reset()
    for i in range(profundidad):
        left(45)
    tracer(0,0)
    hideturtle()
    lista = listaC(profundidad+1)
    dragonAux(tamaño,lista)
    update()



###Fractal de Chopin###
from turtle import*
from random import*

def chopin(lado,minimo):
    # Funcion que dibuja el fractal de chopin
    # Entradas : lado y minimo
    # Restricciones : lado y minimo son numero enteros positivos
    # Salida : Fractal de chopin
    if not isinstance (lado,int) or lado <= 0:
        return "Lado debe ser un numero entero positivo"
    if not isinstance(minimo,int) or minimo <= 0:
        return "Minimo deber ser un numero entero positivo"
    if minimo >= lado:
        return "Lado debe ser mayor que minimo"
    def generarnumero():
        # SubFuncion generar numero #
        # Selecciona aleatoriamente uno de los numeros validos y lo retorna
        # Entradas : Nada
        # Restriccion : Nada
        # Salidas; El numero aleatoria de la lista
        lista = [2,3,5,8]
        return choice(lista)
    def chopinAux(lado,minimo):
        # Subfuncion recursiva que dibuja
        # Entradas : lado, minimo
        # Restricciones : lado y minimo son numero enteros positivos
        # Salida : Fractal de chopin
        if lado < minimo:
            forward(lado)
        else:
            chopinAux(lado*0.61803398875,minimo)
            ##ramas
            cant = generarnumero()
            ang = 180/(cant+1)
            left(180)
            for i in range(cant):
                right(ang)
                chopinAux(lado/5,minimo)
                right(180)
                chopinAux(lado/5,minimo)
                right(180)
            right(ang)
            chopinAux(lado*(1-0.61803398875),minimo)
    reset()
    tracer(0,0)
    hideturtle()
    speed(0)
    penup()
    back(lado/2)
    pendown()
    chopinAux(lado,minimo)
    update()


#####################FUNCIONES ANIMADAS########################################

### Hexagono ###
#Funcion HexagonoP 
#Entradas:
#   lado = Un entero que sera el tamaño de un lado del hexagono
#   prof = Un entero que sera la profunidad con la que se ejecutara el hexagono
#Salidas:
#   El dibujo de un hexagono animado
#Restricciones: 
#   lado y prof deben ser enteros positivos
def HexagonoP(prof,lado):
    mzo = 0
    #Funcion HexagonoPAux
    #Entradas:
    #   lado = Un entero que sera el tamaño de un lado del hexagono
    #   prof = Un entero que sera la profunidad con la que se ejecutara el hexagono
    #Salidas:
    #   dibuja una linea
    #Restricciones: 
    #   lado y prof deben ser enteros positivos
    def HexagonoPAux(prof,lado):
        if prof == 0:
            return
        if prof == 1:
            colores = choice(["Red","Gold","Silver"])
            fillcolor(colores)   
            begin_fill()
            
        if prof == 1:
            
            for i in range(6):
                HexagonoPAux(prof -1,lado/3)
                forward(lado)
                right(60)           
        else:
            
            for i in range(6): 
                HexagonoPAux(prof -1,lado/3)
                penup()
                forward(lado/3)  
                forward(lado/3)       
                forward(lado/3)
                right(60)
                pendown()        
        if prof == 1:
            end_fill()
    if not isinstance(lado,int) or not isinstance(prof,int) or lado < 0 or prof < 0:
            return "Debe ser numeros enteros"
    tracer(0,0)
    colormode(255)
    hideturtle()
    penup()
    left(90)
    back((lado**2 - (lado/2)**2)**(1/2)/2)
    right(90)
    back(lado/2)
    pendown()
    left(60)
    HexagonoPAux(prof,lado)
    update()
        
    while True:
        bgcolor("Black")
        pencolor("Black")
        reset()
        mzo += 10
        karma =  choice([10,-10])
        penup()
        circle(10,mzo)
        forward(karma)
        pendown()
        HexagonoPAux(prof,lado)

### Circulo de Ravel ###


def validad(profundidad,radio):
    if not isinstance (profundidad,int) or profundidad <= 0:
        return "La profundidad debe ser un numero entero positivo"   
    if not isinstance(radio,(float,int))  or radio <= 0 :
        return "El Radio un numero Real Positivo"
    return True
def RavelP(profundidad,radio):
    bgcolor("Black")
    # Funcion con un ciclo infinito que dibuja un circulo de ravel personalizado que gira y cambia de color
    # Entradas: Profundidad, Radio
    # Restricciones : La profundidad es un entero positivo y el radio un numero real positivo
    # Salidas : El fractal del Circulo de Ravel personalizado
    variante = 1
    valido = validad(profundidad,radio)
    #Esto permite  girar y cambiar de color#   
    while valido == True:
        variante += 3
        ravelP(profundidad,radio,variante)
        reset()
    else:
        return valido
def ravelP(profundidad,radio,variante):
    # Funcion que dibuja un circulo de ravel personalizado que gira y cambia de color
    # Entradas: Profundidad, Radio, Variante
    # Restricciones : La profundidad es un entero positivo y el radio un numero real positivo
    # Salidas : El fractal del Circulo de Ravel personalizado
    def ravelAux(profundidad,radio):
        ### Subfuncion recursiva
        # Entradas : profundidad, radio
        # Restricciones: La profundidad es un entero positivo y el radio un numero real positivo
        # Salidas :  El fractal del Circulo de Ravel personalizado
        #Color#
        pencolor(randrange(255),
                 randrange(255),
                 randrange(255))      
        if profundidad == 1 :
            circle(radio,360)
            return
        for i in range(3):
            ravelAux(profundidad-1,radio/2.15)
            circle(radio,60)
            ravelAux(profundidad-1,radio/2.15/2.075)
            circle(radio,60)
    
    tracer(0,0)
    
    hideturtle()
    colormode(255)
    speed(0)
    penup()
    right(90)
    forward(radio)
    right(270)
    circle(radio,30+variante)
    pendown()
    ravelAux(profundidad,radio)
    update()


### Curva de Satie ###
#Funcion satieP
#Entradas:
#    profundidad = Un entero que sera la profunidad con la que sera la Curva de satie
#    tamaño = Un entero que sera el tamaño de un lado
#Salidas:
#   El dibujo de la curva de satie
#Restricciones: 
#   profunididad y tamaño deben ser enteros positivos
def satieP(profundidad,tamaño):
    
    x = 0
    #Funcion Auxsatie
    #Entradas:
    #    profundidad = Un entero que sera la profunidad con la que sera la Curva de satie
    #    tamaño = Un entero que sera el tamaño de un lado
    #Salidas:
    #   El dibujo de la curva de satie
    #Restricciones: 
    #   profunididad y tamaño deben ser enteros positivos
    def AuxsatieP(profundidad,tamaño):
        
        x = ((tamaño//2)**2+(tamaño//4)**2)**(1/2)
        if profundidad==0:
            return
        if profundidad==1:
            left(26)
            forward(x)
            right(116)
            forward(tamaño/2) 
            left(116)
            forward(x)
            right(26)
        else:
            left(26)
            AuxsatieP(profundidad-1,x)
            right(116)
            AuxsatieP(profundidad-1,tamaño/2)
            left(116)
            AuxsatieP(profundidad-1,x)
            right(26)
    if not isinstance(profundidad,int) or not isinstance(tamaño,int) or tamaño <= 0 or profundidad <= 0:
            return "Debe ser numeros enteros y mayores que 0"
    tracer(0,0)
    bgcolor("silver")
    AuxsatieP(profundidad,tamaño)
    update()
    hideturtle()
    while True: 
        if x <= 10:
            left(26)
            penup()
            forward(tamaño)
            pendown()
            x = 0
        left(65)
        pensize(3)
        pencolor (choice(["red","blue","violet","brown","green"]))
        x+= 10
        satieP(profundidad,tamaño)


###Estrella de Debussy personalizada###
def DebussyP(prof,lado,n,rela):
    #Dibuja la estrella de Debussy
    # Entradas: Lado(medida del lado), Profundidad(cantidad de veces que repite),
    # n(numero de picos), Relacion(parametro con el que se va disminuyendo el lado)
    # Restricciones : Profundidad, n, lado son numeros enteros positivos y relacion puede ser flotante
    # Salidas: Fractal de la estrella de Debussy
    def esvalidoP(prof,lado,n,rela):
        # Revisa si los datos son validos
        # Entradas: Lado(medida del lado), Profundidad(cantidad de veces que repite),
        # n(numero de picos), Relacion(parametro con el que se va disminuyendo el lado)
        # Restricciones : Profundidad, n, lado son numeros enteros positivos y relacion puede ser flotante
        # Salidas: Fractal de la estrella de Debussy
        if not isinstance(rela,(int,float)) or rela < 0:
            return "La relacion debe ser un numero positivo mayor que 0(Puede ser flotante)"
        if not isinstance(n,int) or n < 1:
            return "El numero de picos debe ser un entero positivo"
        if not isinstance(lado,int) or lado < 1:
            return "El lado debe ser un entero positivo"
        if not isinstance(prof,int) or prof < 1:
            return "La profundidad debe ser un entero positivo"
        return True
    karma = 0
    oso = 0
    vali = esvalidoP(prof,lado,n,rela)
    while vali == True:
        reset()
        debussyP(prof,lado,n,rela,karma,oso)
        karma += 1
        oso += 1
    else :
        return vali
def debussyP(prof,lado,n,rela,karma,oso):
        #Dibuja la estrella de Debussy
        # Entradas: Lado(medida del lado), Profundidad(cantidad de veces que repite),
        # n(numero de picos), Relacion(parametro con el que se va disminuyendo el lado)
        # karma y oso son variables oara personalizar
        # Restricciones : Profundidad, n, lado son numeros enteros positivos y relacion puede ser flotante
        # Salidas: Fractal de la estrella de Debussy
    costa = 0
    prof += karma
    lado += karma
    n += oso   
    def debussyPAux(prof,lado,n,rela,costa):
    # Subfuncion recursiva
    # Entradas: profundidad, lado, n , relacion, costa(variable contador)
    # Restricciones: Profundidad, n, lado son numeros enteros positivos y relacion puede ser flotante
    # Salida : Fractal de la estrella de Debussy
        pencolor(randrange(255),randrange(255),randrange(255)) 
        if prof == 0:
            return
        elif prof == 1:
            for i in range(n):
                angulo = 360/(n+1)
                forward(lado )
                right(180)
                debussyPAux(prof-1,lado * rela,n,rela,costa)
                right(180)
                back(lado)
                right(360/n)
            return                    
        else :
            if costa == 0:
                costa+=1                
                for i in range(n):
                    angulo = 360/n
                    forward(lado )
                    right(180)
                    right(angulo)
                    debussyPAux(prof-1,lado * rela,n,rela,costa)
                    left(angulo)
                    right(180)
                    back(lado)
                    right(360/n)                    
            else:            
                for i in range(n-1):
                    angulo = 360/n
                    forward(lado )
                    right(180)
                    right(angulo)
                    debussyPAux(prof-1,lado * rela,n,rela,costa)
                    right(180)
                    left(angulo)
                    back(lado)
                    right(360/n)
                right(angulo)
    colormode(255)
    hideturtle()
    speed(0)    
    debussyPAux(prof,lado,n,rela,costa)
    update()

### Curva del Dragon ###
#Funcion dragonP
#Entradas:
#    profundidad = Un entero que sera la profunidad con la que sera la Curva de satie
#    tamaño = Un entero que sera el tamaño de un lado
#Salidas:
#   El dibujo de la Curva del dragon
#Restricciones: 
#   profunididad y tamaño deben ser enteros positivos
def dragonP(profundidad,tamaño):
    if not isinstance(profundidad,int) or not isinstance(tamaño,int) or tamaño <= 0 or profundidad < 0:
            return "Debe ser numeros enteros y tamaño mayor  que 0"
    reset()
    tracer(0,0)
    hideturtle()
    lista = listaC(profundidad+1)
    bgcolor("black")
    x=90
    while True:
        #circle(10,10)
        right(45)
        for n in range(50):
            pencolor(choice(["blue","red","gold","silver","white","yellow","green"]))
            for x in range(4):
                forward(x)
                dragon2(profundidad,tamaño,lista)
                update()
                x+90
### Curva del Dragon ###
#Funcion dragon2
#Entradas:
#    profundidad = Un entero que sera la profunidad con la que sera la Curva de satie
#    tamaño = Un entero que sera el tamaño de un lado
#Salidas:
#   El dibujo de la Curva del dragon
#Restricciones: 
#   profunididad y tamaño deben ser enteros positivos                
def dragon2(profundidad,tamaño,lista):
    for i in range(profundidad):
        left(45)
    #Funcion dragonAux
    #Entradas:
    #    tamaño = Un entero que sera el tamaño de un lado
    #    lista = una lista de string que determinan la dirección del giro
    #Salidas:
    #   El dibujo de la Curva del dragon
    #Restricciones: 
    #   tamaño deben ser enteros positivos
    def dragonAux2(tamaño,lista):
        if len(lista) == 0:
            forward(tamaño)
            return 
        if len(lista) == 1:
            forward(tamaño)
            if lista[0] == "D":
                right(90)
            else:
                left(90)
            dragonAux2(tamaño,lista[1:])
        if len(lista) != 1 :
            forward(tamaño)
            if lista[0] == "D":
                right(90)
            else:
                left(90)
            dragonAux2(tamaño,lista[1:])
    dragonAux2(tamaño,lista)
#Funcion listaC
    #Entradas:
    #    veces: cantidad de iteraciones que debe realizar para generar la lista
    #Salidas:
    #   lista: Una lista con los movimientos 
    #Restricciones: 
    #   veces debe ser un numero entero    
def listaC(veces):
    lista = ["D"]
    nuevalista = ["D"]
    contador = 2
    sumaRonda = 4
    for i in range(veces):
        posicionesD = 0
        posicionesI = 2
        ciclo= len(lista) + contador
        for j in range(len(lista)): 
            if (len(nuevalista)) < ciclo:            
                nuevalista.insert(posicionesD,"D")                
                nuevalista.insert(posicionesI,"I")
                posicionesD+=sumaRonda
                posicionesI+=sumaRonda 
        lista = nuevalista
        contador = contador*2 
    return lista
    



        

    







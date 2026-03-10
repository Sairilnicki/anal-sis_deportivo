nombre_del_jugador1 =input("colocar nombre")
nombre_del_jugador2 =input("colocar nombre")



nombre1_goles = int(input(f"insertar los goles de {nombre_del_jugador1} "))
nombre1_partidos = int(input(f"partidos disputados de {nombre_del_jugador1}"))

nombre2_goles = int(input(f"insertar los goles de {nombre_del_jugador2} "))
nombre2_partidos = int(input(f"partidos disputados de {nombre_del_jugador2}"))

if nombre1_partidos > 0:
    efectividad1= nombre1_goles/ nombre1_partidos
    print(f"la efectividad de{nombre_del_jugador1} es {efectividad1:.2f}")

else: 
    print("no se puede calcular la efectividad si no jugo ningun partido pavo")
    

if nombre1_goles > 0:
    efectividad_nombre2 = nombre2_goles/ nombre2_partidos
    print(f"la efectividad de {nombre_del_jugador2} es {efectividad_nombre2:.2f}")

else: 
    print("no se puede calcular la efectividad si no jugo ningun partido pavo")

if efectividad1 > efectividad_nombre2:
    print(f"el mejor es {nombre_del_jugador1}")

elif efectividad_nombre2 > efectividad1:
    print(f"el mejor es {nombre_del_jugador2}")

else:
    print("tienen los mismos goles")


          


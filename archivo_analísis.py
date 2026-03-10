cavani_goles = int(input("insertar los goles de cavani"))
cavani_partidos = int(input("partidos disputados"))

merentiel_goles = int(input("insertar los goles de merentiel"))
merentiel_partidos = int(input("partidos disputados"))

if cavani_partidos > 0:
    efectividad_cavani = cavani_goles / cavani_partidos
    print(f"la efectividad de cavani es {efectividad_cavani:.2f}")

else: 
    print("no se puede calcular la efectividad si no jugo ningun partido pavo")
    

if cavani_partidos > 0:
    efectividad_merentiel = merentiel_goles / merentiel_partidos
    print(f"la efectividad de la bestia es {efectividad_merentiel:.2f}")

else: 
    print("no se puede calcular la efectividad si no jugo ningun partido pavo")

if efectividad_cavani > efectividad_merentiel:
    print("el muerto de cavani gana en efectividad")

elif efectividad_merentiel > efectividad_cavani:
    print("la bestia gana en efectividad")

else:
    print("tienen los mismos goles")


          


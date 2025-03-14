from vpython import *
import math
cabe = box(pos=vector(1.5, 1.6, 0), size=vector(1.6, 1.2, 1.6), color=color.gray(0.5))
cuerpo = box(pos=vector(0, 0, 0), size=vector(2.5, 1.5, 3), color=color.gray(0.5))



# Crear las patas (cilindros)
pata1 = cylinder(pos=vector(1, -1.5, 1), axis=vector(0, 1, 0), radius=0.3, color=color.gray(0.5))
pata2 = cylinder(pos=vector(1, -1.5, -1), axis=vector(0, 1, 0), radius=0.3, color=color.gray(0.5))
pata3 = cylinder(pos=vector(-1, -1.5, 1), axis=vector(0, 1, 0), radius=0.3, color=color.gray(0.5))
pata4 = cylinder(pos=vector(-1, -1.5, -1), axis=vector(0, 1, 0), radius=0.3, color=color.gray(0.5))

manta= box(pos=vector(0, 1, 0), size=vector(2, 0.1, 2), color=color.magenta)
manta1= box(pos=vector(0, 0.4, 1.5), size=vector(1.6, 1.3, 0.1), color=color.cyan)
manta2= box(pos=vector(0, 0.4, -1.5), size=vector(1.6, 1.3, 0.1), color=color.cyan)

tobillera1 = ring(pos=pata1.pos + vector(0, 0.1, 0), axis=vector(0, 1, 0), radius=0.35, thickness=0.05, color=color.yellow)
tobillera2 = ring(pos=pata2.pos + vector(0, 0.1, 0), axis=vector(0, 1, 0), radius=0.35, thickness=0.05, color=color.yellow)
tobillera3 = ring(pos=pata3.pos + vector(0, 0.1, 0), axis=vector(0, 1, 0), radius=0.35, thickness=0.05, color=color.yellow)
tobillera4 = ring(pos=pata4.pos + vector(0, 0.1, 0), axis=vector(0, 1, 0), radius=0.35, thickness=0.05, color=color.yellow)


# Valores del balanceo
amplitud = 45      # Ángulo máximo de inclinación en grados
frecuencia = 0.2   # Control de la velocidad del balanceo
tiempo = 0

while True:
    rate(30)
     
    angulo = amplitud * math.sin(frecuencia * tiempo)
    
  
    pata1.axis = vector(0, 1.5, 0)
    pata1.rotate(angle=math.radians(angulo), axis=vector(0.5, 1, 0), origin=pata1.pos)
    
 
    pata2.axis = vector(0, 1.5, 0)
    pata2.rotate(angle=math.radians(angulo), axis=vector(0.5, 1, 0), origin=pata2.pos)
    
    
    pata3.axis = vector(0, 1.5, 0)
    pata3.rotate(angle=math.radians(angulo), axis=vector(0.5, 1, 0), origin=pata3.pos)
    
    
    pata4.axis = vector(0, 1.5, 0)
    pata4.rotate(angle=math.radians(angulo), axis=vector(0.5, 1, 0), origin=pata4.pos)
    
    tiempo += 0.1



"""

Ejemplo de programa base de control del sensor ultrasónico para el robot educador LEGO® MINDSTORMS® EV3
-----------------------------------------------------------------------------------

Este programa requiere LEGO® EV3 MicroPython v2.0.
Descargar: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Las instrucciones de construcción se encuentran en:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot

Otro material para leer https://pybricks.com/ev3-micropython/robotics.html

https://tutorials.aposteriori.com.sg/110-Pybricks-Basics/99-Special-Topics/10-DriveBase-vs-Move-Steering.html
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# le damos nombre al robot . en este caso ev3
ev3 = EV3Brick()

# nombramos el sensor e indicamos el puerto. ultra es es el nombre que elegí

ultra = UltrasonicSensor(Port.S1)

# Creamos las variables Motor indicando el puerto, en este caso serán motor izquierdo y derecho
# 
right_motor = Motor(Port.D)
left_motor  = Motor(Port.B)

#La base motriz se compone de dos motores, con una rueda en cada uno.

# wheel_diameter Los valores de diámetro de rueda y vía del eje se utilizan para que los motores se muevan a la velocidad correcta al dar una orden.

#axle_track Largo del  eje es la distancia entre los puntos donde las ruedas tocan el suelo.

robot = DriveBase(left_motor , right_motor, wheel_diameter=55.5, axle_track=146)

# emite un beep en el parlante
ev3.speaker.beep()

#El siguiente bucle hace que el robot avance hasta que detecta un obstáculo. 
#Luego retrocede y da la vuelta. Continúa así hasta que se detiene el programa.
while True:
    # Comience a avanzar a 200 milímetros por segundo.
    robot.drive(200, 0)

    # Espere hasta que se detecte un obstáculo.
    # Esto se logra repetidamente sin hacer nada (esperando 10 milisegundos) mientras la distancia medida siga siendo superior a 300 mm.
    # un esperar hasta que haya algo a menos de 30 cm
    while ultra.distance() > 300:
        wait(10)

    # Conduzca hacia atrás durante 300 milímetros.
    robot.straight(-300)

    # Girar 120 grados
    robot.turn(120)

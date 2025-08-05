#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Motores
motor_izquierdo = Motor(Port.C)
motor_derecho = Motor(Port.B)

# Sensores
sensor_izquierdo = ColorSensor(Port.S1)
sensor_derecho = ColorSensor(Port.S4)

# Base del robot
robot = DriveBase(motor_izquierdo, motor_derecho, wheel_diameter=55.5, axle_track=104)

# Velocidad constante
VELOCIDAD = 90
GIRO = 100  # Valor de giro (ajústalo si gira demasiado o muy poco)

# Bucle principal
while True:
    valor_izquierdo = sensor_izquierdo.reflection()
    valor_derecho = sensor_derecho.reflection()

    if valor_izquierdo < 10:
        # Gira a la derecha
        robot.drive(VELOCIDAD, GIRO)
    elif valor_derecho < 10:
        # Gira a la izquierda
        robot.drive(VELOCIDAD, -GIRO)
    else:
        # Sigue recto
        robot.drive(VELOCIDAD, 0)

    wait(10)

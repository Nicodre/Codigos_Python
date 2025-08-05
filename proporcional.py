from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Motores
motor_izquierdo = Motor(Port.B)
motor_derecho = Motor(Port.C)

# Sensores de color (uno a la izquierda y otro a la derecha)
sensor_izquierdo = ColorSensor(Port.S1)
sensor_derecho = ColorSensor(Port.S4)

# Base del robot
robot = DriveBase(motor_izquierdo, motor_derecho, wheel_diameter=55.5, axle_track=104)

# Valores de luz (ajusta según tu entorno)
NEGRO = 9
BLANCO = 85
umbral = (NEGRO + BLANCO) / 2  # Por ejemplo: 47

# Parámetros del control
VELOCIDAD = 100
GANANCIA_PROPORCIONAL = 1.2

# Bucle principal
while True:
    # Leer luz reflejada de ambos sensores
    valor_izquierdo = sensor_izquierdo.reflection()
    valor_derecho = sensor_derecho.reflection()

    # Calcular error como diferencia entre los sensores
    error = valor_izquierdo - valor_derecho

    # Calcular giro proporcional al error
    velocidad_giro = GANANCIA_PROPORCIONAL * error

    # Mover el robot
    robot.drive(VELOCIDAD, velocidad_giro)

    wait(10)

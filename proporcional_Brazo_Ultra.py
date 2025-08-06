from pybricks.ev3devices import Motor, ColorSensor, InfraredSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Motores
motor_izquierdo = Motor(Port.B)
motor_derecho = Motor(Port.C)
brazo = Motor(Port.A)  # Motor del brazo circular

# Sensores
sensor_izquierdo = ColorSensor(Port.S1)
sensor_derecho = ColorSensor(Port.S4)
sensor_ir = InfraredSensor(Port.S3)

# Base del robot
robot = DriveBase(motor_izquierdo, motor_derecho, wheel_diameter=55.5, axle_track=104)

# Valores de luz
NEGRO = 9
BLANCO = 85
umbral = (NEGRO + BLANCO) / 2

# Parámetros de control
VELOCIDAD = 100
GANANCIA_PROPORCIONAL = 1.2

# Función para cerrar el brazo
def cerrar_brazo():
    brazo.run_angle(500, -90)  # Ajusta el ángulo según tu diseño
    brazo.stop()

# Bucle principal
while True:
    distancia = sensor_ir.distance()

    if distancia <= 15:
        # Avanza 1 segundo
        robot.drive(VELOCIDAD, 0)
        wait(1000)
        robot.stop()

        # Cierra el brazo
        cerrar_brazo()

        # Espera breve antes de seguir línea
        wait(500)

    # Seguimiento de línea
    valor_izquierdo = sensor_izquierdo.reflection()
    valor_derecho = sensor_derecho.reflection()
    error = valor_izquierdo - valor_derecho
    velocidad_giro = GANANCIA_PROPORCIONAL * error
    robot.drive(VELOCIDAD, velocidad_giro)
    wait(10)

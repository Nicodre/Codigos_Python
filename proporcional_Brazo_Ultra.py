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
sensor_ir2 = InfraredSensor(Port.S4)

# Base del robot
robot = DriveBase(motor_izquierdo, motor_derecho, wheel_diameter=55.5, axle_track=292)

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

def abrir_brazo():
    brazo.run_angle(500,90)
    brazo.stop()
# Bucle principal
while True:
    distancia = sensor_ir.distance()
    distancia2 = sensor_ir2.distance()
    
    if distancia <= 15:
        # Avanza 1 segundo
        robot.drive(VELOCIDAD, 0)
        wait(1000)
        robot.stop()

        # Cierra el brazo
        cerrar_brazo()

        # Espera breve antes de seguir línea
        wait(500)

    if 20 <= distancialateral <=30 
        robot.turn(-90) # Girar lentamente a la izquierda.

        # Abrir el brazo
        abrir_brazo()

        # Lanzar pelota va haci adelante para empujar la pelota y regresa
        robot.drive(500, 0)
        wait(50)
        robot.drive(-500, 0)
        robot.turn(90) # Gira a la derecha y continua siguiendo linea.

        else if distancialateral <= 15
            robot.drive(VELOCIDAD, 0) # Sigue para descartar pelota.
            wait(2000)

             abrir_brazo()

        # Lanzar pelota va haci adelante para empujar la pelota y regresa
            robot.drive(500, 0)
            wait(50)
            robot.drive(-500, 0)
            robot.turn(90) 
            
        
    # Seguimiento de línea
    valor_izquierdo = sensor_izquierdo.reflection()
    valor_derecho = sensor_derecho.reflection()
    error = valor_izquierdo - valor_derecho
    velocidad_giro = GANANCIA_PROPORCIONAL * error
    robot.drive(VELOCIDAD, velocidad_giro)
    wait(10)

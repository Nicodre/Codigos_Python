# Movimiento
rom pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
En este caso left_motor  y  right_motor son el nombre de las variables(podemos elegir otros) y Motor(Port.B) define el tipo de variable, Motor, 
y la asigna a un puerto, acá solo podemos cambiar los puertos. 

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
acá hay que medir el robot para tener le diámetro de las ruedas y la longitud del eje. 

# Go forward and backwards for one meter.
robot.straight(1000)
ev3.speaker.beep()

robot.straight(-1000)
ev3.speaker.beep()

# Turn clockwise by 360 degrees and back again.
robot.turn(360)
ev3.speaker.beep()

robot.turn(-360)
ev3.speaker.beep()

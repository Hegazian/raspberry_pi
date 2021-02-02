# Write your code here :-)
from bluedot import BlueDot
from gpiozero import Robot

bd = BlueDot()
robot = Robot(right=(17, 27), left=(22, 23)) ##this may be different depending on your wiring

def move(pos):
    if pos.top:
        robot.forward()
        #print("forward")
    elif pos.bottom:
        robot.backward()
        #print("backward")
    elif pos.right:
        robot.right()
        #print("right")
    elif pos.left:
        robot.left()
        #print("left")

def stop():
    robot.stop()

bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop
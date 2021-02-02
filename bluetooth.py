from bluedot import BlueDot
bd = BlueDot()
bd.wait_for_press()
print("You pressed the blue dot!")
def foo(pos):
    print(pos.x)
    print(pos.y)
bd.when_pressed = foo ##run the function foo when the blue dot is pressed
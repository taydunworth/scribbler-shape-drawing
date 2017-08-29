#Taylor Cox and Elizabeth Ingermann

from Myro import *
init ("/dev/tty.IPRE6-365764-DevB")

draw_shape=ask("What shape would you like drawn?")
if draw_shape == "triangle":
    speak("Please insert the marker.")   #Triangle
    wait(2)
    speak("I will draw a triangle.")
    forward(.5,.5)
    turnBy(45)
    backward(.5,.8)
    turnBy(45)
    forward(.5,.6)
    speak("Please remove the marker.")
    wait(2)
elif draw_shape == "TRIANGLE":
    speak("Please insert the marker.")   #Triangle
    wait(2)
    speak("I will draw a triangle.")
    forward(.5,.5)
    turnBy(45)
    backward(.5,.8)
    turnBy(45)
    forward(.5,.6)
    speak("Please remove the marker.")
    wait(2)
elif draw_shape == "CIRCLE":
    speak("Please insert the marker.")   #Circle
    wait(2)
    speak("I will draw a circle.")
    motors(1,0,5)
    speak("Please remove the marker.")
elif draw_shape == "circle":
    speak("Please insert the marker.")   #Circle
    wait(2)
    speak("I will draw a circle.")
    motors(1,0,5)
    speak("Please remove the marker.")
elif draw_shape == "square":
    speak("Please insert the marker.")   #Square
    wait(2)
    speak("I will draw a square.")
    forward(.5,1)
    turnBy(90)
    forward(.5,1)
    turnBy(90)
    forward(.5,1)
    turnBy(90)
    forward(.5,1)
    speak("Please remove the marker.")
elif draw_shape == "SQUARE":
    speak("Please insert the marker.")   #Square
    wait(2)
    speak("I will draw a square.")
    forward(.5,1)
    turnBy(90)
    forward(.5,1)
    turnBy(90)
    forward(.5,1)
    turnBy(90)
    forward(.5,1)
    speak("Please remove the marker.")
else:
    print("I did not understand your input.")



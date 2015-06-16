import simpleguitk as simplegui ###### !!!!! probably only works at http://www.codeskulptor.org/

# here is the event handler, namely two functions that manage click events depending on the state of variable 'x'

x = True

def switch():
    global x
    x = False

def click_dlg():
    global x
    if x == True:
        print "Yep, you clicked my button."
        switch()
    else:
        print "Hey, you clicked again!"

# here are the program elements; namely a frame with buttons

frame = simplegui.create_frame("You asked for a frame...", 300, 300)

frame.set_canvas_background('Cyan')

frame.add_button("WHAT DOES THIS DO?", click_dlg)


# this starts it all

frame.start()

"""
It is a little tricky using functions and local modifications to global
variables, but I think the main thing that was holding me back here was
using assignment '=' instead of test '==' in my conditional. Python kept
trying to tell me I was declaring variables multiple times, or then 
upon repair referring to undeclared variables. Back when using a counter.
"""

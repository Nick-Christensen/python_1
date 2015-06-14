"""
'Guess The Number' game, from Coursera, Python I. Mini-Project #2.
Started 13 June 2015 by Nick Christensen

Still to add: buttons to change the guessing range
			; limit the number of guesses

"""
import random
import simplegui # NOTE! only works at http://www.codeskulptor.org/


# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(1, 100)
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "Alright, sweet! Let's play Guess The Number!"
    print ""
    return secret_number


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    try:
        guess_int = int(guess)
        print "Your guess, %s, is..." % guess
        if guess_int < secret_number:
            print "...too LOW. Try again!"
            print ""
        elif guess_int > secret_number:
            print "...too HIGH. Try again!"
            print ""
        else:
            print "...exactly right! Wow, congrats."
            print ""
            #new_game() #uncomment this to auto-restart a validly completed game
    except ValueError:
        print "Sorry, try again with a valid guess."
        print ""
    
# create frame
gtn_frame = simplegui.create_frame("Guess The Number!", 300, 200)

# register event handlers for control elements and start frame
gtn_frame.add_input("Enter your guess: ", input_guess, 200)

gtn_frame.start()

# call new_game 
new_game()



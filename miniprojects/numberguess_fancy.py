"""
'Guess The Number' game, from Coursera, Python I. Mini-Project #2.
Started 13 June 2015 by Nick Christensen

Still to add: buttons to change the guessing range --CHECK, 14 June. 
            ; limit the number of guesses --CHECK (I think), 14 June
            ; it is still possible to guess high out of range (oh well: throw away your guesses if you want to, jerk :)

"""
import random
import simplegui # NOTE! only works at http://www.codeskulptor.org/

x = False # for the button below that activates guess-counting (7 or fewer!)

def new_game():
    global secret_number
    secret_number = random.randrange(1, 100)
    return secret_number

def seven_guess():
    global x
    x = True #flips switch on global to activate guess-counting in input_guess()
    global counter
    counter = 0 # guess counter, incremented below also in input_guess()
    print "Ooh, a lover of danger!"
    print ""
    return x

# define event handlers for control panel
def range100():
    print "Back to the classic game; the Secret Number is once again between 1 and 100."
    print ""    
    new_game()

def range1000():
    print "High-stakes game, here; my Secret Number is now between 1 and 1,000!"
    print ""
    global secret_number
    secret_number = random.randrange(1, 1000)
    return secret_number
    
def input_guess(guess):
    if x == False:
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
    else: # i.e., when x = True
        global counter
        if counter < 7:
            try:
                guess_int = int(guess)
                print "Your guess, %s, is..." % guess
                if guess_int < secret_number:
                    print "...too LOW. Try again!"
                    print ""
                    counter = counter + 1
                elif guess_int > secret_number:
                    print "...too HIGH. Try again!"
                    print ""
                    counter = counter + 1
                else:
                    print "...exactly right! Wow, congrats."
                    print ""
            except ValueError:
                print "Sorry, try again with a valid guess."
                print ""
        else: #---> if counter < 7
            print "Wah-waaah, you're out of guesses!"	                
            

# create frame
gtn_frame = simplegui.create_frame("Guess The Number!", 300, 200)

# register event handlers for control elements and start frame
gtn_frame.add_input("Enter your guess: ", input_guess, 200)

gtn_frame.add_button("Play to guess between 1 - 1000!", range1000, 200)
gtn_frame.add_button("Resume original play", range100, 200)
gtn_frame.add_button("Limit my guesses!", seven_guess, 200)

gtn_frame.start()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "Alright, sweet! Let's play Guess The Number!"
print "I'm thinking of a whole number bigger than zero but less than one hundred."
print ""

# call new_game 
new_game()



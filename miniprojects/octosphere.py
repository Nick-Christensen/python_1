# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:34:20 2015

@author: nickchristensenpro 
"""

import random

### instead of if/elif, I put the responses in a dictionary:

response_dict = {0 : 'Yes, for sure!'
, 1 : 'Probably yes.'
, 2 : 'Seems like yes...'
, 3 : 'Definitely not!'
, 4 : 'Probably not.'
, 5 : 'I really doubt it...'
, 6 : 'Not sure, check back later!'
, 7 : 'I really can\'t tell'
}

def fortune_num(): #produces a random int value between 0 - 7, inclusive
    rt = random.randint(0, 7)
    return rt

def number_to_fortune(rt): #translates the random value (passed in main function, below)
    ntf = response_dict[rt]
    return ntf

def mystical_octosphere(summons): #main function invoked by a question

    question = summons
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "You've summoned the * * * MYSTICAL OCTOSPHERE* * * to ask...\n\n...%s" % question    
    print""

    print "You shake the mystical octosphere..."    
    print "...the liquid swirls and a reply comes into view..."
    print ""
    print ""
    answer_number = fortune_num()
    ans_final = number_to_fortune(answer_number)
    return ans_final

x = mystical_octosphere("Will I get rich?")

### alternate questions for the octosphere
#x = mystical_octosphere("Are the Cubs going to win the World Series?")

print x

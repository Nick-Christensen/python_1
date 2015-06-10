from __future__ import division
import math

a = 2
b = 0
c = -10

discrim = (b**2) - (4*a*c)
plus = (-b + (discrim)**0.5) / (2*a)
minus = (-b - (discrim)**0.5) / (2*a)

print "discrim:"
print discrim #

print math.sqrt(discrim) # sqrt of 80
print (math.sqrt(discrim)) / (2*a) # I expect 8.9 / 4 = 2.225 ???
print plus, minus
print min(plus, minus)

a2 = 2*a
print a2

"""
I had trouble getting (discrim)**0.5 to execute in the functions below,
found success finally in math.sqrt()

# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.
import math

def smaller_root(a,b,c):
    discrim = (b**2) - (4*a*c)
    err_msg = "Error: No real solutions"
    plus = (-b + math.sqrt(discrim)) / (2*a)
    minus = (-b - math.sqrt(discrim)) / (2*a)
    if discrim < 0:
        return err_msg
    else:
        return min(plus, minus)


###################################################
# Tests
# Student should not change this code.

def test(a, b, c):
    #Tests the smaller_root function.
    
    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:" 
    print str(smaller_root(a, b, c))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None

"""

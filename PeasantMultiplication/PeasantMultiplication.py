##############################################################################################
#  Author: Collin Mitchell
#    Date: 6 April 2013
# Version: 1.0f
#    Data: Program tests the user on "Peasant Mulitplication." This works like this:
#          20 x 15
#          0 * 5 = 0               // Multiply ones digits
#          0 * 1 + 5 * 2 = 11      // Cross multiply + add result; carry if two digits exist
#          2 * 1 = 2               // Multiply tens digits
#          Answer: 20 * 15 = 310   // Final result
# History: 
#         [April 6th 2013]
#         Initial program created
##############################################################################################
import time as t
import random as r
import sys

###########################################################
# Generate a question and ask the user for their answer
###########################################################
def question(correct):
   num1 = r.randint(10,99)
   num2 = r.randint(10,99)
   solution = num1 * num2

   print ' ' + str(num1)
   print 'x' + str(num2)

   timeBegin = t.time()
   testsolution = raw_input('Solution?: ')
   timeEnd = t.time()
   if testsolution == str(solution):
      correct +=1
   times.append(timeEnd - timeBegin)

   return correct

###########################################################
# Generate results for the user
###########################################################
def results(correct, averageTime):
   for item in times:
      averageTime += item
   averageTime /= total

   print 'Accuracy    : %.2f' % correct/total
   print 'Average Time: %.2f' % averageTime

###########################################################
# Set up data
###########################################################
correct     = 0
total       = 0
averageTime = 0
times = []
if len(sys.argv) > 1:
   total = int(sys.argv[1])
else:
   total = 10

###########################################################
# Run.
###########################################################
while len(times) != total:
   correct = question(correct)
results(correct, averageTime)

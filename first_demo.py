#!/usr/bin/python
#Filename : first_demo.py

# ME2984 Assign #2 Part #3
# Initial Code Written by:Jason Ziglar <jpz@vt.edu>
# Extended and Modified by: Brandon Caleb Scott <bcs2820@vt.edu>

## Define a function which computes the harmonic series
def harmonic_series(Num_Term):
  '''This function computes a certain number of terms from the harmonic series.
  Num_Term: the certain number of terms to add together. If this value is negative it's converted into a zero.
  returns: The value that is computed'''
  # Creates a variable to store result, set to some initial value
  Value = 0
  # Produces a sequence of numbers: [0, Num_Term] and executes the loop with ii set to each value
  for ii in range(Num_Term):
    # Resets Value to Value plus the next term
    # Note: Computers start counting at 0, so we have to add 1 to be safe
    Value = Value + (1.0 / (ii + 1))
  # Returns the Value to whom it may concern
  return Value

## Define a function which computes the harmonic series using a while loop
def harmonic_series_while(Num_Term):
  '''This function computes a certain number of terms from the harmonic series with a while loop.
  Num_Term: the certain number of terms to add together. If this value is negative it's converted into a zero.
  returns: The sum of the first n terms of the series'''
  # Creates a variable to store result, set to some initial value
  Value = 0
  # Counts to keep track of how many terms have been computed
  Counter = 0
  # This will run until "counter <= num_terms" returns a false statement
  while Counter < Num_Term:
    Value = Value + (1.0 / (Counter + 1))
    # Very important - while runs until it sees false, so we have to make sure
    # the test will eventually fail
    Counter = Counter + 1
  # Return value
  return Value

## Print a welcome
print "Welcome to a Simple Harmonic Series Approximation Program."
# Asks the user to select a method and number of iterations repeated
Run = raw_input("Would you like to continue (Yes or No): ")
while Run == "Yes" or Run == "yes":
  #Ask the user to select a function
  request = raw_input("Select which function to use (For or While) loop: ")
  if request == "For" or request == "for":
    # Same as before, but in a single line.
    iterations = float(raw_input("How many terms should I use? "))
    # Protects against the input being negative
    if iterations <= 0:
      print "The iteration prefered was less than or equal to zero"
      interations = 0
    # Converts and Verifies that iterations was rounded properly
    print "The Original Value: %s" % iterations
    iterations=int(round(iterations))
    print "The New Rounded Value: %s" % iterations
    ## The Pi Estimator
    # Produces a sequence of numbers: [0, Num_Term] and executes the   loop with ii set to each value
    Sum = 0
    for Num in range(iterations):
      # Resets Value to Value plus the next term
      # Note: Computers start counting at 0, so we have to add 1 to be safe
      Num = Num + 1
      Sum = Sum + (1.0 / (Num**2))
    Total = (Sum*6) ** (0.5)
    # Returns the Value to whom it may concern
    print "The estimated value for pi: %s" % Total
    ## Test Input
    # Get value form function
    result = harmonic_series(iterations)
    # Print using a technique known as string interpolation. %s means "take the next value after the string and insert as a string"
    # So it will look at the list of values after the % and grab the next (only) one
    # For more details, look here: https://docs.python.org/2/library/stdtypes.html#string-formatting
    print "For loop produces: %s" % result
  elif request == "While" or request == "while":
    # Same as previous statement, but notice you don't have to store a value in a variable before using it, if it makes sense.
    iterations = float(raw_input("How many terms should I use? "))
    # Protects against the input being negative
    if iterations <= 0:
      print "The iteration prefered was less than or equal to zero"
      interations = 0
    # Converts and Verifies that iterations was rounded properly
    print "The Original Value: %s" % iterations
    iterations=int(round(iterations))
    print "The New Rounded Value: %s" % iterations
    ## The Pi Estimator
    # Produces a sequence of numbers: [0, Num_Term] and executes the   loop with ii set to each value
    Sum = 0
    for Num in range(iterations):
      # Resets Value to Value plus the next term
      # Note: Computers start counting at 0, so we have to add 1 to be safe
      Num = Num + 1
      Sum = Sum + (1.0 / (Num**2))
    Total = (Sum*6) ** (0.5)
    # Returns the Value to whom it may concern
    print "The estimated value for pi: %s" % Total
    print "While loop produces %s" % harmonic_series_while(iterations)
  else:
    # Commentary courtesy of B9 Robot
    print "DANGER WILL ROBINSON DANGER! DOES NOT COMPUTE! DOES NOT COMPUTE!"
  Run = raw_input("Would you like to continue (Yes or No): ")
if Run == 'No' or Run == "no":
  print "Thank you and have a great day. End of Program."
else:
  print "Error..."

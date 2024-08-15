year = int(input("What year were you born? "))

if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994: # if only ">" is used, the program will not print "You are a Gen Z." for the year 1994
    print("You are a Gen Z.")
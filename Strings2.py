name = 'Sam'
print(name)
lastLetters = name[1:]
name = 'P' + lastLetters
print(name)

x = 'Hello World'
print(x + "it is beautiful outside!")   #Gives you no space when concatenating these two strings together
#Hello Worldit is beautiful outside!

print("-" * 10) #Can also multiply a string to print it multiple times, here it prints out "-" 10 times, can be useful for formatting outputs in the terminal
#----------

print(x.upper())    #Capitalize all letters in a string uppercase
#HELLO WORLD

print(x.lower())    #Make all letters in a string lowercasee
#hello world

print(x.split())    #Splits a string into a list, delimited by a given character, whitespace is chosen by default if nothing is given
#['Hello', 'World']

stringString = "Hi this is a string"
print(stringString.split("i"))      #Now that a character was given to delimit the string into a list with, rather than white space it breaks the string up at each "i" in the string and removes it rather than leaving
                                    #it there and the whitespace remains
#['H', ' th', 's ', 's a str', 'ng']
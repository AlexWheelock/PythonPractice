string1 = 'hello' #Single quotes can be used
string2 = "world" #double quotes can also be used
string3 = "I'm going on a run" #Since the single quote (apostrophe) in "I'm" can be used to signify a string, a double quote is necessary to not throw an error.

print(string1)
print(string2)
print(string3)

print("hello\nworld")       #\n is an escape character meaning "new line" or "carriage return" into the string
print("hello\tworld")       #\t is an escape character for inserting a tab into the string
print(len("hello world"))   #len() returns the length of the string

myString = "Hello World"
print(myString[0])          #Using the square brackets returns the character with the index of the number within the square brackets
print(myString[-1])         #Can also be used for reverse indexing from the end (last character being -1)

secondString = 'abcdefghijk'
print(secondString[2:])     #Slicing strings: [starting index:stopping index:step]
#will print out from index 2 to the end of the string since no stopping index is given
#cdefghijk

print(secondString[:3])     #Note: the stopping index is non-inclusive, and goes up to the index but does not include it
#abc

print(secondString[3:6])
#def

print(secondString[::2])    #starting from index 0 until the end of the string, will slice every other index since the step is set to 2
#acegik

print(secondString[::-1])   #will flip the string since it prints out the entire length of secondString backwards since the step is negative
#kjihgfedcba
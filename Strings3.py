print('This is a string {}'.format('INSERTED'))     #Inserting curly braces into a string acts as a way for something such as a variable to be inserted into a string using the .format() method
#This is a stringINSERTED

print("The {} {} {}".format("fox", "brown", "quick"))   #The reason you might use the .format() method is because it is indexed
#The fox brown quick

print("The {2} {1} {0}".format("fox", "brown", "quick"))    #Inserting the index allows us to change the output only by adjusting the index that we give each curly brace
#The quick brown fox


result = 100/777
print(result)
#0.1287001287001287

print("The result was: {r:10.5f}".format(r = result))   #float formatting "{value:width.precisionf}" allows us to format the output
#The result was:    0.12870                             #Since the output is a floating point number that is long, we can format the output of r to take 10 characters (padding) and 5f for 5 digits past the decimal point

print("The result was: {r:1.5f}".format(r = result)) 
#The result was: 0.12870


name = "Jose"
print(f'Hello, my name is {name}')      #String literal is done by adding "f" prior to the string, and allows us to add a variable a bit simpler, making it recognize the curly brackets as something
#Hello, my name is Jose                 #that we are passing into the string and does not require us to use the .format() method and works more similarly to how we would do it in Visual Basic.

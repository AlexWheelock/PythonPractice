myList = [1,2,3]        #List is declared by using the square brackets "[]"
myList = ['string', 100, 123.4]     #A list can also be made up of several differt object types

print(myList)
#['string', 100, 123.4]

len(myList)
#3

firstList = ['one', 'two', 'three']
secondList = ['four', 'five']

newList = firstList + secondList
print(newList)   #You can also concatenate lists
#['one', 'two', 'three', 'four', 'five']

firstList[0] = "ONE ALL CAPS"
print(firstList)    #Lists are mutable, meaning that you are able to modify lists
#['ONE ALL CAPS', 'two', 'three']

newList.append('six')   #You can also add additional data into lists using the .append() method
print(newList)
#['one', 'two', 'three', 'four', 'five', 'six']

poppedItem = newList.pop()  #It is also possible to delete data from lists using the .pop() method, and it will take the last item out by default
print(poppedItem)
#six
print(newList)
#['one', 'two', 'three', 'four', 'five']


stringList = ['a', 'x', 'z', 'b', 'y', 'c']
numList = [4, 1, 3, 2]

print(stringList)
print(numList)
#['a', 'x', 'z', 'b', 'y', 'c']
#[4, 1, 3, 2]

stringList.sort()   #You can sort a list alphabetically using the .sort() method and occurs in place rather than needing you to assign it to another variable
print(stringList)   #Actually will not work if you try to assign it to another variable
#['a', 'b', 'c', 'x', 'y', 'z']

numList.sort()      #This also works numerically
print(numList)
#[1, 2, 3, 4]

print(numList[1:])  #You can slice lists as you would a string
#[2, 3, 4]

numList.reverse()   #You can also reverse the order of the list using the .reverse method
print(numList)
#[4, 3, 2, 1]

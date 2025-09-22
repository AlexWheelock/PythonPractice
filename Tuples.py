#similar to lists however are immutable; use parentheses ()

t = (1,2,3)
myList = [1,2,3]

print(type(t))
#<class 'tuple'>

print(type(myList))
#<class 'list'>

print(len(t))
#3

print(t[0])     #Can call indexs as you would a list
#1

print(t[-1])    #Can also call index from the end using negative index
#3

#NOTE: tuples only have these two methods that you can use, while lists have a much wider range of options for methods for you to use

t = ('a', 'a', 'b')

print(t.count('a'))     #.count() method returns the number of times that a certain value appears within the tuple
#2

print(t.index('a'))     #.index() method returns the index location that the given value appears at
#0                      #NOTE: If a value appears multiple times within a tuple, it will return only the index at which it appears first


myList[0] = 'NEW'       #lists allow us to modify/re-assign objects within them
print(myList)
#['NEW', 2, 3]

#t[0] = 'NEW'            #tuple does not allow for re-assignment of objects within it; throws an error
#print(t)
#Traceback (most recent call last):
#  File "c:\Users\frame\Documents\repos\PythonPractice\Tuples.py", line 34, in <module>
#    t[0] = 'NEW'
#    ~^^^
#TypeError: 'tuple' object does not support item assignment


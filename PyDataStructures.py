"""
Data structures
"""


"""
Arrays
"""

anArray = ["car","boat",3,True,2.3]
anArray[0] = "car2"
#print(anArray)

"""
for x in anArray:
    if( type(x) == int):
         print(x)
"""

#Constructor
newArray = list(("car","toy",2,2.3))
#if "car" in newArray:
#    print("yes there is a car object ")

newArray.append("appended object")
newArray.insert(1,"airplane")
#print(newArray)

secondList = ["orange","green"]
newArray.extend(secondList)
#print(newArray)

newArray.remove("car")
newArray.pop(2)
newArray.pop()
#newArray.clear()
#print(newArray)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
#print(newlist)

newlist = [x for x in range(2)]
#print(len(newlist))

"""
Tuples
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.
"""

firstTuple = ("first",2,"third",True)

#Constructor
aTuple = tuple(("apple",))
#print(aTuple)
listFromTuple = list(firstTuple)
listFromTuple[1] = 5
#print(listFromTuple)

#Unpack a tuple
(first,second,*third) = firstTuple
#print(first, second, third)
count = firstTuple.count("third")
#print(count)

"""
Sets

A set is a collection which is unordered, unchangeable*, and unindexed.
"""

mySet = {"toyota", "Suzuki", "Opel", 5, 5.6, True}
print(mySet)

# Constructor

newSet = set(("one",False, 3))
print(type(newSet))
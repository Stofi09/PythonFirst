"""
Variables
"""

integerVar = 6
boolVar = True
strVar = "String"
floatVar = 2.3

var1,var2,var3 = "string1",2,False
#print(var1)
#print(var2)
#print(var3)

#print(integerVar + var2)
#print(var1 + var2) => TypeError: can only concatenate str (not "int") to str
#print(var1 , var2) => No error 

"""
Global
"""

globalVar = 5

def myFunc():
    print(globalVar)

def myFuncLocal(): 
    globalVar = 10
    print(globalVar)

def myFuncGlobal(): 
   global x
   x = 10

#myFuncGlobal()
#print(x)
x  = 20
def myFuncGlobalChange(): 
   global x
   x = 10

#myFuncGlobalChange()
#print(x)

"""
Casting
"""

int1 = int(2.3)
int2 = int("3")
# int3 = int("char") => ValueError: invalid literal for int() with base 10
#int4 = int(False) => True == 1, False == 0
#print (int1 , int2)

float1 = float(3)
float2 = float("2.3")
#print(float1, float2)

str1 = str(1)
str2 = str(2.8)
str3 = str(True)
#print(str1, str2, str3)

"""
String
"""

strVar1 = "String as array"
#print(len(strVar1))
#print(strVar1[3])
#for x in strVar1:
#    print(x)
#print ("as" in strVar1)
#print("blob" not in strVar1)

strSlice= "123456789"
#print(strSlice[:2])
#print(strSlice[1:4])
#print(strSlice[1:7:2])
#print(strSlice[2:])

strUpper = "to upper case"
strLower = "to lower case"
strStrip = " to strip "
strReplace = " to replace c"
strSplit = "Split it , here"
#print(strUpper.upper(), strLower.lower(), strStrip.strip(), strReplace.replace("c", "j"))
#print(strSplit.split(","))

text = "Today is {} "
day = "Wednesday"
print(text.format(day))
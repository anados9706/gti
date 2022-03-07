#def reverseString(rString):
#    arr = list(rString)
#    print("Before:", rString)
#    arr.reverse()
#    print("After:", arr)

#reverseString("Hello World")

def reverseString_fun(rString_list):
    length = len(rString_list)
    s = length

    reversed_list=[None]*length

    for item in rString_list:
     s = s-1
     reversed_list[s]=item
    return reversed_list

list1 = "Hello World" 

def listToString(s):
	reverseString_fun = ""
	for ele in s:
		reverseString_fun += ele
	return reverseString_fun
s = "Hello World"
print(listToString(s))

print(reverseString_fun(list1))    
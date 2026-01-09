def functionSample():
    resultK = 10*2
    print("The sample function is working")

def returnExample():
    result = 10*100
    return result


functionSample()
# output = returnExample()
# print("The returned value is:",output)  
print(returnExample())

def inputSample():
    userInput= input("Enter a name:")
    print(userInput)
inputSample()

def inputSample(a,b):
    result = a*b
    return result

a = input("input first number:")
b = input("input second number:")

print(inputSample(int(a), int(b)))


def operationType(num1, num2, op):
    if(op == "a"):
        return num1+num2
    elif(op == "s"):
        if(num1<num2):
            print("given input is invalid! pls give valid input")
        else:
            return num1-num2    
    elif(op == "m"):
        return num1*num2
    elif(op == "d"):
        return num1/num2  
    else:
        print("invalid operation please enter valid one")

          

def printResult(inp):
    if(inp%2 ==0):
        print("The output number is even")
    else:
        print("The output is odd number")        

op = input("please Enter the operation to perform a: Add, s: sub, m: multiplication,d: Division")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
result = operationType(num1, num2, op)
printResult(result)  
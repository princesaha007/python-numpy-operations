# first code 1 /////////////////////////////////////////////////
x = 20
y = 10
def sum(x, y):
    return x + y

result = sum(x, y)
print("The sum of these two numbers is " + str(result))


# another way and passing param in the print
def sum2(x, y):
    return x + y
result = sum(x, y)
print(sum2(2,3))




# first code 2 //////////////////////////////////////////////////
name= "prince"
print('my name is ' + name)


# first code 3 ///////////////////////////////////////////////////
def isEven(num):
    if num%2==0:
        return True
    else:
        return False

print(isEven(6))

# first code 4 ///////////////////////////////////////////////////
def isPrime(num):
    if num<2:
        return False
    else:
        for i in range(2,num):
            if num%i==0:
                return True
            else:
                return False

print(isPrime(7))


# first code 5 ///////////////////////////////////////////////////

def largeestNumber(num1, num2):
    if num1>num2:
        return "largest number " + str(num1)
    else:
        return "largest number " + str(num2)

print(largeestNumber(5,9 ))


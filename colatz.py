def colatz(number):
    
    if number %2 == 0:
        print(number // 2)
        return number // 2
    elif number %2 == 1:
        result = 3 * number + 1
        print(result)
        return result
n = input("Give me a number: ")
while n != 1:
    n = colatz(int(n))
    
def isstr(n):
    try:
        colatz(str(n))
    except ValueError:
        print('Please type integer value')
       
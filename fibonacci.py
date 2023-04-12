fiboList = [0,1]
def fibonacci(n):
    if n<0:
        print("incorrect number")
        
    elif n<len(fiboList):
        return fiboList[n]
    else:
        fiboList.append(fibonacci(n-1)+fibonacci(n-2))
        return fiboList[n]
    
num = 9
result = fibonacci(num)
print(fiboList)
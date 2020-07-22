#Wilson Wu

#Write a function that calculates the nth Fibonacci number in O(n) time or better without using any "for" or "while" loops. 

#Implemented using dynamic programming and recursion methods.

fiboList = [0,1]        #Hard Code initial base cases

def fibonacci(n):

    #Base Case
    if n == 0:
        return 0
    
    #Base Case
    elif n == 1:
        return 1

    #Case other than f(0) or f(1)
    else:
        #Check if f(n-1) has already been calculated
        if(len(fiboList)-1 == n-1):
            second = fiboList[n-1]
        #Caluclate f(n-1) and save it to fiboList array
        else:
            second = fibonacci(n-1)
            fiboList.append(second)

        #Check if f(n-2) has already been calculated
        if(len(fiboList)-1 == n-2):
            first = fiboList[n-2]
        #Caluclate f(n-2) and save it to fiboList array
        else:
            first = fibonacci(n-2)
            fiboList.append(second)

        #Add totals and return
        total = first + second
        return total

def main():
    userInput = int(input("Please enter an interger N to caluculate the Nth Fibonacci Number:"))
    
    print(fibonacci(userInput))
        

main()





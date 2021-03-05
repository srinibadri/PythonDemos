import time

# Fibonacci Sequence function
def fibo_iterative(n):

   # initial values
   if (n==0):
       return 0
   elif (n==1):
       return 1
   else:
       # iteration loop
       a = 0
       b = 1
       result = 1
       i = 2
       while (i <= n):
           result = a + b
           a = b
           b = result
           i += 1
       return result


# Fibonacci Sequence function
def fibo_recursive(n):
    # To be implemented
    return

def main():
    # call fib method from fibo module, and store the results in seq
    n = int(input("Enter an integer for fibonacci number: "))
    start = time.time()
    result = fibo_iterative(n)
    end = time.time()
    print(result)
    print("exection time: {:4e}".format(end-start))

if __name__ == "__main__":
    main()

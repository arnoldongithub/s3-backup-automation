#python program to find Fibonacci number using recursion

#function to find nth fibonacci number

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Driver code
if __name__ == "__main__":
    n = 5
    print(fib(n))

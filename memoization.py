#python program to find fibonacci number using memoization

def fibRec(n, memo):

    #Base case
    if n <= 1:
        return n
    
    #to check if output already exists
    if memo[n] !=-1:
        return memo [n]
    
    #calculate and save output for future use
    memo [n] = fibRec(n-1, memo) + \
               fibRec(n-2, memo)
    return memo[n]

def fib(n):
    memo=[-1]*(n+1)
    return fibRec(n,memo)

n = 5
print(fib(n))

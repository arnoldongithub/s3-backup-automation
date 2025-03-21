#python program to express
#n as sum of 1,3,5

def countRecur(n,memo):
    #base case
    if n<0:
        return 0
    if n==0:
        return 1
    #memoize the state
    if memo[n]!=-1:
        return memo [n]
    
    #memoize the state
    memo[n]= countRecur(n-1, memo)+ \
       countRecur(n-3,memo)+\
       countRecur(n-5,memo)
    
    return memo[n]

#returns the number of
#arrangements to form 'n'
def countWays(n):
    memo= [-1]*(n+1)
    return countRecur(n,memo)

if __name__=='__main__':
    n=7
    print(countWays(n))
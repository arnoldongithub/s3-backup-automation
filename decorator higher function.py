def hello_decorator(func):
    #inner1 is a wrapper function in which the argument is called
    #inner function can access the outer local finctions
    #in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        #calling the actual function now
        #inside the wrapper function
        func()

        print("this is after function execution")
    return inner1
#defining 'function_to_be_used' inside the 
#decorator to control its behaviour
function_to_be_used=hello_decorator("inner1")

#calling the function
function_to_be_used()
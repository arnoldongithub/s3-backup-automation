def shout(text):
    return text.upper()  # Call the upper method to return the transformed string

print(shout('Hello'))  # Should output 'HELLO'

# Assigning function to a variable
yell = shout
print(yell('Hello'))  # Should also output 'HELLO'


#new higher order function
def shout (text):
    return text.upper()

def whisper (text):
    return text.lower()

def greet(func):
    #storing the function in a variable
    greeting=func("HELLO, I AM CREATED BY ARNOLD. THE ARNOLD\
                  passed as an argument")
    print(greeting)


greet(shout)
greet(whisper)

#another function to save on tab space
def create_adder(x):
    def adder(y):
        return x+y
    
    return adder
add_15=create_adder(15)

print(add_15((10)))


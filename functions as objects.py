def shout(text):
    return text.upper()

print(shout('Hello'))

#assigning function to a variable
yell=shout
print(f"hello I always {yell('Hello')}" )
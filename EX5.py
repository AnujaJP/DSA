###Ask user for two numbers (as strings), convert them to integers, then print:
##their sumtheir differencetheir productwhich one is bigger (or if they are equal)
num1=input("enter a number:")
num2=input("enter a number:")
num1_converted=int(num1)
num2_converted=int(num2)
add = num1_converted + num2_converted
sub = num1_converted - num2_converted
mul = num1_converted * num2_converted
print("Sum:", add)
print("Difference:", sub)
print("Product:", mul)
if num1_converted > num2_converted:
    print("First number is bigger")
elif num2_converted > num1_converted:
    print("Second number is bigger")
else:
    print("Both numbers are equal")
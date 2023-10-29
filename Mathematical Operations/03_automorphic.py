# One-liner Python program to check automorphic number:

# The following line of code checks and prints whether the entered number is Automorphic or not. 
print("Automorphic Number\n" if (len(list((x for x in [int(input("\nEnter a number: "))] if str(x*x).endswith(str(x)))))==1) else "Not Automorphic Number\n" )

# One-liner Python program to tell whether entered numbemr is Automorphic or not.

print("Automorphic Number" if (len(list((x for x in [int(input("Enter a number: "))] if str(x*x).endswith(str(x)))))==1) else "Not Automorphic Number" )
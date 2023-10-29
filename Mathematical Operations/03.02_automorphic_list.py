# One-liner Python program to print a list of Automorphic numbers.

# The following line of prints automorphic numbers in a given range. (Upper limit of the range is to be entered by the user during run-time)
print("\nList of Automorphic numbers in the given list are: ",list(x for x in range(1, int(input("\nEnter upper limit of the range (1,?) : "))) if str(x*x).endswith(str(x))),'\n', sep='\n')
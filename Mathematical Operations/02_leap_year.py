# The following one-liner Python Program takes input a range of years and returns all the learp years from that range

print("List of all the Leap Years in between:",list(i for i in range(int(input("From which year (yyyy): ")), int(input("Till which year (yyyy): "))) if (i % 4 == 0 and i % 100 != 0)  or i % 400 == 0), sep="\n")
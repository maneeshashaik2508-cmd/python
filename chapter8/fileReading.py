# with keyword

# with open("chapter8\ report.txt","r") as f:               # AUTOMATICALLY CLOSES THE FILE
#     data = f.read()
#     print(data)

with open("report.txt","r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    line5 = f.readline()
    line6 = f.readline()
    data=f.read()
    print("line 1 :-",line1)
    print("line 2 :-",line2)
    print("line 3 :-",line3)
    print("line 4 :-",line4)
    print("line 5 :-",line5)
    print("line 6 :-",line6)
    print("data is",data)

# Read all lines

with open("report.txt","r") as f:
 readLinesMethod = f.readlines()
 print(readLinesMethod)

# Read only the first line of bio.txt.

with open("bio.txt","r") as f:
   line1 = f.readline()
   print("line 1 :-",line1)
   
# Print how many lines are present in notes.txt.

import os 


with open("notes.txt","r") as f:
   listOflines= f.readlines()
   print(listOflines)
   print("NUmber of lines in file :-", len(listOflines))


# os.rename("bio.txt","new_bio.txt")
# os.remove("new_bio.txt")


try:
   with open("notes1.txt","r") as f:
        listOflines= f.readlines()
        print(listOflines)
        print("NUmber of lines in file :-", len(listOflines))
except:
   print("That file does not exist.")


try:
   with open("notes.txt","r") as f:
        listOflines= f.readlines()
        print(listOflines)
        print("NUmber of lines in file :-", len(listOflines))
except:
   print("That file does not exist.")


   



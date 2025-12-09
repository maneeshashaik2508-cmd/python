# FILE HANDLING

file = open("chapter8\mast", "r")         # default mode is read(r) ## path is defferent here so have taken chapter8\
data = file.read()
file.close()

print("Data of the file is :-",data)

#  Write code to open a file named mydata.txt in read mode.

# Write a program to read a text from a given file certificate.txt 
# and find whether it contains the word live.  

file = open("chapter8\certificate.txt","r")
dataOfFile = file.read()

dataOfFile = dataOfFile.lower()

if "live" in dataOfFile:
    print("Yes! 'Live' word is present in the certificate.text")
else:
    print("No")


#  Open a file called report.txt in write mode.

file= open("report.txt","w")

file = open("chapter8\ report.txt","w")
file.write("Learning python!")

file = open("chapter8\ report1.text","a")
file.write("Maneesha is very clever \n")

# Create a file named saumya_info.txt using "x" mode.

file = open("chapter8\ report34.txt","x")
file.write("Learning python!")


# methods in oops
# Create class Student that takes 3 marks and has a method average(). 

class student:

    def __init__(self,name,listOfMarks):
        self.name =name
        self.listOfMarks= listOfMarks
        pass 

    

    def average(self):
        sum =0
        for eachValue in self.listOfMarks:
            sum = sum+eachValue
        average = sum/3
        print("Average is ",average)


s1 = student("maneesha",[99,98,97])
s1.average()
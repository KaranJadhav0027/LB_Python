"""############################################################

Enter a number :5
Enter a Multiple Number :3

3   6   9   12   15
###############################################################"""

class Number:
    def __init__(self,No1,No2):
        self.No1=No1
        self.No2=No2

    def DisplayMultiple(self):
        
        if self.No1<0:
            self.No1=-self.No1
        for i in range(1,self.No1+1):
             Ret=i*self.No2
             print(Ret,"  ",end="")
        
def main():
    print("Enter a number :",end="")
    Value1=int(input())

    print("Enter a Multiple Number :",end="")
    Value2=int(input())

    nobj=Number(Value1,Value2)
    nobj.DisplayMultiple()


if __name__=="__main__":
    main()
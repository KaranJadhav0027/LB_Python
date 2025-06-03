"""############################################################

Enter a number :25

Even Numbers :
2   4   6   8   10   12   14   16   18   20   22   24
Odd Numbers :
1   3   5   7   9   11   13   15   17   19   21   23   25
###############################################################"""

class Number:
    def __init__(self,No):
        self.No=No

    def DisplayEven(self):
        print("Even Numbers :")
        if self.No<0:
            self.No=-self.No
        for i in range(1,self.No+1):
            if i%2==0:
                print(i,"  ",end="")
        print()
    
    def DisplayOdd(self):
        print("Odd Numbers :")
        if self.No<0:
            self.No=-self.No
        for i in range(1,self.No+1):
            if i%2!=0:
                print(i,"  ",end="")

def main():
    print("Enter a number :",end="")
    Value=int(input())

    nobj=Number(Value)
    nobj.DisplayEven()
    
    nobj.DisplayOdd()

if __name__=="__main__":
    main()
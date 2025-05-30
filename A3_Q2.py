"""############################################################
    A program Dispaly Even And Odd Factors Using For and While Loop
    
Enter a Number :24

OutPut:
Using For Loop Even Number
2       4       6       8       12
Using While Loop Even Number
2       4       6       8       12
Using For Loop Odd Number
1       3
Using While Loop Odd Number
1       3

###############################################################"""
class Loop:
    def __init__(self,No1):
        self.No1=No1
        
    def DisplayFroEven(self):
        print("Using For Loop Even Number")
        for i in range(1,self.No1):
            if self.No1%i==0 and i%2==0:
              print(i,end="\t")

    def DisplayWhileEven(self):
        print("Using While Loop Even Number")
        i=1
        while i<self.No1:
            if self.No1%i==0 and i%2==0:
               print(i,end="\t")
            i=i+1
    
    def DisplayFroOdd(self):
        print("Using For Loop Odd Number")
        for i in range(1,self.No1):
            if self.No1%i==0 and i%2!=0:
              print(i,end="\t")

    def DisplayWhileOdd(self):
        print("Using While Loop Odd Number")
        i=1
        while i<self.No1:
            if self.No1%i==0 and i%2!=0:
               print(i,end="\t")
            i=i+1
        
def main():
    print("Enter a Number :",end="")
    Value1=int(input())

    if Value1<0:
        Value1=-Value1
         
    Dobj=Loop(Value1)
    Dobj.DisplayFroEven()
    print()
    Dobj.DisplayWhileEven()
    print()
    Dobj.DisplayFroOdd()
    print()
    Dobj.DisplayWhileOdd()
    
if __name__=="__main__":
    main()
"""############################################################
   A program Dispaly Count  of Even And Odd Number
    
Enter a Number  :11

Output:
Using For Loop Even Number
0       2       4       6       8       10      12      14      16      18      20
Using While Loop Even Number
0       2       4       6       8       10      12      14      16      18      20
Using For Loop Odd Number
1       3       5       7       9       11      13      15      17      19      21
Using While Loop Odd Number
1       3       5       7       9       11      13      15      17      19      21

###############################################################"""
class Loop:
    def __init__(self,No1):
        self.No1=No1
        
    def DisplayFroEven(self):
        count=self.No1*2
        print("Using For Loop Even Number")
        for i in range(count):
            if i%2==0:
              print(i,end="\t")

    def DisplayWhileEven(self):
        count=self.No1*2
        print("Using While Loop Even Number")
        i=0
        while i<count:
            if i%2==0:
               print(i,end="\t")
            i=i+1
    
    def DisplayFroOdd(self):
        count=self.No1*2
        print("Using For Loop Odd Number")
        for i in range(count):
            if i%2!=0:
              print(i,end="\t")

    def DisplayWhileOdd(self):
        count=self.No1*2
        print("Using While Loop Odd Number")
        i=0
        while i<count:
            if i%2!=0:
               print(i,end="\t")
            i=i+1
        
def main():
    print("Enter a Number  :",end="")
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
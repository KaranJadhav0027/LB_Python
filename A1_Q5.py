"""############################################################
    A program print Numbe of Star(*) usin While And For Loop

Enter a Number :6
Using For Loop
*       *       *       *       *       *
Using While Loop
*       *       *       *       *       *

###############################################################"""
class Loop:
    def __init__(self,No):
        self.No=No

    def DisplayFro(self):
        print("Using For Loop")
        for i in range(self.No):
            print("*",end="\t")

    def DisplayWhile(self):
        print("Using While Loop")
        i=0
        while i<self.No:
            print("*",end="\t")
            i=i+1
        
def main():
    print("Enter a Number :",end="")
    Value1=int(input())
     
    if Value1<0:
        Value1=-Value1
        
    Dobj=Loop(Value1)
    Dobj.DisplayFro()
    print()
    Dobj.DisplayWhile()
    
if __name__=="__main__":
    main()
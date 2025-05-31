"""############################################################
   A program Display Reverse of factors

Enter a Number :18

9  6  3  2  1
###############################################################"""

class RevFact:
    def __init__(self,No):
        self.No=No
    
    def Fact(self):
        for i in range(self.No-1,0,-1):
            if self.No%i==0:
                print(i,end="  ")
        

def main():
    print("Enter a Number :",end="")
    Value=int(input())

    if Value<0:
        Value=-Value

    Mobj=RevFact(Value)
    Mobj.Fact()

if __name__=="__main__":
    main()
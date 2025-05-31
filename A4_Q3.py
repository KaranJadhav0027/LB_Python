"""############################################################
   A program Display Numbers Non  of factors

Enter a Number :18

4  5  7  8  10  11  12  13  14  15  16  17
###############################################################"""

class RevFact:
    def __init__(self,No):
        self.No=No
    
    def Fact(self):
        for i in range(1,self.No):
            if self.No%i!=0:
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
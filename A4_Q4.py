"""############################################################
   A program Display Addition of Non-Factors 

Enter a Number :18

Addition of Non-Factors is : 132
###############################################################"""

class RevFact:
    def __init__(self,No):
        self.No=No
    
    def Fact(self):
        Total=0
        for i in range(1,self.No):
            if self.No%i!=0:
                Total=Total+i
        return Total
                      
def main():
    print("Enter a Number :",end="")
    Value=int(input())

    if Value<0:
        Value=-Value

    Mobj=RevFact(Value)
    Ret=Mobj.Fact()
    print("Addition of Non-Factors is :",Ret)

if __name__=="__main__":
    main()
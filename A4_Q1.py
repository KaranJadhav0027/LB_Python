"""############################################################
   A program Display Multiplication of factors

Enter a Number :12

Multiplication of Factors : 144
###############################################################"""

class MultFact:
    def __init__(self,No):
        self.No=No
    
    def Fact(self):
        Total=1
        for i in range(1,self.No):
            if self.No%i==0:
                Total=Total*i
        return Total

def main():
    
    print("Enter a Number :",end="")
    Value=int(input())

    if Value<0:
        Value=-Value

    Mobj=MultFact(Value)
    Ret=Mobj.Fact()
    print("Multiplication of Factors :",Ret)

if __name__=="__main__":
    main()
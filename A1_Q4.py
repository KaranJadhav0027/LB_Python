"""############################################################
    A program Check Number is Divisible by or not

Enter First  Number :567
Enter Second Number :5

OutPut
567  is not Divisible by  5

###############################################################"""
class Check:
    def __init__(self,No1,No2):
        self.No1=No1
        self.No2=No2
    
    def Division(self):
        if self.No2==0:
            print("Enter Greather than Zero number")
            return False
        if self.No1%self.No2==0:
            return True
        else:
            return False
        
def main():
    print("Enter First  Number :",end="")
    Value1=int(input())

    print("Enter Second Number :",end="")
    Value2=int(input())


    Dobj=Check(Value1,Value2)
    Ret=Dobj.Division()
    if Ret==True:
        print(Value1," is Divisible by ",Value2)
    else:
         print(Value1," is not Divisible by ",Value2)
        
if __name__=="__main__":
    main()
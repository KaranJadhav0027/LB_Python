"""############################################################
    A program Check Number Even or Odd

Enter A Number :23456

23456  is Even Number

###############################################################"""
class Check:
    def __init__(self,No1):
        self.No1=No1

    def EvenNumber(self):
        
        if self.No1%2==0:
            return True
        else:
            return False
        
def main():
    print("Enter A Number :",end="")
    Value1=int(input())


    Dobj=Check(Value1)
    Ret=Dobj.EvenNumber()
    if Ret==True:
        print(Value1," is Even Number")
    else:
         print(Value1," is Odd Number")
        
if __name__=="__main__":
    main()
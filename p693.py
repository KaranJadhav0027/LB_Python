class Arithematic:
    def __init__(self,A=0,B=0):
        
        self.No1=A
        self.No2=B

    def Addition(self):
        return self.No1+self.No2
    
    def Substraction(self):
        return self.No1-self.No2
    
def main():
  
    obj1=Arithematic(11 ,10)
    
    Ret=obj1.Addition()
    print("Addition is ",Ret)
    Ret=obj1.Substraction()
    print("Substraction is ",Ret)
      
if __name__=="__main__":
    main()
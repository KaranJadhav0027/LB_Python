"""############################################################

Input:
Enter a number :45087650680605605640
Output:
45087650680605605640 Contain Zero
Count of Zero is  5


Input:
Enter a number :234567
Output:
234567 Not Contain Zero
###############################################################"""
class Digit:
    def __init__(self,No1):
        self.No1=No1
     
    def CheckZero(self):
       if self.No1<0:
           self.No1=-self.No1
    
       while self.No1>0:
          Dig=self.No1%10
          if Dig==0:
              return True
         
          self.No1=int(self.No1/10)
       return False
    
    def CountZero(self):
       if self.No1<0:
           self.No1=-self.No1
       
       Count=0
       while self.No1>0:
          Dig=self.No1%10
          if Dig==0:
              Count=Count+1
          self.No1=int(self.No1/10)
       
       return Count 
    

def main():
    print("Enter a number :",end="")
    Value1=int(input())
    
    obj=Digit(Value1)
    Ret=obj.CheckZero()
    if Ret==True:
        print(Value1,"Contain Zero")
    else:
        print(Value1,"Not Contain Zero")

    Ret=obj.CountZero()
    print("Count of Zero is ",Ret)
if __name__=="__main__":
    main()
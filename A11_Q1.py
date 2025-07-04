"""############################################################

Input:
Enter a number :87634

OutPut:
4
3
6
7
8
###############################################################"""
class Digit:
    def __init__(self,No1):
        self.No1=No1
     
    def DigitReverse(self):
       if self.No1<0:
           self.No1=-self.No1
    
       while self.No1>0:
          Dig=self.No1%10
          print(Dig)
          self.No1=int(self.No1/10)

def main():
    print("Enter a number :",end="")
    Value1=int(input())
    
    obj=Digit(Value1)
    obj.DigitReverse()
if __name__=="__main__":
    main()
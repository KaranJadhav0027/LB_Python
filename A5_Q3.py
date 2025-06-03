"""############################################################

Enter a number :4

*       $       *       $       *       $       *       $
###############################################################"""

class NumberLine:
    def __init__(self,No):
        self.No=No

    def Display(self):
        if self.No<0:
            self.No=-self.No

        for i in range(-self.No,self.No+1):
            print(i,"\t",end="")

def main():
    print("Enter a number :",end="")
    Value=int(input())

    nobj=NumberLine(Value)
    nobj.Display()

if __name__=="__main__":
    main()
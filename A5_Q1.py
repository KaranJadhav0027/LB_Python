"""############################################################

Enter a number :4

*       $       *       $       *       $       *       $
###############################################################"""

class Pattern:
    def __init__(self,No):
        self.No=No

    def Display(self):
        if self.No<0:
            self.No=-self.No

        for i in range(self.No):
            print("*\t$\t",end="")

def main():
    print("Enter a number :",end="")
    Value=int(input())

    pobj=Pattern(Value)
    pobj.Display()

if __name__=="__main__":
    main()
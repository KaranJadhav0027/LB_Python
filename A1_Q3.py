"""############################################################
    A program print 1 to N and N to 1 number 

Enter A Number :5

1       2       3       4       5
5       4       3       2       1

###############################################################"""
class Loop:
    def __init__(self,No):
        self.No=No
    
    def Display(self):
        i=1
        while i<=self.No:
            print(i,end="\t")
            i=i+1

    def DisplayReverse(self):
        i=5
        while i>=1:
            print(i,end="\t")
            i=i-1
        
def main():
    print("Enter A Number :",end="")
    Value1=int(input())

    Dobj=Loop(Value1)
    Dobj.Display()
    print()
    Dobj.DisplayReverse()
    


if __name__=="__main__":
    main()
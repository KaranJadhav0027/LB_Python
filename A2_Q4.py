"""############################################################
    A program Dispaly Except(Alphabet/ Number/ Symbol) and print 
    there Frequency
    
Enter a Alphabet/ Number/ Symbol :A
Enter Frequency :5

Using For Loop
A       A       A       A       A
Using While Loop
A       A       A       A       A

###############################################################"""
class Loop:
    def __init__(self,No1,No2):
        self.No1=No1
        self.No2=No2

    def DisplayFro(self):
        print("Using For Loop")
        for i in range(self.No2):
            print(self.No1,end="\t")

    def DisplayWhile(self):
        print("Using While Loop")
        i=0
        while i<self.No2:
            print(self.No1,end="\t")
            i=i+1
        
def main():
    print("Enter a Alphabet/ Number/ Symbol :",end="")
    Value1=input()

    print("Enter Frequency :",end="")
    Value2=int(input())
     
    if Value2<0:
        Value2=-Value2
        
    Dobj=Loop(Value1,Value2)
    Dobj.DisplayFro()
    print()
    Dobj.DisplayWhile()
    
if __name__=="__main__":
    main()
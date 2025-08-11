"""
Enter a Number Row
4
Enter a Number Coloum
5

$       $       $       $       $
$       $       $       $       $
$       $       $       $       $
$       $       $       $       $

"""

def Display(row,col):

    for i in range(1,row+1,1):
        print("$\t"*col)
    
def main():
    print("Enter a Number Row")
    Value1=int(input())
   
    print("Enter a Number Coloum")
    Value2=int(input())

    Display(Value1,Value2)  

if __name__=="__main__":
    main()
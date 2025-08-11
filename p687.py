"""
Enter a Number Row
5
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""

def Display(row):

    for i in range(1,row+1,1):
        print(" "*(row-i),end="")
        print("* "*i)
    for i in range(row-1,0,-1):
        print(" "*(row-i),end="")
        print("* "*i)

def main():
    print("Enter a Number Row")
    Value=int(input())
   
    Display(Value)  

if __name__=="__main__":
    main()
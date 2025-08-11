# input Hello
"""
 H       e       l       l       o
H       e       l       l       o
H       e       l       l       o
H       e       l       l       o
H       e       l       l       o
"""

def Display(Data):

    for i in  range(len(Data)):
        for ch in Data:
           print(ch,end="\t")
        print()
      
    print()

def main():
    print("Enter a String")
    str=input()

    Display(str)  

if __name__=="__main__":
    main()
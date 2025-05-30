"""############################################################
    A program to Convert Case

Enter a Character :K
k

###############################################################"""
class Converter:
    def __init__(self,char):
        self.char=char
    
    def ConverterFun(self):
        if(self.char>='A' and self.char<='Z'):
            print(self.char.lower())
        elif(self.char>='a' and self.char<='z'):
            print(self.char.upper())
                    
        
def main():
    print("Enter a Character :",end="")
    Str=input()

    Cobj=Converter(Str)
    Cobj.ConverterFun()
     
if __name__=="__main__":
    main()
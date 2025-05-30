"""############################################################
   A program to Check Character is Vowel or Consonant
  
Enter Character :A
A  is a Vowel

Enter Character :D
D  is a Consonant
###############################################################"""
class Check:
    def __init__(self,Char):
        self.char=Char
        
    def CheckVowel(self):
        if self.char=='a'or self.char=='e'or self.char=='i'or self.char=='o'or self.char=='u' or self.char=='A'or self.char=='E'or self.char=='I'or self.char=='O'or self.char=='U':
            return True
        else:
            return False

def main():
    print("Enter Character :",end="")
    Character=input()
    
    Cobj=Check(Character)
    Ret=Cobj.CheckVowel()
       
    if Ret==True:
        print(Character," is a Vowel")
    else:
        print(Character," is a Consonant")

if __name__=="__main__":
    main()
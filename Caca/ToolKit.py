from logging import exception
from time import sleep, strftime
import os 
import pyshorteners
from ToolKitBASE import user
from time import sleep


def shortLink():
   link = input("Introduce you're link: ")
   shortener = pyshorteners.Shortener()
   finalLink = shortener.tinyurl.short(link)

   f = False
   while not f:
      choose2_1 = input("Show the shorted link in console (1) or save in a .txt (2): ")
      if choose2_1 == "1":
         print(finalLink)
         f = True
         sleep(5)

         os.system('cls' if os.name == 'nt' else 'clear')

      elif choose2_1 == "2":
         directorylinks = user("user_link_dir")
         f = True

         with open(user("user_link_dir")/"ShortedLinks.txt", "a") as shortedLinks:
            shortedLinks.write("\n{} = {}".format(link, finalLink))
            print("Link writed successfully")
         
         os.system('cls' if os.name == 'nt' else 'clear')   
      else:
         print("Incorrect Value")


def schoolTools():
   print("""
   1 - Marks Calculator
   2 - Webgrafia Generator
   3 - Exit
    
   """)



def main():
   os.system('cls' if os.name == 'nt' else 'clear')
   finish = False
   while not finish:
      print("""
      $$$$$$$$\                  $$\ $$\   $$\ $$\   $$\     
      \__$$  __|                 $$ |$$ | $$  |\__|  $$ |    
         $$ | $$$$$$\   $$$$$$\  $$ |$$ |$$  / $$\ $$$$$$\   
         $$ |$$  __$$\ $$  __$$\ $$ |$$$$$  /  $$ |\_$$  _|  
         $$ |$$ /  $$ |$$ /  $$ |$$ |$$  $$<   $$ |  $$ |    
         $$ |$$ |  $$ |$$ |  $$ |$$ |$$ |\$$\  $$ |  $$ |$$\ 
         $$ |\$$$$$$  |\$$$$$$  |$$ |$$ | \$$\ $$ |  \$$$$  |
         \__| \______/  \______/ \__|\__|  \__|\__|   \____/
         """)


      
      start = False
      while not start:
         print("""


         1 - Link shorter
         2 - Movefiler 
         3 - Password Gen
         4 - Password trunk
         5 - School Tools Menu
         6 - Exit

         """)
         choose = None
         while choose not in range(7):
            choose = int(input("-> "))
         start = True
            
         os.system('cls' if os.name == 'nt' else 'clear')


         if choose == 1:
               shortLink()

         elif choose == 2:
            pass # moveFiler()
            
         elif choose == 3:
            pass #passwordGen()

         elif choose == 4:
            pass #passwordTrunk()

         elif choose == 5:
            pass #schoolTools()

         elif choose == 6:
            finish = True


if __name__ == "__main__":
   main()



from time import sleep
import pyshorteners
import os


def shortLink():
   link = input("Introdueix el link: ")
   shortener = pyshorteners.Shortener()
   finalLink = shortener.tinyurl.short(link)
      
   print(finalLink)

   sleep(5)

   os.system('cls' if os.name == 'nt' else 'clear')

def main():
   shortLink()

if __name__ == "__main__":
   main()
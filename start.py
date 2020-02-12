
from subprocess import call
import os
choice = int(input("\t\tHello\n Main menu:\n 1. Download movie\n 2. Download playlist\n 3. Download audio\n 0. Exit\n"))


def start():
    exit = False
    while not exit:
        if choice == 1:
            url = input("Enter movie url: ")
            choice_format = "youtube-dl -F " + url
            call(choice_format.split(), shell=False)
            format_url = input("Enter format movie: ")
            command = "youtube-dl -f " + format_url + " " + url
            os.chdir("Downloads")
            call(command, shell=False)
                 
        elif choice == 2:
            url = input("Enter playlist url: ")
            command = "youtube-dl -citk –format mp4 –yes-playlist " + url
            os.chdir("Downloads/playlist")
            call(command, shell=False)

        elif choice == 3:
            url = input("Enter video url: ")
            command = "youtube-dl -f bestaudio " + url
            os.chdir("Downloads/audio")
            call(command, shell=False)
              
        elif choice == 0:
            exit = True
        else:
            print("Read the manual")
        
start()        
  

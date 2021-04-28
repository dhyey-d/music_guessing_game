import random
import os
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
pygame.mixer.init()
root = tk.Tk()
root.withdraw()
directory = askdirectory()
os.chdir(directory)
list_dir = os.listdir(directory)
list_dir.sort()
list_of_songs = []
for files in list_dir:
    if files.endswith(".mp3"):
        list_of_songs.append(files)
another_track = True


while another_track:
    try:
        one_rand_song_array = random.sample(range(len(list_of_songs)), 1)
        one_rand_song = one_rand_song_array[0]

        pygame.mixer.music.stop()
        pygame.mixer.init()
        pygame.mixer.music.load(list_of_songs[one_rand_song])
        pygame.mixer.music.play()

        while pygame.mixer.music.get_pos() < 3000:
            continue
        pygame.mixer.music.pause()
        prompt1 = input("Type m for more \n\nType a for answer \n\nType q for quit\n\n")
        if prompt1 == "m":
            print("\n..............................\n")
            print("\nPlaying more\n")
            pygame.mixer.music.unpause()

            while pygame.mixer.music.get_pos() < 8000:
                continue
            pygame.mixer.music.pause()
            prompt2 = input("Type m for more \n\nType a for answer \n\nType q for quit\n\n")
            if prompt2 == "m":
                print("\n..............................\n")
                print("\nPlaying more\n")
                pygame.mixer.music.unpause()

                while pygame.mixer.music.get_pos() < 15000:
                    continue
                pygame.mixer.music.pause()
                prompt3 = input("No more music \n\nType a for answer \n\nType q for quit\n\n")
                if prompt3 == "a":
                    print("\n..............................\n")
                    print(f"The correct answer was {list_of_songs[int(one_rand_song)]}\n")
                    next_track = input("Do you want to continue? (y/n)")
                    if next_track == "n":
                        break
                else:
                    break

            elif prompt2 == "a":
                print("\n..............................\n")
                print(f"The correct answer was {list_of_songs[int(one_rand_song)]}\n")
                next_track = input("Do you want to continue? (y/n)")
                if next_track == "n":
                    break

        elif prompt1 == "a":
            print("\n..............................\n")
            print(f"The correct answer was {list_of_songs[int(one_rand_song)]}\n")
            next_track = input("Do you want to continue? (y/n)")
            if next_track == "n":
                break

        else:
            print("\nGoodbye\n")
            break

    except pygame.error:
        continue

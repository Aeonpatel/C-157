# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 08:06:42 2024

@author: apal
"""

from tkinter import*
root=Tk()

from PIL import ImageTk, Image

root.title("Endless Dice Game")
root.geometry("600x600")

root.configure(background="orange")



player1 = Label(root,text="Player 1",bg="royal blue" ,fg="white" )
player1.place(relx="0.1",rely="0.5")

player2 = Label(root,text="Player 2" , bg="royal blue" , fg="white")
player2.place(relx="0.9",rely="0.5")

player1_score_label = Label(root,text="0",bg="orange",fg="white")
player1_score_label.place(relx="0.1",rely="0.6")

player2_score_label = Label(root,text="0",bg="orange",fg="white")
player2_score_label.place(relx="0.9",rely="0.6")

label=Label(root)
label.pack()

pokemon_list = {"pikachu","raichu","larvitar","pupitar","tyranitar","mewtwo"}
power_list = {30,60,110,190,250,340}

player1score=0
def player_1():
    global player1score
    random_no = random.randint(1,6)
    random_pokemon = pokemon_list[random_no]
    label["text"] = random_pokemon
    
    random_power = random.randint(1,6)
    player1score = player1score + random_power
    player1_score_label["text"] = str(player1score)
    
player1_btn=Button(root , hint="Play" , command=player_1)
player.pack()
    
player2score=0
def player_2():
    global player2score
    random_no2 = random.randint(1,6)
    random_pokemon2 = pokemon_list[random_no2]
    label["text"] = random_pokemon2
    
    random_power2 = random.randint(1,6)
    player2score = player2score + random_power2
    player2_score_label["text"] = str(player2score)

player2_btn=Button(root , hint="Play" , command=player_2)    
player2.pack()
    
    

root.mainloop()

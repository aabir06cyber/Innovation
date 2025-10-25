# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:58:38 2024

@author: Aabir Bhattacharya
"""

#------WORD GAME--------

import pygame
import datetime
import time
import os
import sys
import keyboard
import random
import fontstyle
import csv
import math
from IPython import get_ipython

soundplayer=pygame.mixer
soundplayer.init()

print()
def greet():
    currentTime=datetime.datetime.now()
    currentHour=currentTime.hour
    if(currentHour>=6 and currentHour<12):
        print("GOOD MORNING!")
        soundplayer.music.load("F:/My Python Programs/Word Game/Good Morning.mp3")
        soundplayer.music.play()
    elif(currentHour>=12 and currentHour<18):
        print("GOOD AFTERNOON!")
        soundplayer.music.load("F:/My Python Programs/Word Game/Good Afternoon.mp3")
        soundplayer.music.play()
    elif(currentHour>=18 and currentHour<24):
        print("GOOD EVENING!")
        soundplayer.music.load("F:/My Python Programs/Word Game/Good Evening.mp3")
        soundplayer.music.play()
    else:
        print("Sorry, not operational from 12 am to 6 pm.")
        print("Exiting in 3 seconds...")
        time.sleep(3) #Wait 3 seconds
        print("Termination successful.")
        #sys.exit(0) #Exiting program
def prestart():
    print()
    time.sleep(2)
    print("Connecting to word list",end="")
    for i in range(1,4,1):
        time.sleep(0.8) #print at 0.8s intervals
        print(".",end="")
    print("100%")
    print("Connecting to log file",end="")
    for i in range(1,4,1):
        time.sleep(0.8) #print at 0.8s intervals
        print(".",end="")
    print("100%")
    print("Loading error checker",end="")
    for i in range(1,4,1):
        time.sleep(0.8) #print at 0.8s intervals
        print(".",end="")
    print("100%")
    print("Loading score calculator",end="")
    for i in range(1,4,1):
        time.sleep(0.8) #print at 0.8s intervals
        print(".",end="")
    print("100%")
def instructions():
    print()
    print()
    instruct_file=open("F:/My Python Programs/Word Game/User Instruction.txt")
    print(instruct_file.read())
    instruct_file.close()
    #35sec timer....
    for i in range(35,-1,-1):
        if(i>=10):
            print("\r\t\t\t\t\t\t\tTime Left: "+str(i),end="")  
        else:
            print("\r\t\t\t\t\t\t\tTime Left: 0"+str(i),end="")
        time.sleep(1)
    #os.system('clear')
    print("\nTHE WORD GAME")
def  clearscreen():
    #os.system("cls")
    #The following is for IPython console
    #for cmd, os.system("cls") works fine
    try:
       get_ipython().magic('clear')
       get_ipython().magic('reset -f')
    except: pass
def player_info():
    global player_name
    player_name=input("Please enter your name: ")
    print("Creating new Player ID...")
    time.sleep(0.7)
    global user_id
    user_id=round((random.random()*(10**5)))
    print("\rYour Player ID is: ",user_id)
    
def music():
    music1="A Day at Sea [NCS].mp3"
    music2="Ikson - Alive (Official).mp3"
    music3="Ricky Rich x Habibi [Albanian Remix].mp3"
    music4="Sky Mubs - Battle's Spirit.mp3"
    music5="Sky Mubs X Alston & Ozone - Back to Home.mp3"
    print("1. ",music1)
    print("2. ",music2)
    print("3. ",music3)
    print("4. ",music4)
    print("5. ",music5)
    print("6. No music")
    print("You can change this later as well.")
    bgm=input("Please choose any background music (Enter only number):")
    if(bgm=="1"):
        bgm=music1
    elif(bgm=="2"):
        bgm=music2
    elif(bgm=="3"):
        bgm=music3
    elif(bgm=="4"):
        bgm=music4
    elif(bgm=="5"):
        bgm=music5
    if(bgm in "12345"):
        soundplayer.music.load("C:/Users/Aabir Bhattacharya/Music/Music/"+bgm)
        soundplayer.music.play()
        soundplayer.music.play(loops=-1)
def initialize_wordlist():
    global file;file=open("F:/My Python Programs/Word Game/wordlist.ENABLE.txt")
    global wordlist; wordlist=file.readlines()
    for i in range(len(wordlist)):
        wordlist[i]=wordlist[i].rstrip()
def startgame():
    comp_word=""
    player_word=""
    global player_input_list; player_input_list=[]
    global computer_output_list; computer_output_list=[]
    commands=["stop game","@changebgm","@stopbgm"]#more commands to be added...
    global unique_inputs,unique_outputs #to finally store single occurences of words...
    unique_inputs=unique_outputs=[]
    global linecount; linecount=1
    global comp_score; comp_score=0
    global player_score; player_score=0
    global game_start_time; game_start_time=time.time()
    global game_stop_time
    global total_play_time
    
    print("  Line  ",end="")
    print("   Computer        vs      Player")
    while(player_word!="stop game"):
        if(linecount<10):
            print("    ",linecount,":",end=" ")
        elif(linecount<100):
            print("   ",linecount,":",end=" ")
        elif(linecount<1000):
            print("  ",linecount,":",end=" ")
        elif(linecount<10000):
            print(" ",linecount,":",end=" ")
        if(linecount==1):
            comp_word=random.choice(wordlist)
        #print the next computer's word starting with last letter of player's word...
        else:
            while(True):
                comp_word=random.choice(wordlist)
                if(comp_word[0]==player_word[-1]):
                    break
        gap=23-len(comp_word)
        print(comp_word," "*gap,end="") #" "*gap is for space after output...
        #input player's word...
        player_word=input()
        #follow commands...
        if(player_word!="stop game" or player_word not in commands):
            player_input_list.append(player_word)
            player_score+=1
            computer_output_list.append(comp_word)
            comp_score+=1
        if(player_word in commands):#for now only stop game...to be added aftrwds.
            game_stop_time=time.time()
            break
        linecount+=1
    total_play_time=time.strftime("%H:%M:%S",time.gmtime(game_stop_time-game_start_time))
def checking():#edit...
    print("\n\n\n")
    print("\t\t\t\t\tCHECKING FOR ERRORS...")
    
    #---------------DISPLAYING PERCENTAGE....----------------
    percent_checked=[]
    for i in range(0,101,1):
        percent_checked.append(i)
    perc1=0
    perc2=0
    for i in range(0,10,1):
        print("\rLoading: "+str(perc2)+"%",end="")
        if(perc2==100): break
        while(True):
            perc2=random.choice(percent_checked)
            if(perc2>perc1):
                perc1=perc2
                break
        time.sleep(0.76)
    #-----------------------------------
    deduct=0
    repeated=0
    repeated_COMP=0
    lineoferror_repeated=""
    errorlist_deductline=[] #to create a dictionary to store lines where errors were made
    errordict_repeated={} #to store repeated (lines)
    for i in range(0,len(player_input_list),1):
        checkterm=player_input_list[i]
        if(checkterm in wordlist and checkterm not in unique_inputs and checkterm!="--"):
            unique_inputs.append(checkterm)
        if(checkterm[0]!=computer_output_list[i][-1]):
            deduct+=1 #to award -1 point for not beginning with same letter
            errorlist_deductline.append(i)
        #to check for repeated words
        for j in range(i+1,len(player_input_list),1):
            sample=player_input_list[j]
            if(sample==checkterm and sample!="--"):
                lineoferror_repeated+=str(j+1)+","
                repeated+=1
                player_input_list[j]="--"
        if(repeated>=1):
            lineoferror_repeated.rstrip(',')
            errordict_repeated[checkterm]=lineoferror_repeated
            lineoferror_repeated="";repeated=0 #reset values for next iteration
                
    global final_player_score
    final_player_score=deduct*(-1)+len(unique_inputs)
    
    #for computer's errors:
    for i in range(0,len(computer_output_list),1):
        checkterm_COMP=computer_output_list[i]
        for j in range(i+1,len(computer_output_list),1):
            sample_COMP=computer_output_list[j]
            if(sample_COMP==checkterm_COMP and sample_COMP!="--"):
               # getlineoferror=getlineoferror+","+str(j)
               # error_line_dict.setdefault(sample,getlineoferror)
                #get frequency of repeated words
                repeated_COMP+=1
    global final_comp_score
    final_comp_score=len(computer_output_list)-repeated_COMP
    file.close()
    score_table=[]
    cat=["Final Score","Total words","Deducted","Repeated","Unique Inputs"]
    cat_disp=[[final_player_score,final_comp_score],
              [linecount-1,linecount-1],
              [deduct,repeated_COMP],
              [repeated,repeated_COMP],
              [len(unique_inputs),final_comp_score]]
    print("\n\t\t\t\t\t\t\t\t\t\tTABULATED RESULT")
    print("Category","\t\tPLAYER","\t\tCOMPUTER")
    for i in range(len(cat)):
        print(cat[i],end="")
        print(" "*(18-len(cat[i])),end="")
        print(cat_disp[i][0],"\t\t\t",cat_disp[i][1])
    print("UNIQUE INPUTS: ",unique_inputs)
    print("REPEATED: ",errordict_repeated)
    print("DEDUCTED AT: ",errorlist_deductline)
    print("TOTAL PLAY TIME: ",total_play_time)
    if(final_player_score>final_comp_score): print("Result: Won")
    elif(final_player_score==final_comp_score): print("Result: Tie")
    elif(final_player_score<final_comp_score): print("Result: Lost");
            
def write_to_Game_Data_File():
    global game_status
    if(final_player_score>final_comp_score): game_status="Won"
    elif(final_player_score==final_comp_score): game_status="Tie"
    elif(final_player_score<final_comp_score): game_status="Lost"
    datafile=open("F:/My Python Programs/Word Game/Game Data File.csv","a",newline="")
    data=[user_id,player_name,linecount-1,final_player_score,final_comp_score,game_status,total_play_time]
    filewriter=csv.writer(datafile).writerow(data)
    datafile.close()
    
    
    
#Calling functions...
greet()
prestart()
instructions()
clearscreen()
player_info()
music()
initialize_wordlist()
startgame()
checking()  
write_to_Game_Data_File()
from turtle import update
from games import run_game
from games import sudoku
from games import packman
from games import game4
from player import player
from matplotlib import pyplot as plt
# from scoreboard import get_score


Game1="alien_invasion"
Game2="sudoku"
Game3="Packman"
Game4="snake"


def play_game():
   #  num=numm
    print('Now choose the game you want to play:')
    print(f'1.{Game1}')
    print(f'2.{Game2}')
    print(f'3.{Game3}')
    print(f'4.{Game4}')
    num=int(input('Choose the number associated with the game:'))
   #  num=printing()

    if num==1:
       file=open('highscore.txt','r')
       score=file.read()
       Player.createOrUpdateFile(score,num)
       file.close()

    if num==1:
       run_game()
       
    elif num==2:
       score2=sudoku()
       if score2==None:
          score2=0
       Player.createOrUpdateFile(score2,num)
    elif num==3:
       score3=packman()
       Player.createOrUpdateFile(score3,num)
    elif num==4:
       score4=game4()
       Player.createOrUpdateFile(score4,num)
    else:
       print('Please Enter a Valid Number!!')
       play_game()
      

Player=player()
Player.GetName()

def check_scoreboard():
   status=input('Do you want to check the scoreboard? y/n : ')

   if status=='y':
      flag=1
   elif status=='n':
      flag=0
   
   if flag==1:
      print(f'1.{Game1}')
      print(f'2.{Game2}')
      print(f'3.{Game3}')
      print(f'4.{Game4}') 
      num=int(input("choose the game who's scoreboard you want to see: "))
      if num==1:
         i=0
         f=open('all_players.txt','r')
         for each in f:
            i+=1
         score=[]
         # print("h")
         f.close()
         f=open('all_players.txt','r')
         for each in f:
            nm=each
            b=nm.replace('\n','')
            line_number=line_num(b,1)
            if line_number>-1:
               file=open(f'{b}.txt','r')
               all_lines=file.readlines()
               line=all_lines[line_number-1]
               lt=line.split()
               score.append(int(lt[3]))
         # print(score)
         length=len(score)
         i=0
         x=[]
         while(length):
            x.append(i+1)
            i=i+1
            length=length-1
         # print(x)
         plt.title('ALIEN INVASION SCOREBOARD')
         plt.plot(x,score)
         plt.xlabel('players')
         plt.ylabel('scores')
         plt.show()

      if num==2:
         i=0
         f=open('all_players.txt','r')
         for each in f:
            i+=1
         score=[]
         # print("h")
         f.close()
         f=open('all_players.txt','r')
         for each in f:
            nm=each
            b=nm.replace('\n','')
            line_number=line_num(b,2)
            if line_number>-1:
               file=open(f'{b}.txt','r')
               all_lines=file.readlines()
               line=all_lines[line_number-1]
               lt=line.split()
               score.append(int(lt[3]))
         # print(score)
         length=len(score)
         i=0
         x=[]
         while(length):
            x.append(i+1)
            i=i+1
            length=length-1
         # print(x)
         plt.title('SUDOKU SCOREBOARD')
         plt.plot(x,score)
         plt.xlabel('players')
         plt.ylabel('scores')
         plt.show()
      if num==3:
         i=0
         f=open('all_players.txt','r')
         for each in f:
            i+=1
         score=[]
         # print("h")
         f.close()
         f=open('all_players.txt','r')
         for each in f:
            nm=each
            b=nm.replace('\n','')
            line_number=line_num(b,3)
            if line_number>-1:
               file=open(f'{b}.txt','r')
               all_lines=file.readlines()
               line=all_lines[line_number-1]
               lt=line.split()
               score.append(int(lt[3]))
         # print(score)
         length=len(score)
         i=0
         x=[]
         while(length):
            x.append(i+1)
            i=i+1
            length=length-1
         # print(x)
         plt.title('PACKMAN SCOREBOARD')
         plt.plot(x,score)
         plt.xlabel('players')
         plt.ylabel('scores')
         plt.show()
      if num==4:
         i=0
         f=open('all_players.txt','r')
         for each in f:
            i+=1
         score=[]
         # print("h")
         f.close()
         f=open('all_players.txt','r')
         for each in f:
            nm=each
            b=nm.replace('\n','')
            line_number=line_num(b,4)
            if line_number>-1:
               file=open(f'{b}.txt','r')
               all_lines=file.readlines()
               line=all_lines[line_number-1]
               lt=line.split()
               score.append(int(lt[3]))
         # print(score)
         length=len(score)
         i=0
         x=[]
         while(length):
            x.append(i+1)
            i=i+1
            length=length-1
         # print(x)
         plt.title('SNAKE SCOREBOARD')
         plt.plot(x,score)
         plt.xlabel('players')
         plt.ylabel('scores')
         plt.show()

def line_num(name,num):
   string1=f'Game{num}'
   f=open(f'{name}.txt','r')
   flag=0
   index=0
   for line in f:
      index+=1
      if string1 in line:
            flag=1
            break
   if flag==0:
      return -1
   else:
      return index



def check_status():
   status=input('Do you want to continue? y/n : ')
   if status=='y':
      flag=1
   elif status=='n':
      flag=0

   if flag==1:
      play_game()
      check_scoreboard()
      check_status()

play_game()
check_scoreboard()
check_status()



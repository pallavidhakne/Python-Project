import os
from turtle import update
Game1='Game1'
Game2='Game2'
Game3='Game3'
Game4='Game4'
Game5='Game5'

# from play_game import Game1

# from play_game import Player

class player:
    def GetName(self):
        self.name=input("Enter your name:")
        if(os.path.isfile(f'{self.name}.txt')):
            pass
        else:
            f=open('all_players.txt','a')
            f.write(f'\n{self.name}')
            f.close
    def createOrUpdateFile(self,score,num):
        if(os.path.isfile(f'{self.name}.txt')):
            self.score=score
            self.game=num
            if self.game==1:
                Update=self.update(self.game)
                if Update != 0:   
                    f=open(f'{self.name}.txt','r')
                    all_lines=f.readlines()
                    line=all_lines[Update-1]
                    lt=line.split()
                    prev_score=int(lt[3])
                    if(prev_score<int(self.score)):
                        self.Replace(lt[3],str(self.score))
                    f.close()
                else:
                    f=open(f'{self.name}.txt','a+')
                    f.write(f'\nGame1 highest score {score}')
                    f.close()
            elif self.game==2:
                Update=self.update(self.game)
                if Update != 0: 
                    f=open(f'{self.name}.txt','r')
                    all_lines=f.readlines()
                    line=all_lines[Update-1]
                    lt=line.split()
                    prev_score=int(lt[3])
                    if(prev_score<int(self.score)):
                        self.Replace(lt[3],str(self.score))
                    f.close()
                else:
                    f=open(f'{self.name}.txt','a+')
                    f.write(f'\nGame2 highest score {score}')
                    f.close()
            elif self.game==3:
                Update=self.update(self.game)
                if Update != 0: 
                    f=open(f'{self.name}.txt','r')
                    all_lines=f.readlines()
                    line=all_lines[Update-1]
                    lt=line.split()
                    prev_score=int(lt[3])
                    if(prev_score<int(self.score)):
                        self.Replace(lt[3],str(self.score))
                    f.close()
                else:
                    f=open(f'{self.name}.txt','a+')
                    f.write(f'\nGame3 highest score {score}')
                    f.close()
            elif self.game==4:
                Update=self.update(self.game)
                if Update != 0: 
                    f=open(f'{self.name}.txt','r')
                    all_lines=f.readlines()
                    line=all_lines[Update-1]
                    lt=line.split()
                    prev_score=int(lt[3])
                    if(prev_score<int(self.score)):
                        self.Replace(lt[3],str(self.score))
                    f.close()
                else:
                    f=open(f'{self.name}.txt','a+')
                    f.write(f'\nGame4 highest score {score}')
                    f.close()
           
            
        else:
            self.score=score
            self.game=num
            f=open(f'{self.name}.txt','a')
            f.write(self.name)
            if self.game == 1:
                f.write("\nGame1 Highest Score ")
                f.write(str(self.score))
                f.close()
            elif self.game == 2:
                f.write("\nGame2 Highest Score ")
                f.write(str(self.score))
                f.close()
            elif self.game == 3:
                f.write("\nGame3 Highest Score ")
                f.write(str(self.score))
                f.close()
            elif self.game == 4:
                f.write("\nGame4 Highest Score ")
                f.write(str(self.score))
                f.close()
            
    def Replace(self,search_text,replace_text):
        self.search_text=search_text
        self.replace_text=replace_text
        with open(f'{self.name}.txt','r') as file:
            data=file.read()
            data=data.replace(self.search_text,self.replace_text)
        with open(f'{self.name}.txt','w') as file:
            file.write(data)
        
    
    def update(self,num):
        string1=f'Game{num}'
        f=open(f'{self.name}.txt','r')
        flag=0
        index=0
        for line in f:
            index+=1
            if string1 in line:
                flag=1
                break
        if flag==0:
            return 0
        else:
            return index
        

# Player=player()
# Player.GetName()
# print(Player.update(1))


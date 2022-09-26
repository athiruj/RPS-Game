#request Libs
import random
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image

#!setting
#? Rounds  
EndRound = 10

#? your file path
#?Ex 'C:\Users\username\Downloads\RPS'
FliePath ='D:\Workfile\Project\python\school\RPS'

# Game System
Round = []
Win = 1
Lose = 2
Drew = 0
Base = -1
WinColor = '#43C441'
LoseColor = '#848484'
DrewColor = '#EADA4D'
ImgSize = 230

# Red RPS
RRock = Image.open(f'{FliePath}\Red\R_W_Rock.png')
RPaper = Image.open(f'{FliePath}\Red\R_W_Paper.png')
RScissors = Image.open(
    f'{FliePath}\Red\R_W_Scissors.png')
RedRPS = [RRock, RPaper, RScissors]

# Blue RPS
BRock = Image.open(f'{FliePath}\Blue\B_W_Rock.png')
BPaper = Image.open(f'{FliePath}\Blue\B_W_Paper.png')
BScissors = Image.open(
    f'{FliePath}\Blue\B_W_Scissors.png')
BlueRPS = [BRock, BPaper, BScissors]

BaseColor = '#D9D9D9'
BgColor = '#F7F7F7'

# Player
RPlayer = '#F34040'
BPlayer = '#456AEE'
ADrew = Round.count('Drew')
RWin = Round.count('Red')
BWin = Round.count('Blue')
RPlayerScore = []
BPlayerScore = []

# Window screen
width = 800
height = 300

# Score Block size
Swidth = 20
Sheight = Swidth


def settingRound(root, endRound: int):
    x = tk.Scale(root, from_=1, to=15, orient='horizontal')
    x['bg'] = BgColor
    x.set(endRound)
    x.place(x=width/2-50, y=50, width=100, height=50)
    bt = tk.Button(root)
    bt['command'] = lambda: setRound(setRound=x.get(), endRound=endRound)
    bt['text'] = 'set rounds'
    bt.place(x=width/2-50, y=100, width=100, height=30)


def setStartPlayerScore(playerScoreList: list, endRound: int):
    i = 0
    while i < endRound:
        playerScoreList.append(Base)
        i += 1
    return playerScoreList


def setPlayerScoreBlock(nRoot, playerScoreList: list, playerColor: str, position: str, score: int):
    if position == "start":
        # playerScore
        sx = 0
        x = 0
    if position == "end":
        if playerScoreList[EndRound-1] == Base:
            playerScoreList.reverse()
        sx = width-36
        x = width-(len(playerScoreList)*Swidth)

    ScoreRed = tk.Label(nRoot)
    ScoreRed['text'] = score
    ScoreRed['bg'] = BgColor
    st = tkFont.Font(family='Time', size=24)
    ScoreRed['font'] = st
    ScoreRed["fg"] = "#333333"
    ScoreRed.place(x=sx, y=height-(Sheight+39), width=36, height=36)

    for i, item in enumerate(playerScoreList):
        Block = tk.Frame(nRoot)
        Block["highlightthickness"] = "2"
        Block["highlightbackground"] = "#F2F2F2"
        Block["highlightcolor"] = "#000"
        if item == Base:
            Block["bg"] = BaseColor
        if item == Win:
            Block["bg"] = WinColor
        if item == Drew:
            Block["bg"] = DrewColor
        if item == Lose:
            Block["bg"] = LoseColor
        Block.place(x=(i*Swidth)+x, y=height-Swidth,
                    width=Swidth, height=Sheight)
        Team = tk.Frame(nRoot)
        Team["bg"] = playerColor
        Team.place(x=(i*Swidth)+x, y=height-Swidth-3, width=Swidth, height=3)


def updateScore(playerScoreList: list, posList: int, state: int):
    playerScoreList[posList] = state



def setResultImg(rps: list, team: str):
    i = random.randint(0, 2)
    if team == 'Red':
        x = 30
    if team == 'Blue':
        x = width-(ImgSize+30)
    img = ImageTk.PhotoImage(rps[i])
    canvas = tk.Label(root, image=img, bg=BgColor)
    canvas.image = img
    canvas.place(x=x, y=20, width=ImgSize, height=ImgSize)
    return i


def RedWin(pos: int, endRound: int):
    updateScore(playerScoreList=RPlayerScore, posList=pos, state=Win)
    updateScore(playerScoreList=BPlayerScore,
                posList=endRound-pos-1, state=Lose)


def BlueWin(pos: int, endRound: int):
    updateScore(playerScoreList=RPlayerScore, posList=pos, state=Lose)
    updateScore(playerScoreList=BPlayerScore,
                posList=endRound-pos-1, state=Win)


def TeamDrew(pos: int, endRound: int):
    updateScore(playerScoreList=RPlayerScore, posList=pos, state=Drew)
    updateScore(playerScoreList=BPlayerScore,
                posList=endRound-pos-1, state=Drew)
  
    


def resetScore(nRoot, round: list, button: tk.Button, button2: tk.Button):
    button2.place(x=width/2-50, y=150, width=100, height=30)
    round.clear()
    RPlayerScore.clear()
    BPlayerScore.clear()
    setStartPlayerScore(playerScoreList=RPlayerScore, endRound=EndRound)
    setStartPlayerScore(playerScoreList=BPlayerScore, endRound=EndRound)
    setPlayerScoreBlock(nRoot, playerScoreList=RPlayerScore,
                        playerColor=RPlayer, position="start", score=0)
    setPlayerScoreBlock(nRoot, playerScoreList=BPlayerScore,
                        playerColor=BPlayer, position="end", score=0)
    button.place_forget()

def resetScoreButton(nRoot, round: list, button: tk.Button):
    reset = tk.Button(nRoot)
    reset['text'] = 'reset'
    reset['command'] = lambda: resetScore(
        nRoot, round=round, button=reset, button2=button)
    reset.place(x=width/2-50, y=180, width=100, height=30)

def setRound(setRound: int, endRound: int):
    endRound = setRound
    setStartPlayerScore(playerScoreList=RPlayerScore, endRound=endRound)
    setStartPlayerScore(playerScoreList=BPlayerScore, endRound=endRound)
    return endRound

def spinRPS(nRoot, round: list, endRound: int, button: tk.Button):
    i = len(round)
    ip = i
    if i < endRound:
        rPlayer = setResultImg(rps=RedRPS, team='Red')
        bPlayer = setResultImg(rps=BlueRPS, team='Blue')
        st = tkFont.Font(family='Time', size=24)
        T = tk.Label(root,font=st)
        T['bg'] = BgColor
        T["justify"] = "center"

        if rPlayer == bPlayer:
            print('Drew')
            round.append("Drew")
            TeamDrew(pos=ip, endRound=endRound)
            T['text'] = 'Drew'
        # Red Rock win Scissors
        if rPlayer == 0 and bPlayer == 2:
            print('Red')
            round.append("Red")
            RedWin(pos=ip, endRound=endRound)
            T['text'] = 'Red Win'
        # Blue Rock win Scissors
        if rPlayer == 2 and bPlayer == 0:
            print('Blue')
            round.append("Blue")
            BlueWin(pos=ip, endRound=endRound)
            T['text'] = 'Blue Win'

        # Red Paper win Rock
        if rPlayer == 1 and bPlayer == 0:
            print('Red')
            round.append("Red")
            RedWin(pos=ip, endRound=endRound)
            T['text'] = 'Red Win'
        # Blue Paper win Rock
        if rPlayer == 0 and bPlayer == 1:
            print('Blue')
            round.append("Blue")
            BlueWin(pos=ip, endRound=endRound)
            T['text'] = 'Blue Win'
        # Red Scissors win Paper
        if rPlayer == 2 and bPlayer == 1:
            print('Red')
            round.append("Red")
            RedWin(pos=ip, endRound=endRound)
            T['text'] = 'Red Win'
        # Blue Scissors win Paper
        if rPlayer == 1 and bPlayer == 2:
            print('Blue')
            round.append("Blue")
            BlueWin(pos=ip, endRound=endRound)
            T['text'] = 'Blue Win'
        T.place(x=width/2-75, y=100, width=150, height=30)
        # print('Red',round.count('Red'))
        # print('Blue',round.count('Blue'))
        # print('Drew',round.count('Drew'))
    if i == endRound-1:
        print('reset')
        button.place_forget()
        resetScoreButton(nRoot, round=round, button=button)

    setPlayerScoreBlock(nRoot, playerScoreList=RPlayerScore,
                        playerColor=RPlayer, position="start", score=round.count('Red'))
    setPlayerScoreBlock(nRoot, playerScoreList=BPlayerScore,
                        playerColor=BPlayer, position="end", score=round.count('Blue'))



class App:

    def __init__(self, root):
        # setting title
        root.title("Rock Paper Scissors")
        # setting window size
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        # st = tkFont.Font(family='Time', size=24)
        # lt = tkFont.Font(family='Time', size=10)

        # settingRound(root, endRound=EndRound)

        # set Score
        setStartPlayerScore(playerScoreList=RPlayerScore, endRound=EndRound)
        setStartPlayerScore(playerScoreList=BPlayerScore, endRound=EndRound)

        setPlayerScoreBlock(root, playerScoreList=RPlayerScore,
                            playerColor=RPlayer, position="start", score=0)
        setPlayerScoreBlock(root, playerScoreList=BPlayerScore,
                            playerColor=BPlayer, position="end", score=0)

        setResultImg(rps=RedRPS, team='Red')
        setResultImg(rps=BlueRPS, team='Blue')

        g = tk.Button(root)
        g['command'] = lambda: spinRPS(
            root, round=Round, endRound=EndRound, button=g)
        g['text'] = 'start'
        g.place(x=width/2-50, y=150, width=100, height=30)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.configure(bg=BgColor)
    root.mainloop()

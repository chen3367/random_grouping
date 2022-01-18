import random
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('阿明勾最強分組') 
window.resizable(False, False)
window.iconbitmap('images/ming.ico')
window.geometry('770x860')

img = Image.open('images/ming.jpg').resize((385,430), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(img)
ming = Label(window, image = bg)
ming.place(x = 385, y = 0)

img2 = Image.open('images/fly.jpg').resize((770,430), Image.ANTIALIAS)
bg2 = ImageTk.PhotoImage(img2)
fly = Label(window, image = bg2)
fly.place(x = 0, y = 430)

player_entrys = []
def generate(size):
    for i in range(size):
        player = Label(window, text = 'Player' + str(i+1).zfill(2))
        player.place(x = 0, y = i * 20)
        player_string = StringVar()
        player_entrys.append(Entry(window, width=20, textvariable = player_string))
        player_entrys[i].place(x = 60, y = i * 20)

def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


def shuffle():
    players = [entry.get() for entry in player_entrys]
    players = list(filter(lambda x: x != '', players))
    teamA = random.sample(players, k = len(players) // 2)
    teamB = Diff(players, teamA)
    outputA.config(text = 'teamA: ' + ', '.join(teamA))
    outputB.config(text = 'teamB: ' + ', '.join(teamB))

size = 10
outputA = Label(window, text = '')
outputB = Label(window, text = '')
outputA.place(x = 0, y = (size + 2) * 20)
outputB.place(x = 0, y = (size + 4) * 20)

generate(10)
button = Button(window, text = 'Shuffle', command = shuffle)
button.place(x = 80, y = size * 20 + 5)


window.mainloop()
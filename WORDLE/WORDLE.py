﻿import random
from tkinter import *



# Открытие файла
with open("C:/Users/Kyrylo/source/repos/NewRepo-master/WORDLE_/wordList.txt", 'r') as f:
    mylist = list(f)

wordList = [] #содержит список всех допустимых слов

for words in mylist:
    wordList.append(words.strip())


genList = list((random.choice(wordList)).upper()) #содержит слово из списка, которое нужно отгадать
finalWord = ''.join(genList).capitalize()
print(genList)



# def для проверки наличия слова в списке слов
def presentInList(word):
    if(word in wordList):
        return True
    return False

#def для проверки того, имеет ли слово длину в 5 букв
def isValid(word):
    if len(word) == 5 and presentInList(word):      
        return True
    return False

# def для изменение подзаголовка на «введите слово», «вы проиграли», «вы выиграли»
inputCounter=0
name="User"

def change_heading():
    global inputCounter, name
    check_word = inputBox.get()

    if inputCounter == 0:
        name = inputBox.get()
        subLabel.config(text=name + " ! Enter your Guess word")
        inputCounter += 1
        inputBox.delete(0, 'end') #Очистка поля ввода после каждой записи
    elif inputCounter == 6 and isValid(check_word):
        subLabel.config(text="YOU LOST! The word was "+ finalWord,bg=black,fg=red)
        enterButton.config(DISABLED)
        inputBox.delete(0, 'end') #Очистка поля ввода после каждой записи
    elif isValid(check_word):
        subLabel.config(text=name + " ! Enter your Guess word",bg=black,fg=orange)
        inputCounter += 1
        inputBox.delete(0, 'end') #Очистка поля ввода после каждой записи
    elif len(check_word )!= 5:
         subLabel.config(text="Must be a 5 letter word!",bg=black,fg=red)
         inputBox.delete(0, 'end')
    else:
        subLabel.config(text="Word not found in wordlist. Enter another word!",bg=black,fg=red)
        inputBox.delete(0, 'end') #Очистка поля ввода после каждой записи


# def для обновления полей для букв
def updateLabels(inputWord):
    inputWord = inputWord.strip().upper()
    userList = list(inputWord)

    for col in range(5):
        exec(f"label_{inputCounter - 1}_{col}.config(text=inputWord[col])")

        if userList[col] == genList[col]:
            exec(f"label_{inputCounter - 1}_{col}.config(bg=box_green,fg=white)")
        elif userList[col] in genList:
            exec(f"label_{inputCounter - 1}_{col}.config(bg=box_blue,fg=white)")
        else:
            exec(f"label_{inputCounter - 1}_{col}.config(bg=box_grey,fg=white)")


#def для заупска игры заново
def replay_game():
    global inputCounter, name, genList, finalWord
    # сбросс переменных
    inputCounter = 0
    name = "User"
    genList = list((random.choice(wordList)).upper())  # генерация нового слова 
    print(genList)
    finalWord = ''.join(genList).capitalize()
    # сброс надписей
    for row in range(6):
        for col in range(5):
            exec(f"label_{row}_{col}.config(text='', bg=box_bg)")
    # Сбросить поле ввода и заголовка
    inputBox.delete(0, 'end')
    subLabel.config(text="Enter Player Name", bg=black, fg=white)
    # Включить кнопку ENTER
    enterButton.config(state="normal")


def allFunctions(inputWord):
    global inputCounter

    if inputCounter in range(1, 8) and isValid(inputWord):
        updateLabels(inputWord)

    change_heading()
    winCheck(list(inputWord.upper()))  



#def для победителя
def winCheck(userList):
    global inputCounter,name
    if userList == genList:
        subLabel.config(text="CONGRATULATIONS! YOU WON",bg=black,fg=green)#Изменил цвет на зеленый
        enterButton.config(state="disabled")


# Пользовательский интерфейс игры Wordle
box_green = "#79B851"
box_blue = "#0000FF"
box_grey = "#A4AEC4"

orange='#fa8128'
green="#00fc00"
black = "#15141A"
blue="#0000FF"
red = "#AB202A"
white = "#FFFFFF"
grey="#335155"
purple="#8B00FF"

my_font="Roboto"

# Метки, содержащие каждую букву слова
box_width = 2
box_height = 1
box_borderwidth = 1
box_relief = "solid"
box_bg = "#335155"
box_fg = "#FFFFFF"
box_font = ("Roboto", 20)


root = Tk()
root.title("Wordle Game")
root.config(background=black)
 
wordleLabel = Label(root,text = "WELCOME WORDLE",font=(my_font,50),bg=black,fg=white)
wordleLabel.pack(pady=5)

subLabel = Label(root,text="Enter Player Name",font=(my_font,20),bg=black,fg=purple)
subLabel.pack(pady=5)

inputBox = Entry(root, font=(my_font,10),borderwidth="3",relief="flat",bg=grey,fg=white)
inputBox.pack(pady=10)

enterButton = Button(root,font=(my_font, 16),text="Submit", command=lambda:allFunctions(inputBox.get()),bg=blue,fg=black)
enterButton.pack(pady=10)





x_start = 250  # x-координата меток
y_start = 300  # y-координата меток

for row in range(6):
    ybox = y_start + row * 50
    for col in range(5):
        xbox = x_start + col * 40
        text = " "
        
        exec(f"label_{row}_{col} = Label(root, borderwidth=box_borderwidth, relief=box_relief, bg=box_bg, fg=box_fg,height=box_height, width=box_width, text=text, font=box_font)")
        exec(f"label_{row}_{col}.place(x=xbox, y=ybox)")

replayButton = Button(root, font=(my_font, 12), text="Replay", command=replay_game, bg="blue", fg="black")
replayButton.pack(side=LEFT,padx=[240,10], pady=20, anchor=S) 


root.geometry("700x675")
root.resizable(False,False)


root.mainloop()











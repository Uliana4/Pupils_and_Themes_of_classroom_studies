import os
from tkinter import *

class Pupils:
    def __init__(self,name):
        self.name = name
        self.count_one= []
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setCount_one(self, count_one):
        self.count_one.append(count_one)

class Themes:
    def __init__(self, theme, date):
        self.theme = theme
        self.date = date
    def setTheme(self, theme):
        self.theme = theme
    def getTheme(self):
        return self.theme
    def setDate(self, date):
        self.date = date
    def getDate(self):
        return self.date

# Sprawdzam, czy określona ścieżka (pupils) jest istniejącym katalogiem, czy nie. Jeżeli katalog "pupils" nie istnieje, to os.mkdir pozwala na jrgp stworzenie 
if not os.path.isdir("pupils"):
    os.mkdir("pupils")
if not os.path.isdir("themes"):
    os.mkdir("themes")

# Os.listdir zwraca listę wszystkich plików i podkatalogów w katalogu pupils 
lista = os.listdir(("./pupils"))
print(lista)
lista_Pupils=[]
for i in lista:
    f = open(f'./pupils/{i}', 'r')
    array = f.read().split('\n')
    object = Pupils(array[0])
    object.count_one=array[1].split()
    lista_Pupils.append(object)
    print(object.getName())

lista_1 = os.listdir(("./themes"))
print(lista_1)
lista_Themes = []
for i in lista_1:
    f = open(f'./themes/{i}', 'r')
    array = f.read().split('\n')
    object = Themes(array[0], array[1])
    lista_Themes.append(object)


root = Tk()

entry = Entry(width=20, font="Arial 27")
b1 = Button(text="add pupil", font="Arial 27")
b2 = Button(text="add theme", font="Arial 27")
l1 = Listbox(width=20, font="Arial 27")
l2 = Listbox(width=20, font="Arial 27")

# Zapełniam katalog "Pupils" i dodaje "\n", aby nowy uczeń był wyświetlany w następnym wierszu
def completion_pupils(event):
    s = entry.get()
    object = Pupils(s)
    lista_Pupils.append(object)
    l1.insert(END, object.getName())
    f = open(f"./pupils/{s.replace(' ', '_')}.txt", "w")
    s_add = s + '\n'
    f.write(s_add)
    f.close()

# Zapełniam katalog "Themes" w taki sposób, aby buł wyświetlony temat oraz dodaje "\n", aby data tego tematu została wyświetlona w następnym wierszu
def completion_themes(event):
    s = entry.get().split()
    object = Themes(s[0], s[1])
    lista_Themes.append(object)
    l2.insert(END, object.getTheme())
    f = open(f"./themes/{s[0]}.txt", 'w')
    s_add = s[0] + '\n' + s[1]
    f.write(s_add)
    f.close()

def enhance(event):
    global lista_Pupils
    imie_nazwisko = l1.curselection()[0]
    imie_nazwisko = l1.get(imie_nazwisko)
    print(imie_nazwisko)
    object = ''
    for i in lista_Pupils:
        if imie_nazwisko == i.getName():
            object = i
            break
    print(object.getName())

    root_1 = Tk()
    label = Label(root_1, width=30)
    label['text'] = object.getName()
    entry_1 = Entry(root_1, width=30)
    entry_1.insert(0,','.join(object.count))
    button = Button(root_1, text='add')
    label.pack()
    entry_1.pack()
    button.pack()

    def enhance_one(event):
        object.count_one = entry_1.get().split(',')
        for i in lista_Pupils:
            if object.getName() == i.getName():
                i.count_one = object.count_one
                arr = os.listdir('./pupils')
                for i in arr:
                    if i.replace('_', ' ').startswith(object.getName()):
                        f = open(f"./pupils/{i}", 'w')
                        f.write(object.getName() + '\n' + ' '.join(object.count_one))
                        f.close()
    button.bind('<Button-1>', enhance_one)
    root_1.mainloop()

for i in lista_Pupils:
    l1.insert(END, i.getName())
for i in lista_Themes:
    l2.insert(END, i.getTheme())

l1.bind('<Double-Button-1>', enhance)
b1.bind('<Button-1>', completion_pupils)
b2.bind('<Button-1>', completion_themes)
entry.grid(row = 1, column = 2)
b1.grid(row = 2, column = 2)
b2.grid(row = 3, column = 2)
l1.grid(row = 1, column = 1)
l2.grid(row = 1, column = 3)
root.mainloop()

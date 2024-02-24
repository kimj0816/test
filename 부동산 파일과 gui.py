from tkinter import *
import csv, os

    
class App:
    def __init__(self):
        
        self.window = Tk()
        self.window.title("집 찾기")
        self.window.geometry('800x400+100+100')

        self.entry = Entry(self.window)
        self.entry.pack()

        self.button = Button(self.window,text = '검색', command = self.Home)
        self.button.pack()

        self.label = Label(self.window)
        self.label.pack()

        self.window.mainloop()

    def Home(self):
        os.chdir(r'C:/Users/datak/OneDrive/바탕 화면')
        f = open('sample_data.csv', 'r')
        data_1 = csv.reader(f)
        data_2 = [i for i in data_1]
        re = 0
        for i in range(1,986):
            if data_2[i][9] >= (self.entry.get()) :
                re += 1
        self.label.configure(text = "결과 값 = " + str(re))

App()









from tkinter import *
import os
from PhoneAndEmailScrapper import *

root = Tk()
root.title('Phone&Emails Scrapper')
etcObj = extraction()

def clearSourcePath():
    sourcePath.delete(0, END)
    sourcePath.insert(0,"")

def scrapData():
    getSourcePath = sourcePath.get()
    etcObj.extractContent(getSourcePath)

# row 0
sourcePathLabel = Label(root, text='Source Path: ')
sourcePathLabel.grid(row = 0, column = 0, padx = 10, pady = 10)
sourcePath = Entry(root)
sourcePath.grid(row = 0, column = 1, ipadx = 200, padx = 10, pady = 15)

ScrapData = Button(root, text = "Scrap", command = scrapData)
ScrapData.grid(row = 0, column = 2, padx = 5)

clearUserEntryPath = Button(root, text = "Clear", command = clearSourcePath)
clearUserEntryPath.grid(row = 0, column = 3, padx = 10)

#row 1
resultPathLabel = Label(root, text='Result Path: ')
resultPathLabel.grid(row = 1, column = 0, padx = 10, pady = 10)
resultDirectory = os.getcwd() + "\\" + 'PhoneNoAndEmail_RESULT.txt'

setResultDirectory = StringVar(root, resultDirectory)
resultPath = Entry(root, textvariable=setResultDirectory)

resultPath.grid(row = 1, column = 1, ipadx = 200, padx = 10, pady = 15)

#row 2
message = Text(root, width = 90, height = 10 )
message.grid(row = 2, columnspan = 5, rowspan = 5, pady = 15)


root.mainloop()
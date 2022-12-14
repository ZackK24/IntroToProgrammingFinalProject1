# Zack K
# Sources and Overview of the Project.
# https://www.youtube.com/watch?v=IbpInH4q4Sg&list=LL&index=1&t=390s
# Course Code Files Day 30 Exercise
# https://www.youtube.com/watch?v=wFyzmZVKPAw

'''
This code will tell you what the projected price of a home would be based of the 
user's input of the the home
'''
# Pandas is a library which reads and analyzes excel spreadsheets
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import Entry
# Draws the Tkinter window
# Analyze the pdf file which tells the info of houses and gives a sample of the homes.
homesdata = pd.read_excel("HomeData.xlsx")
print(homesdata.head())

# Draws the Tkinter window
win = Tk()
win.title("Home Price Predictor")
win.geometry("1000x500")
PRICE = int()
POINTS = int
# Creating the category variables
Price = PRICE
Price = int(0)
Points = POINTS
Points = int(0)
# Creates the label variable
frame = Frame(win)
frame1 = Frame(win)
frame.pack()
frame1.pack()
page1 = Frame(frame)
page1.pack(pady=20)
page2 = Frame(frame1)
page2.pack(pady=20)
page1label = Label(page1, text = "Welcome to Home Price Predictors! Would You like to see some sample data?") 
page1label.pack()
page2label = Label(page2, text = "Enter your home's characteristics:")
tableentry = Label(page1, text = homesdata.head(5))
# Creates the entries that are on page 2
pages = [page1, page2]
count = 0
def nextclick():
   global count

   if not count > len(pages):
   
      for p in pages:
         p.pack_forget()
      count += 1
      page = pages[count]
      page.pack(pady = 20)
   page2label.pack()
   Bath.pack()
   Bed.pack()
   Condition.pack()
   Pool.pack()
   Year.pack()
   Size.pack()
   estimatebutton.pack(pady=10)
   Bath.insert(INSERT, "Bathroom # ")
   Bed.insert(INSERT, "Bedroom # ")
   Condition.insert(INSERT, "Condition (out of 10): ")
   Pool.insert(INSERT, "Pool? ")
   Year.insert(INSERT, "When was it built? ")
   Size.insert(INSERT, "What is the size of your home? ")
def backclick():
   global count

   if not count == 0:
   
      for p in pages:
         p.pack_forget()
      count -= 1
      page = pages[count]
      page.pack(pady = 20)
def yesclick():
   tableentry.pack()

# Creates the buttons
yesbutton = Button(page1, text = "Yes!", command = yesclick)
backbutton = Button(win, text = "Back", command = backclick)
nextbutton = Button(win, text = "Next", command = nextclick)
backbutton.pack()
nextbutton.pack()
yesbutton.pack()
Bath = Entry(page2, width= 40)
Bed = Entry(page2, width = 40)
Condition = Entry(page2, width = 40)
Pool = Entry(page2, width = 40)
Year = Entry(page2, width = 40)
Size = Entry(page2, width = 40)


# Defines the function of when the button is clicked
def estimation():
# Converts the entries into integers
   try:
      int(Bath.get())
      int(Bed.get())
      int(Condition.get())
      int(Year.get())
      int(Size.get())
   except ValueError:
      print("Invalid answer...")
   PRICE = int()
   POINTS = int()
   if Pool == "Yes" or Pool == "yes":
      POINTS += 2
   else:
      POINTS +=0
   if Condition < 3:
      POINTS += 1
   elif Condition > 4 and Condition < 7:
      POINTS += 2
   elif Condition > 7:
      POINTS += 3
# Will ask for how many bathrooms there are and will use the input to assign how many qualtiy points their hoem gets.
   if Bath == 0:
      POINTS += 0
   elif Bath == 1:
      POINTS += 1
   elif Bath > 1 and Bath < 5:
      POINTS += 2
   elif Bath > 4:
      POINTS += 3
# Processes the the user input of how many bedrooms 
   if Bed == 0:
      POINTS += 0
   elif Bed > 0 and Bed < 3:
      POINTS += 1
   elif Bed > 2 and Bed < 6:
      POINTS += 2
   elif Bed > 5:
      POINTS += 3
# Takes in the user input as a string value and will add points if it matches with the string value
   if Pool == "Yes" or Pool == "yes":
      POINTS += 2
   else:
      POINTS +=0
# Asks for the age of the home and adds points to the corresponding answer
   if Year < 1950:
      POINTS += 0
   elif Year > 1949 and Year < 1965:
      POINTS += 1
   elif Year > 1954 and Year < 1980:
      POINTS += 2
   elif Year > 1979 and Year < 1995:
      POINTS += 3
   elif Year > 1994:
      POINTS += 4
# User inputs the size of the gome and points are added based off user input.
   if Size < 1500:
      POINTS += 1
   elif Size > 1499 and Size < 2500:
      POINTS += 2
   elif Size > 2499 and Size < 3000:
      POINTS += 3
   elif Size > 2999 and Size < 3500:
      POINTS += 4
   elif Size > 3499 and Size < 4000:
      POINTS += 5
   else: 
      POINTS += 6
# Will then give the Quality score of the home after the questions.
# Will use the amount of Quality Points to then estimate how long much the hoem will cost.
   if POINTS == 0:
      PRICE += 0
   elif POINTS > 0 and POINTS < 6:
      PRICE += 250000
   elif POINTS > 5 and POINTS < 11:
      PRICE += 400000
   elif POINTS > 10 and POINTS < 16:
      PRICE += 550000
   elif POINTS > 15 and POINTS < 21:
      PRICE += 700000
   elif POINTS > 20:
      PRICE += 825000
   Points = ("Your Home Quality Score is: " + str(POINTS) + " Points!")
   Price = ("Your Home Price is:" + str(PRICE) + " dollars!")
   label2 = Label(frame, text = Points, font = ('Times New Roman', 14, 'italic'))
   label3= Label(frame, text= Price, font= ('Times New Roman', 14, 'italic'))
   label2.pack(pady = 30)
   label3.pack(pady=30)
estimatebutton = ttk.Button(page2, text= "Estimate!", command = estimation)
win.mainloop()



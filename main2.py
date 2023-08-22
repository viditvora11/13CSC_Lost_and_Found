from tkinter import *  #importing fies from tkinter
from PIL import Image, ImageTk #Importing PIL for use of image
global item_list #allowing to list to be global so it can be used out of the list
item_list = [] #Items can be stored in this list
line_list = [] 
from tkinter import messagebox #importing message box to display error messages

#########CLASS HOME START#########
class Home: #Class used for home page to subclassify the code
    def __init__(self, parent): #Used to internalize the code

        self.img_file = Image.open("lost.png") #Open Lost button image
        self.img_file = self.img_file.resize((130,70)) #Resize lost image
        self.img_file = ImageTk.PhotoImage(self.img_file) #Used to show image with tkinter label

        self.b1 = Button(parent,image=self.img_file, border = 0, highlightthickness=0, command = self.lost) #Making the image a button
        self.b1.place(x=0,y=255) #Placing the button on a cordinate

        self.img_file1 = Image.open("exit.png")#Open Exit button image
        self.img_file1 = self.img_file1.resize((110,60)) #Resize exit button
        self.img_file1 = ImageTk.PhotoImage(self.img_file1) #Used to show image with tkinter label

        self.b2 = Button(parent,image=self.img_file1, border = 0, highlightthickness=0, command = self.exit) #Making the image a button
        self.b2.place(x=220,y=539)#Placing the button on a cordinate

        self.img_file2 = Image.open("found.png")#Open Found button image
        self.img_file2 = self.img_file2.resize((170,74)) #Resize exit button
        self.img_file2 = ImageTk.PhotoImage(self.img_file2) #Used to show image with tkinter label

        self.b3 = Button(parent,image=self.img_file2, border = 0, highlightthickness=0, command = self.found) #Making the image a button
        self.b3.place(x=430,y=255)#Placing the button on a cordinate
      
    def exit(self): #Define Exit command 
      window.destroy() #destroy the program
  
    def lost(self): #Define Lost command
      self.b1.place_forget()#Forget button
      self.b2.place_forget()#Forget button
      self.b3.place_forget()#Forget button
      Lost(window)#Open class Lost

    def found(self): #Define Found command
      self.b1.place_forget()#Forget button
      self.b2.place_forget()#Forget button
      self.b3.place_forget()#Forget button
      Found(window)#Open class Found
#########CLASS HOME END###########

#########CLASS LOST START#########      
class Lost: #Class used for Lost page to subclassify the code
    def __init__(self, parent): #Used to internalize the code

      
        bg_image2 = Image.open("back2.png") #Open background image
        bg_image2 = bg_image2.resize((600,600)) #Resize the backgroud image
        bg_image2 = ImageTk.PhotoImage(bg_image2) #Used to show image with tkinter label
        image_label.configure(image = bg_image2) #Configue the image
        image_label.image=bg_image2 #Label th image

      
        self.w_label = Label(window, font=('Arial 20')) #Adding label
        self.w_label.place(x=10,y=100) #Resize the label

        inputFile = open("Item_entry.txt", "r") #Open the Item list file
        lineList = inputFile.readlines() #Read items from the file into line list
        
        for item in lineList: #Each item in line list
          item_list.append(item) #Print all items

        lost_string = "" #Adding blank space
        for i in range(len(item_list)):#items in item list
            lost_string +="{}\n".format(item_list[i]) #
        print(lost_string)#for testing to show on the console
        self.w_label.config(text=lost_string) 
        inputFile.close()
  
        self.img_file1 = Image.open("exit.png")
        self.img_file1 = self.img_file1.resize((110,70))
        self.img_file1 = ImageTk.PhotoImage(self.img_file1)

        self.b3 = Button(window,text = "Back",font = ('Eczar 20'), command = self.exit1, bg = '#38b6ff')
        
        self.b3.place(x=0,y=550)

    def exit1(self):
        self.b3.place_forget()
        self.w_label.place_forget()
        item_list.clear()
        Home2(window)
##########CLASS LOST END###########

#########CLASS FOUND START#########
class Found:
    def __init__(self, parent):
        bg_image3 = Image.open("back3.png") 
        bg_image3 = bg_image3.resize((600,600))
        bg_image3 = ImageTk.PhotoImage(bg_image3) 
        image_label.configure(image = bg_image3) 
        image_label.image=bg_image3 

        self.item_entry=Entry(window,width=10, font=('Arial 20'))
        self.item_entry.place(x=200, y=200)
        self.continue_button = Button(window, text="Continue", font=("Helvetica", "11", "bold"), bg="orange", command = self.item_name_collection)

        self.continue_button.place( x=275, y=250) 

        self.img_file1 = Image.open("exit.png")
        self.img_file1 = self.img_file1.resize((110,60))
        self.img_file1 = ImageTk.PhotoImage(self.img_file1)

        self.b4 = Button(window,text = "Back",font = ('Eczar 20'), border = 0, highlightthickness=0, command = self.exit1, bg = 'orange')
        self.b4.place(x=0,y=550)

    def exit1(self):
        self.b4.place_forget()
        self.item_entry.place_forget()
        self.continue_button.place_forget()
        Home2(window)

    def item_name_collection(self):
        if self.item_entry.get() == "" or len(self.item_entry.get()) <= 12:
            file = open("Item_entry.txt", "a")
            file.write(self.item_entry.get()+"\n")
            self.continue_button.place_forget()
            self.b4.place_forget()
            self.item_entry.place_forget()
            Home2(window)
        else:
            messagebox.showinfo("Blank answer", "Item entry can't be left blank or greater than 12 characters")
            Found(window)
##########CLASS FOUND END##########

#########CLASS HOME2 START#########
class Home2:
    def __init__(self, parent):

        self.img_file = Image.open("lost.png")
        self.img_file = self.img_file.resize((130,70))
        self.img_file = ImageTk.PhotoImage(self.img_file)

        self.b1 = Button(parent,image=self.img_file, border = 0, highlightthickness=0, command = self.lost)
        self.b1.place(x=0,y=255)

        self.img_file1 = Image.open("exit.png")
        self.img_file1 = self.img_file1.resize((110,60))
        self.img_file1 = ImageTk.PhotoImage(self.img_file1)

        self.b2 = Button(parent,image=self.img_file1, border = 0, highlightthickness=0, command = self.exit)
        self.b2.place(x=220,y=539)

        self.img_file2 = Image.open("found.png")
        self.img_file2 = self.img_file2.resize((170,74))
        self.img_file2 = ImageTk.PhotoImage(self.img_file2)

        self.b3 = Button(parent,image=self.img_file2, border = 0, highlightthickness=0, command = self.found)
        self.b3.place(x=430,y=255)

        bg_image2 = Image.open("back.png") 
        bg_image2 = bg_image2.resize((600,600))
        bg_image2 = ImageTk.PhotoImage(bg_image2) 
        image_label.configure(image = bg_image2) 
        image_label.image=bg_image2

        self.items_frame = Frame(window)
        self.items_frame.grid(padx = 50, pady = 50)


    def exit(self):
      window.destroy()
  
    def lost(self):
      self.b1.place_forget()
      self.b2.place_forget()
      self.b3.place_forget()
      Lost(window)

    def found(self):
      self.b1.place_forget()
      self.b2.place_forget()
      self.b3.place_forget()
      Found(window)
##########CLASS HOME2 END##########

  
      
if __name__== "__main__": 
    window = Tk()
    window.title("Lost and Found MRGS")
    window.geometry("600x600")
    bg_image = Image.open("back.png")
    bg_image = bg_image.resize((600,600))
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Home(window)

    window.mainloop()

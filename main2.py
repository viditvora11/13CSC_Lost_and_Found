#Import items
from tkinter import *  #importing fies from tkinter
from PIL import Image, ImageTk #Importing PIL for use of image
from tkinter import messagebox #importing message box to display error messages

global item_list #allowing to list to be global so it can be used out of the list

item_list = [] #Items can be stored in this list
line_list = []

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
      self.login_window = LoginWindow() #Open class login
#########CLASS HOME END###########

#########CLASS LOST START#########      
class Lost: #Class used for Lost page to subclassify the code
    listbox = None
    
    def __init__(self, parent): #Used to internalize the code
        bg_image2 = Image.open("back2.png") #Open background image
        bg_image2 = bg_image2.resize((600,600)) #Resize the backgroud image
        bg_image2 = ImageTk.PhotoImage(bg_image2) #Used to show image with tkinter label
        image_label.configure(image = bg_image2) #Configue the image
        image_label.image=bg_image2 #Label the image
        
        inputFile = open("Item_entry.txt", "r") #Open the Item list file
        lineList = inputFile.readlines() #Read items from the file into line list
        
        for item in lineList: #Each item in line list
          item_list.append(item) #Print all items

        lost_string = "" #Adding blank space
        for i in range(len(item_list)):#items in item list
            lost_string +="{}\n".format(item_list[i]) #Adding items from the list and adding the next item on a new line
        self.listbox = Listbox(font=('Eczar 27'), justify = "center")
        self.listbox.place(x=100, y=100)
        for i in range(len(item_list)):#items in item list #Adding items from the list and adding the next item on a new line
            self.listbox.insert(0, item_list[i])
        inputFile.close() #Close item list 

        self.b3 = Button(window,text = "Back",font = ('Eczar 20'), command = self.exit1, bg = '#38b6ff') #Back button
        
        self.b3.place(x=0,y=550) #place back button

    def exit1(self): #Define back button 
        self.b3.place_forget() #Forget b3
        self.listbox.place_forget() #forget label
        item_list.clear() #Clear item list
        Home2(window) #Run home 2
##########CLASS LOST END###########

#########CLASS FOUND START#########
class Found: #Class used for Found page to subclassify the code
    def __init__(self, parent): #Used to internalize the code
        bg_image3 = Image.open("back3.png") #Open background image
        bg_image3 = bg_image3.resize((600,600)) #Resize background image
        bg_image3 = ImageTk.PhotoImage(bg_image3) #Used to show image with tkinter label
        image_label.configure(image = bg_image3) #Configue the image
        image_label.image=bg_image3 #Label the image

        self.item_entry=Entry(window,width=10, font=('Arial 20')) #Item entry window
        self.item_entry.place(x=225, y=200) #Place item entry
        self.continue_button = Button(window, text="Continue", font=("Helvetica", "11", "bold"), bg="orange", command = self.item_name_collection) #Continue button

        self.continue_button.place( x=300, y=250) #Place continue button

        self.b4 = Button(window,text = "Back",font = ('Eczar 20'), border = 0, highlightthickness=0, command = self.exit1, bg = 'orange')#Back button config
        self.b4.place(x=0,y=550)#Place back button

    def exit1(self):#define Back button
        self.b4.place_forget()#Forget b4
        self.item_entry.place_forget() #Forget item entry
        self.continue_button.place_forget() #Forget continue button
        Home2(window) #Open home2

    def item_name_collection(self): #Define item name collection
        if len(self.item_entry.get()) >= 1 and len(self.item_entry.get()) <= 12: #If entry is empty or more than 12 do not allow
            file = open("Item_entry.txt", "a") #Append items in item entry 
            file.write(self.item_entry.get()+"\n") #Write in item entry
            self.continue_button.place_forget() #Forget continue button
            self.b4.place_forget() #Forget b4
            self.item_entry.place_forget() #Forget entry box
            Home2(window) #Open home2
        else:
            messagebox.showinfo("Blank answer", "Item entry can't be left blank or greater than 12 characters") #If blank or more than 12 charachers show error message
            pass #Continue on found page
##########CLASS FOUND END##########

#####CLASS LOGIN WINDOW START######
class LoginWindow(): #Class used for Login Window page to subclassify the code

    login_window = None 

    def __init__(self): #Used to internalize the code
        self.login_window = Tk() #Opening a new window for login
        self.login_window.title("Teachers Login") #Lable new window
        self.login_window.geometry('600x600') #Resize the login page to 600 x 600
        self.login_window.configure(bg='#00008B') #Background colour

        frame = Frame(self.login_window, bg='#00008B') #Frame colour selection

        login_label = Label(frame, text="MRGS TEACHERS LOGIN", bg='#00008B', fg="#FFFFFF", font=("Arial", 30)) #Page text config
        username_label =  Label(frame, text="Username", bg='#00008B', fg="#FFFFFF", font=("Arial", 16, 'bold')) #username text
        password_label =  Label(frame, text="Password", bg='#00008B', fg="#FFFFFF", font=("Arial", 16, 'bold')) #Password text 

        self.username_entry =  Entry(frame, font=("Arial", 16)) #Entry box for username 
        self.password_entry =  Entry(frame, show="*", font=("Arial", 16)) #Entry box for password

        login_button =  Button(frame, text="Login", bg="#DC143C", fg="#FFFFFF", font=("Arial", 16), command=self.login) #Login button to check username and password validation

        login_label.grid(row=0, column=0, columnspan=3, sticky="news", pady=40) #Place login button
        username_label.grid(row=1, column=0) #Place username label
        self.username_entry.grid(row=1, column=1, pady=20) #Adding padding
        password_label.grid(row=2, column=0) #Place password lablel
        self.password_entry.grid(row=2, column=1, pady=20)#Adding padding
        login_button.grid(row=3, column=1, columnspan=4, pady=30) #Adding login button padding

        frame.pack() #Pack the frame and place the frame on the window

    def login(self): #Define the password and username 
        username = "VIDIT" #Username 
        password = "MRGS" #Password

        if self.username_entry.get()==username and self.password_entry.get()==password: #If password and username match
            Found(window) #Open found window
            self.login_window.destroy() #Destroy the login window if the password and username are correct
        else: # If password and username do not macth
            messagebox.showerror(title="Error", message="The password or the username do not match. Make sure the text is not in lower case") #Show error message 
#######CLASS LOGIN WINDOW END######

#########CLASS HOME2 START#########
class Home2: #Class used for Home2 page to subclassify the code
    def __init__(self, parent): #Used to internalize the code

        self.img_file = Image.open("lost.png") #Open Lost button image
        self.img_file = self.img_file.resize((130,70))#Resize lost image
        self.img_file = ImageTk.PhotoImage(self.img_file) #Used to show image with tkinter label

        self.b1 = Button(parent,image=self.img_file, border = 0, highlightthickness=0, command = self.lost)  #Making the image a button
        self.b1.place(x=0,y=255) #Placing the button on a cordinate

        self.img_file1 = Image.open("exit.png") #Open Exit button image
        self.img_file1 = self.img_file1.resize((110,60)) #Resize exit button
        self.img_file1 = ImageTk.PhotoImage(self.img_file1) #Used to show image with tkinter label

        self.b2 = Button(parent,image=self.img_file1, border = 0, highlightthickness=0, command = self.exit) #Making the image a button
        self.b2.place(x=220,y=539)#Placing the button on a cordinate

        self.img_file2 = Image.open("found.png")#Open Found button image
        self.img_file2 = self.img_file2.resize((170,74))#Resize exit button
        self.img_file2 = ImageTk.PhotoImage(self.img_file2)#Used to show image with tkinter label

        self.b3 = Button(parent,image=self.img_file2, border = 0, highlightthickness=0, command = self.found) #Making the image a button
        self.b3.place(x=430,y=255)#Placing the button on a cordinate

        bg_image2 = Image.open("back.png") #Open backgroud image
        bg_image2 = bg_image2.resize((600,600)) #Resize image
        bg_image2 = ImageTk.PhotoImage(bg_image2) #Label image
        image_label.configure(image = bg_image2) #Config image
        image_label.image=bg_image2 #Image = bg_image2

        self.items_frame = Frame(window) #Frame on window
        self.items_frame.grid(padx = 50, pady = 50) #place frame


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
      self.login_window = LoginWindow() #Open class login
##########CLASS HOME2 END##########

##########Main Code Start##########
if __name__== "__main__": 
    window = Tk() #window as tk
    window.title("Lost and Found MRGS") #Window title
    window.geometry("600x600") #Resize frame
    bg_image = Image.open("back.png") #Background image
    bg_image = bg_image.resize((600,600))#Resize background image 
    bg_image = ImageTk.PhotoImage(bg_image) #Label image
    image_label= Label(window, image=bg_image) #Config image
    image_label.place(x=0, y=0, relwidth=1, relheight=1) #Place label
    start_object = Home(window) #Run home on window

    window.mainloop() #Window will run in the main loop
##########Main Code END############

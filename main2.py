from tkinter import *
from PIL import Image, ImageTk
global item_list
item_list = []
line_list = []


class Home:
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

    def room(self):
      Room(window)



      
class Lost:
    def __init__(self, parent):

      
        bg_image2 = Image.open("back2.png") 
        bg_image2 = bg_image2.resize((600,600),Image.ANTIALIAS)
        bg_image2 = ImageTk.PhotoImage(bg_image2) 
        image_label.configure(image = bg_image2) 
        image_label.image=bg_image2

      
        self.w_label = Label(window, font=('Arial 20'))
        self.w_label.grid(pady=10,padx=5)

        inputFile = open("Item_entry.txt", "r")
        lineList = inputFile.readlines()
        
        for item in lineList:
          item_list.append(item)

        lost_string = ""
        for i in range(len(item_list)):
            lost_string +="{}\n".format(item_list[i])
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
        self.w_label.grid_remove()
        item_list.clear()
        Home2(window)





class Found:
    def __init__(self, parent):

            
        bg_image3 = Image.open("back3.png") 
        bg_image3 = bg_image3.resize((600,600),Image.ANTIALIAS)
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

        file = open("Item_entry.txt", "a")
        file.write(self.item_entry.get()+"\n")
        self.continue_button.place_forget()
        self.b4.place_forget()
        self.item_entry.place_forget()
        Home2(window)  




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
        bg_image2 = bg_image2.resize((600,600),Image.ANTIALIAS)
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


  
      
if __name__== "__main__": 
    window = Tk()
    window.title("Lost and Found MRGS")
    window.geometry("600x600")
    bg_image = Image.open("back.png")
    bg_image = bg_image.resize((600,600),Image.ANTIALIAS)
    bg_image = ImageTk.PhotoImage(bg_image)
    image_label= Label(window, image=bg_image)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    start_object = Home(window)

    window.mainloop()

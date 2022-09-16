from cgitb import text
from email.mime import image
import tkinter
from tkinter import font
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):

    WIDTH = 900
    HEIGHT = 600  

    def __init__(self):
        super().__init__()

        self.title("Enigma Tester")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ============ create two frames ============
       
       
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_left = customtkinter.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")
        self.frame_center = customtkinter.CTkFrame(master=self)
        self.frame_center.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        
        
        
        # ============ Description ===========
        
        self.frame_info = customtkinter.CTkFrame(self.frame_center)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text=text="""  Enigma tester's purpose is to compare
                                                                the speed of famous encryption algorithms
                                                           like RSA and AES in order to optimise their usage""" ,
                                                   height=20,
                                                   corner_radius=6, 
                                                   fg_color=("white", "#363636"),
                                                   justify=tkinter.LEFT , text_font=("Calibri", 13 ))
        self.label_info_1.grid(column=0, row=0, sticky="nwse", padx=15, pady=15)
          
        
        ####
       
       
        self.frame_center.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_center.rowconfigure(7, weight=10)
        self.frame_center.columnconfigure((0, 1), weight=1)
        self.frame_center.columnconfigure(2, weight=0)
    
    
        # configure grid layout (1x11)
    
    
        self.frame_left.grid_rowconfigure(0, minsize=10)   
        self.frame_left.grid_rowconfigure(5, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)    
        self.frame_left.grid_rowconfigure(11, minsize=10)  


    
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                               text_font=("Calibri", 18 ),
                                            ) 
                                        
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        
        
        self.description_image = self.load_image("/home/aws/Desktop/projet-ensi/description.jpg", 30)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Description",
                                                command="",
                                                image=self.description_image
                                                ,text_font=("Calibri", 13 ))
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.test_image = self.load_image("/home/aws/Desktop/projet-ensi/test.jpg", 30)
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Testing",
                                                command="",
                                                image=self.test_image , text_font=("Calibri", 13 ))
        self.button_2.grid(row=5, column=0, pady=10, padx=20)
       
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")

        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============
        Description_Text=customtkinter.CTkTextbox()

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(-1)

        self.entry1 = customtkinter.CTkEntry(master=self.frame_center,
                                            width=120,
                                            placeholder_text="select file" , text_font=("Calibri", 13 ))
        self.entry1.grid(row=6, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.button_5 = customtkinter.CTkButton(master=self.frame_center,
                                                text="Start",
                                                border_width=2,  
                                                fg_color=None,
                                                command=self.button_event)
        
        self.button_5.grid(row=6, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.entry2 = customtkinter.CTkEntry(master=self.frame_center,
                                            width=90,
                                            placeholder_text="Choose RSA OR AES" , text_font=("Calibri", 13 ))
        self.entry2.grid(row=7, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        
        self.optionmenu_1.set("Dark")    
        
        
    def load_image(self, path, image_size):
        return ImageTk.PhotoImage(Image.open(path).resize((image_size, image_size))) 

    
    def button_event(self):
        '''
        size_of_file = os.path.getsize(self.entry1.get())
        self.label_size_of_file= customtkinter.CTkLabel(master=self.frame_right, 
                                                    text="The size of the current file is "+str(size_of_file) + " bytes")
        self.label_size_of_file.grid(row=9, column=1, pady=0, padx=20, sticky="w")
        '''
        os.system("python3 figure.py" +" "+ str(self.entry1.get()) + " " + str(self.entry2.get()))

    
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    
    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    

    

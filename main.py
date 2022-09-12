from email.mime import image
import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



class App(customtkinter.CTk):

    WIDTH = 1200
    HEIGHT = 800
    algorithm = False
    def __init__(self):
        super().__init__()

        self.title("Enigma Tester")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  


        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

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
                                                   text="Enigma tester is an application \n" +
                                                        "which is used to calculate the execution \n" +
                                                        "time of encryption algorithms " ,
                                                    text_font=('Arial',25),
                                                   height=20,
                                                   corner_radius=6,  # <- custom corner radius
                                                   fg_color=("white", "#363636"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwse", padx=15, pady=15)
          
        
        
        self.frame_center.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_center.rowconfigure(7, weight=10)
        self.frame_center.columnconfigure((0, 1), weight=1)
        self.frame_center.columnconfigure(2, weight=0)
        self.frame_left.grid_rowconfigure(0, minsize=10)   
        self.frame_left.grid_rowconfigure(5, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)   
        self.frame_left.grid_rowconfigure(11, minsize=10)  
    
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Menu",
                                              text_font=("Roboto Medium", -16),
                                            ) 
                                        
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        
        
        self.description_image = self.load_image("C:/Users/aayma/OneDrive/Bureau/Enigma-Tester-main/description.jpg", 30)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Description",
                                                command="",
                                                image=self.description_image)
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.test_image = self.load_image("C:/Users/aayma/OneDrive/Bureau/Enigma-Tester-main/test.jpg", 30)
        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Testing",
                                                command="",
                                                image=self.test_image)
        self.button_2.grid(row=5, column=0, pady=10, padx=20)
       
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")

        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        
        
        
      

        
        Description_Text=customtkinter.CTkTextbox()
        

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(-1)
        
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_center,
                                 variable=self.radio_var,value=1,text="AES")
        
        self.radio_button_1.grid(row=8, column=0, pady=5, padx=20, sticky="n")
        
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_center,
                                 variable=self.radio_var,value=0 ,text="RSA")
        
        self.radio_button_2.grid(row=8, column=1, pady=5, padx=20, sticky="n")

        self.entry = customtkinter.CTkEntry(master=self.frame_center,
                                            width=120,
                                            placeholder_text="select file")
        self.entry.grid(row=7, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_center,
                                                text="Start",
                                                border_width=2,  
                                                fg_color=None,
                                                command=self.button_event)
        
        self.button_5.grid(row=7, column=2, columnspan=1, pady=20, padx=20, sticky="we")
        self.optionmenu_1.set("Dark")   
        

    def load_image(self, path, image_size):
        return ImageTk.PhotoImage(Image.open(path).resize((image_size, image_size)))

    
    def button_event(self):
        size_of_file = os.path.getsize(self.entry.get())
        self.label_size_of_file= customtkinter.CTkLabel(master=self.frame_right, 
                                                    text="The size of the current file is "+str(size_of_file) + " bytes")
        self.label_size_of_file.grid(row=9, column=1, pady=0, padx=20, sticky="w")
        os.system("python3 figure.py" +" "+ str(self.entry.get()) + " " + str(self.algorithm))

    
    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    
    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

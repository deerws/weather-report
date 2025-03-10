import requests
import customtkinter
import customtkinter as ctk
from tkinter import PhotoImage

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.conf_windown_start()
        self.background()
        self.login_screen()

    def conf_windown_start(self):
        self.geometry("1000x450")
        self.title("Weather Report")
        self.resizable(False, False)

    def background(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    def login_screen(self):

        #Image
        self.img = PhotoImage(file="imageee.png")
        self.lb_img=ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.grid(row=50, column=0, padx=0)

        self.title = ctk.CTkLabel(self, text="Welcome to Channel 5 Weather Forecast", font=("Century Gothic bold",30))
        self.title.place(x=0, y=0)
        self.title.grid(row=0,column=0,pady=10,padx=10)

        #Forms
        self.frame_login = ctk.CTkFrame(self, width=400, height=300)
        self.frame_login.place(x=560, y=55)
        self.lb_title = ctk.CTkLabel(self.frame_login, text= "Enter your Username and Password", font=("Century Gothic bold",22),text_color='purple')
        self.lb_title.grid(row=0, column=0, padx=50,pady=50)

        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Username", font=("Century Gothic bold",15), corner_radius=15)
        self.username_login_entry.grid(row=1,column=0,pady=10,padx=10)

        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Password", show='*', font=("Century Gothic bold",15),corner_radius=15)
        self.senha_login_entry.grid(row=2,column=0,pady=10,padx=10)

        self.look_password = ctk.CTkCheckBox(self.frame_login, width=300, text="Remember me", font=("Century Gothic bold",12),corner_radius=15)
        self.look_password.grid(row=3, column=0, pady=10,padx=10)

        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="Login".upper(), font=("Century Gothic bold", 12),corner_radius=15, command=self.forms)
        self.btn_login.grid(row=4, column=0, pady=10, padx=10)

        self.btn_signup = ctk.CTkButton(self.frame_login, width=300, text="Sign Up".upper(), font=("Century Gothic bold", 12), corner_radius=15, command=self.forms2)
        self.btn_signup.grid(row=5, column=0, pady=10, padx=10)



    def forms(self):


        self.frame_login.place_forget()
        self.frame_login2.place_forget()

        self.frame_loca = ctk.CTkFrame(self, width=400, height=100)
        self.frame_loca.place(x=630, y=55)

        self.city_entry = ctk.CTkEntry(self.frame_loca, width=300, placeholder_text="Enter the city", font=("Century Gothic bold",15), corner_radius=15)
        self.city_entry.grid(row=1,column=0,pady=10,padx=10)


        self.diary_entry = ctk.CTkEntry(self.frame_loca, width=150, placeholder_text="Days (Max: 5 days)",font=("Century Gothic bold",15),corner_radius=15)
        self.diary_entry.grid(row=3,column=0,pady=10,padx=10)



        self.btn_weather = ctk.CTkButton(self.frame_loca, width=300, text="Search".upper(), font=("Century Gothic bold", 12),corner_radius=15, command=self.open)
        self.btn_weather.grid(row=4, column=0, pady=10, padx=10)


    def forms2(self):

        self.frame_login.place_forget()

        self.frame_login2 = ctk.CTkFrame(self, width=400, height=300)
        self.frame_login2.place(x=560, y=55)

        self.username_sign_entry = ctk.CTkEntry(self.frame_login2, width=300, placeholder_text="New Username", font=("Century Gothic bold",15), corner_radius=15)
        self.username_sign_entry.grid(row=1,column=0,pady=10,padx=10)

        self.senha_sign_entry = ctk.CTkEntry(self.frame_login2, width=300, placeholder_text="New Password", show='*', font=("Century Gothic bold",15),corner_radius=15)
        self.senha_sign_entry.grid(row=2,column=0,pady=10,padx=10)

        self.lb_title2 = ctk.CTkLabel(self.frame_login2, text="Create your Username and Password", font=("Century Gothic bold", 22), text_color='purple')
        self.lb_title2.grid(row=0, column=0, padx=50, pady=50)

        self.btn_login3 = ctk.CTkButton(self.frame_login2, width=300, text="Sign up".upper(), font=("Century Gothic bold", 12),corner_radius=15, command=self.login_screen)
        self.btn_login3.grid(row=4, column=0, pady=10, padx=10)


    def open(self):

        self.frame_loca.place_forget()

        cityy = self.city_entry.get()
        dayss = int(self.diary_entry.get())

        API_KEY = "950bfa0d150d01685fd8598557f22b0c"
        link = f"https://api.openweathermap.org/data/2.5/forecast?q={cityy}&appid={API_KEY}&cnt={dayss}"
        reqst = requests.get(link)
        reqst_dic = reqst.json()


        loc = reqst_dic['city']['name']
        listt = reqst_dic['list'][dayss-1]['main']['temp']-273
        sensation = reqst_dic['list'][dayss-1]['main']['feels_like']-273
        #descrip = reqst_dic['list'][dayss-1]['weather']['main']


        self.frame_login4 = ctk.CTkFrame(self, width=400, height=300)
        self.frame_login4.place(x=560, y=55)

        self.text_box= ctk.CTkTextbox(self.frame_login4, width=300, height=100)
        self.text_box.grid(row=5,column=0, pady=10, padx=10)
        self.text_box.insert("0.0","The information you requested has already been \nsent...\nHave a nice day :)")


        print(f"Location: {loc}")
        print(f"In {dayss} days from now it will be an average of {listt:.2f}ºC, with a thermal sensation of {sensation:.2f}ºC")
        #print("The weather description will be: ",descrip)


if __name__=="__main__":
    app = App()
    app.mainloop()
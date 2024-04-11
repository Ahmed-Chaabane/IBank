from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Database import Database
from customtkinter import *
from Menu import Application as MenuWindow


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.menu_window = None
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login ibank')

        # Background Image
        self.bg_frame = Image.open("images/bg_login.png")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both')

        # Login Frame
        self.lgn_frame = Frame(self.window, bg='#fbfbfd', width=950, height=600)
        self.lgn_frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the frame

        # Left Side Image
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#fbfbfd')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=50)

        # SignIn Image
        self.sign_in_image = Image.open('images/login_sign.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#fbfbfd')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=630, y=80)

        # SignIn Label
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#fbfbfd", fg="black", font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=665, y=240)

        # Username
        self.username_label = Label(self.lgn_frame, text="Username", bg="#fbfbfd", fg="black",font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)
        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#fbfbfd", fg="#6b6a69", font=("yu gothic ui", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)
        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#fbfbfd')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # Login Button
        self.login = Button(self.lgn_frame, text='LOGIN', font=("yu gothic ui", 14, "bold"), width=29, height=1, bd=0, bg='#3047ff', cursor='hand2', activebackground='#e7e7e7', fg='white', command=self.show_message)
        self.login.place(x=550, y=470)

        # Password
        self.password_label = Label(self.lgn_frame, text="Password", bg="#fbfbfd", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)
        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#fbfbfd", fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#fbfbfd')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)

        self.show_button = Button(self.lgn_frame, text='SHOW', font=("yu gothic ui", 10), relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2", command=self.show_password)
        self.show_button.place(x=830, y=415)

    def show_password(self):
        self.password_entry.config(show='')

    def show_message(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username:
            messagebox.showerror("Error", "Please enter your username.")
        elif not password:
            messagebox.showerror("Error", "Please enter your password.")
        elif len(username) < 6 or len(password) < 6:
            messagebox.showerror("Error", "Username and password must be at least 6 characters long.")
        else:
            db = Database.get_instance()  # Get the database connection instance
            db.connect_to_database()  # Connect to the database
            authenticated = db.authenticate_user(username, password)
            db.disconnect()

            if authenticated:
                messagebox.showinfo("Success", "Login Successful!")
                self.window.destroy()
                root = Tk()
                menu_window = MenuWindow(root)
                root.mainloop()
            else:
                messagebox.showerror("Error", "Invalid username or password.")

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()

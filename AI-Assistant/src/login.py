from database.database_operations import insert_login

from customtkinter import *
from PIL import Image
from google_auth_oauthlib.flow import InstalledAppFlow
import os

app = CTk()
app.geometry("800x680")
app.resizable(0, 0)

# Load and set side image
side_img_data = Image.open("resources//side-img.png")
google_img = Image.open("resources//google-icon.png")
srm_logo = Image.open("resources//srm-logo.png")
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(500, 680))
google_img = CTkImage(dark_image=google_img, light_image=google_img, size=(20,20))
srm_logo=CTkImage(dark_image=srm_logo, light_image=srm_logo, size=(20,20))

# Left side image label (keeps this constant)
CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

# Right frame to hold login or create account fields
frame = CTkFrame(master=app, width=500, height=680, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

def login():
    import home
    from PIL import Image
    send_img_data = Image.open("resources/arrow.png")
    home_img_data = Image.open("resources//home.png")
    settings_img_data = Image.open("resources//settings.png")
    home.open_home_window(send_img_data, home_img_data, settings_img_data)

def authenticate_with_google():
    # Specify the scopes you need (e.g., email, profile)
    scopes = ["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"]
    # Initialize the OAuth flow
    flow = InstalledAppFlow.from_client_secrets_file(
        'E:\Admin\Python\APP Project\AI Assistant\src\google\secret.json', scopes=scopes)
    credentials = flow.run_local_server(port=8080)
    # Retrieve user info here, if needed, after successful login
    print("Authenticated user:", credentials)

def open_academia_url():
    import webbrowser
    url = "https://academia.srmist.edu.in"
    webbrowser.open(url)

# Toggle function to switch views
def show_login():
    # Clear frame and populate with login fields
    for widget in frame.winfo_children():
        widget.destroy()
    
    CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))
    
    CTkLabel(master=frame, text="Username", text_color="#601E88", anchor="w", font=("Arial Bold", 14)).pack(anchor="w", pady=(38, 0), padx=(25, 0))
    CTkEntry(master=frame, width=225, placeholder_text="username",font=("Helventica",20), text_color=('white', 'black'), fg_color="#EEEEEE").pack(anchor="w", padx=(25, 0))
    
    CTkLabel(master=frame, text="Password:", text_color="#601E88", anchor="w", font=("verdana", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
    CTkEntry(master=frame, width=225, placeholder_text="password",font=("Helventica",20), text_color=('white', 'black'), fg_color="#EEEEEE", show="*").pack(anchor="w", padx=(25, 0))
    
    CTkButton(master=frame, text="Login", fg_color="#601E88", font=("Arial Bold", 12), width=225, command=login).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, image=google_img, text="Continue with google", fg_color="#F1F1F1",text_color="black", font=("Arial Bold", 12), width=225, command=authenticate_with_google).pack(anchor="w", pady=(10, 0), padx=(25, 0))    
    CTkButton(master=frame, image=srm_logo,hover_color="#D1E8FF", text="Continue with college",text_color="black", fg_color="#F1F1F1", font=("Arial Bold", 12), width=225, command=open_academia_url).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    # Button to toggle to create account view
    CTkButton(master=frame, text="Create new account", fg_color="#601E88", command=show_create_account).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    CTkLabel(master=frame, text="Made by Nimitt Sharma-All rights reserved 2024-v.1.0.0", text_color="#601E88", anchor="w", font=("Arial Bold", 11, 'bold')).pack(anchor="w", pady=(270, 0), padx=(0, 0))
def show_create_account():
    # Clear frame and populate with create account fields
    for widget in frame.winfo_children():
        widget.destroy()
    
    CTkLabel(master=frame, text="Create New Account", text_color="#601E88", anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    
    CTkLabel(master=frame, text="First Name:", text_color="#601E88", anchor="w", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    CTkEntry(master=frame,placeholder_text="Nimitt", width=225, fg_color="#EEEEEE").pack(anchor="w", padx=(25, 0))
    
    CTkLabel(master=frame, text="Last Name:", text_color="#601E88", anchor="w", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    CTkEntry(master=frame, width=225,placeholder_text="Sharma", fg_color="#EEEEEE").pack(anchor="w", padx=(25, 0))
    
    CTkLabel(master=frame, text="Username:", text_color="#601E88", anchor="w", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    CTkEntry(master=frame, width=225,placeholder_text="username", fg_color="#EEEEEE").pack(anchor="w", padx=(25, 0))
    
    CTkLabel(master=frame, text="Password:", text_color="#601E88", anchor="w", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    CTkEntry(master=frame, width=225,placeholder_text="password", fg_color="#EEEEEE", show="*").pack(anchor="w", padx=(25, 0))
    
    CTkLabel(master=frame, text="Confirm Password:", text_color="#601E88", anchor="w", font=("Arial Bold", 14)).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    CTkEntry(master=frame, width=225,placeholder_text="confirm password", fg_color="#EEEEEE", show="*").pack(anchor="w", padx=(25, 0))
    
    CTkButton(master=frame, text="Sign Up", fg_color="#601E88", font=("Arial Bold", 12), width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    CTkButton(master=frame, image=google_img, text="Continue with google", fg_color="#F1F1F1", font=("Arial Bold", 12), width=225, command=authenticate_with_google).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    CTkButton(master=frame, image=srm_logo,hover_color="#D1E8FF", text="Continue with college",text_color="black", fg_color="#F1F1F1", font=("Arial Bold", 12), width=225, command=open_academia_url).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    # Button to toggle back to login view
    CTkButton(master=frame, text="Back to Login", fg_color="#601E88", command=show_login).pack(anchor="w", pady=(10, 0), padx=(25, 0))
    CTkLabel(master=frame, text="Made by Nimitt Sharma-All rights reserved 2024-v.1.0.0", text_color="#601E88", anchor="w", font=("Arial Bold", 11, 'bold')).pack(anchor="w", pady=(270, 0), padx=(0, 0))
# Initialize with login view
show_login()
app.mainloop()

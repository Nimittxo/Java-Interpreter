from tkinter import Tk, Frame
from customtkinter import CTkButton
from google_auth_oauthlib.flow import InstalledAppFlow
import os

def authenticate_with_google():
    # Specify the scopes you need (e.g., email, profile)
    scopes = ["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email"]
    # Initialize the OAuth flow
    flow = InstalledAppFlow.from_client_secrets_file(
        'E:\Admin\Python\APP Project\AI Assistant\src\google\secret.json', scopes=scopes)
    credentials = flow.run_local_server(port=8080)
    # Retrieve user info here, if needed, after successful login
    print("Authenticated user:", credentials)

# Initialize Tkinter window
root = Tk()
frame = Frame(root)
frame.pack()

# Add Google sign-in button
google_img = None  # Add your Google icon image here
google_button = CTkButton(master=frame, image=google_img, text="Continue with Google", 
                          fg_color="black", font=("Arial Bold", 12), width=225, 
                          command=authenticate_with_google)
google_button.pack(anchor="w", pady=(10, 0), padx=(25, 0))

root.mainloop()

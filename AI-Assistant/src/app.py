from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("856x645")
app.resizable(0,0)
set_appearance_mode("light")

# Sidebar frame
sidebar_frame = CTkFrame(master=app, fg_color="#2A8C55",  width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

# Load images for buttons
#logo_img_data = Image.open("logo.png")
#logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

#analytics_img_data = Image.open("analytics_icon.png")
#analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)

#package_img_data = Image.open("package_icon.png")
#package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)

#returns_img_data = Image.open("returns_icon.png")
#returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)

# Display logo on the sidebar
#CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(38, 0), anchor="center")

# Function to switch frames
def show_frame(frame):
    frame.tkraise()  # Bring the selected frame to the front

# Main content frame for switching views
main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

# Create frames for each tab
dashboard_frame = CTkFrame(main_view, fg_color="lightblue", width=680, height=650, corner_radius=0)
orders_frame = CTkFrame(main_view, fg_color="lightgreen", width=680, height=650, corner_radius=0)
returns_frame = CTkFrame(main_view, fg_color="lightyellow", width=680, height=650, corner_radius=0)

# Pack all frames in the same position
for frame in (dashboard_frame, orders_frame, returns_frame):
    frame.place(relwidth=1, relheight=1)

# Content in each frame
CTkLabel(dashboard_frame, text="Dashboard", font=("Arial Black", 25), text_color="#2A8C55").pack(pady=20)
CTkLabel(orders_frame, text="Orders", font=("Arial Black", 25), text_color="#2A8C55").pack(pady=20)
CTkLabel(returns_frame, text="Returns", font=("Arial Black", 25), text_color="#2A8C55").pack(pady=20)

# Sidebar buttons with commands to switch frames
CTkButton(master=sidebar_frame, text="Dashboard", fg_color="transparent", 
          font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: show_frame(dashboard_frame)).pack(anchor="center", ipady=5, pady=(60, 0))

CTkButton(master=sidebar_frame, text="Orders", fg_color="transparent", 
          font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: show_frame(orders_frame)).pack(anchor="center", ipady=5, pady=(16, 0))

CTkButton(master=sidebar_frame, text="Returns", fg_color="transparent", 
          font=("Arial Bold", 14), hover_color="#207244", anchor="w", command=lambda: show_frame(returns_frame)).pack(anchor="center", ipady=5, pady=(16, 0))

# Show the initial frame (e.g., Dashboard) by default
show_frame(dashboard_frame)

app.mainloop()

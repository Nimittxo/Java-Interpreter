from customtkinter import CTk, CTkLabel
from tkinter import Canvas
import threading
from PIL import Image, ImageDraw, ImageTk

# Create the application window
app = CTk()
app.geometry("300x300")
app.title("Splash Loading Example")

# Make the window transparent
app.overrideredirect(True)  # Removes window borders
app.attributes("-topmost", True)  # Keeps it on top of all windows
app.attributes("-alpha", 0.5)  # Set transparency (1.0 = opaque, 0.0 = fully transparent)

# Function to create rotating circular loading animation
def create_circle_arc(angle, radius=40):
    image = Image.new("RGBA", (radius*2, radius*2), (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(image)
    draw.arc((5, 5, radius*2-5, radius*2-5), start=angle, end=angle + 45, fill="purple", width=8)
    return ImageTk.PhotoImage(image)

# Function to update the loading animation
def animate_loading(canvas, angle=0):
    if not hasattr(canvas, "image_id"):
        canvas.image_id = None

    if canvas.image_id:
        canvas.delete(canvas.image_id)

    image = create_circle_arc(angle)
    canvas.image_id = canvas.create_image(80, 80, image=image)
    canvas.image = image
    
    app.after(50, animate_loading, canvas, (angle + 15) % 360)

# Canvas for circular loading animation
canvas = Canvas(app, width=160, height=160,bg='black', highlightthickness=0)  # Fully transparent canvas
canvas.pack(pady=40)

# Label to show loading text
CTkLabel(app, text="Loading, please wait...", font=("Arial", 14)).pack()

# Start animation in a thread to keep GUI responsive
threading.Thread(target=animate_loading, args=(canvas,), daemon=True).start()

app.mainloop()

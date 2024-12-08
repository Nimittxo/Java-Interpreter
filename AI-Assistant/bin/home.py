import customtkinter as ctk
from tkinter import Text, Scrollbar
from PIL import Image
import os
import requests
import base64
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import ChatCompletionsClient

api_key = os.getenv("AZURE_INFERENCE_CREDENTIAL", "Ty7XOPAZWDxWwprpH58YBldDnoPpdJyB")  # Replace 'MY_API_KEY' with your actual API key
endpoint = "https://Phi-3-5-mini-instruct-pdnyp.eastus.models.ai.azure.com"  # Replace with your actual endpoint

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)



# Initialize main application window
def open_home_window(send_img_data, home_img_data, settings_img_data):
    app = ctk.CTkToplevel()
    app.geometry("700x600")
    app.title("ChatGPT Interface")

    # Load and convert the send button image using CTkImage from Pillow
    send_img = ctk.CTkImage(dark_image=send_img_data, light_image=send_img_data)
    home_img = ctk.CTkImage(dark_image=home_img_data, light_image=home_img_data)
    setting_img = ctk.CTkImage(dark_image=settings_img_data, light_image=settings_img_data)

    chat_names = []
    button_y_position=170

    # Function to handle sending messages
    def send_message():
        user_message = entry_message.get().strip()
        if user_message:
            display_chat.insert("end", f"You: {user_message}\n", "user")
            entry_message.delete(0, "end")

            # Prepare the payload for Azure LLM API
            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": user_message
                    }
                ],
                "max_tokens": 2048,
                "temperature": 0.8,
                "top_p": 0.1,
                "presence_penalty": 0,
                "frequency_penalty": 0
            }
            
            # Fetch response from Azure LLM
            try:
                response = client.complete(payload)
                bot_response = response.choices[0].message.content
                display_chat.insert("end", f"Azure: {bot_response}\n", "bot")
            except Exception as e:
                display_chat.insert("end", f"Error: {str(e)}\n", "error")

        display_chat.see("end")  # Scroll to the end

    # Function to add a new chat
    def add_chat():
        nonlocal button_y_position  # Use the nonlocal variable to modify it
        # Generate a new chat name (for example, "Chat 1", "Chat 2", etc.)
        chat_name = f"Chat {len(chat_names) + 1}"
        chat_names.append(chat_name)

        # Create a button for the new chat in the sidebar
        chat_button = ctk.CTkButton(sidebar_frame, text=chat_name, command=lambda: select_chat(chat_name))
        chat_button.place(x=0, y=button_y_position)  # Set the y position
        button_y_position += 50

    # Function to select a chat
    def select_chat(chat_name):
        # Display the selected chat name in the chat display area
        display_chat.delete(1.0, "end")  # Clear previous chat
        display_chat.insert("end", f"Selected: {chat_name}\n")

    # Sidebar Frame
    sidebar_frame = ctk.CTkFrame(app, width=150, fg_color="#1F1F1F")
    sidebar_frame.pack(side="left", fill="y")

    sidebar_buttons1 = ctk.CTkButton(sidebar_frame, image=home_img, text="Home", 
                                      font=ctk.CTkFont(size=14, weight="bold"), 
                                      fg_color="#2E2E2E", text_color="white")
    sidebar_buttons1.place(x=0, y=20)

    sidebar_buttons2 = ctk.CTkButton(sidebar_frame, image=setting_img, text="Settings", 
                                      font=ctk.CTkFont(size=14, weight="bold"), 
                                      fg_color="#2E2E2E", text_color="white")
    sidebar_buttons2.place(x=0, y=70)

    # Button to add a new chat
    add_chat_button = ctk.CTkButton(sidebar_frame, text="New Chat", command=add_chat, 
                                     font=ctk.CTkFont(size=14, weight="bold"), 
                                     fg_color="#2E2E2E", text_color="white")
    add_chat_button.place(x=0, y=120)

    # Chat Display Frame
    chat_frame = ctk.CTkFrame(app, fg_color="#121212")
    chat_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Display Chat Text Box
    display_chat = Text(chat_frame, wrap="word", font=("Helventica", 15), bg="#121212", fg="white")
    display_chat.tag_config("user", foreground="#00BFFF")  # Bright Blue
    display_chat.tag_config("model3.0", foreground="#FFA500")   # Orange
    display_chat.pack(expand=True, fill="both", padx=10, pady=(10, 0))

    # Scrollbar for chat display
    scrollbar = Scrollbar(chat_frame, command=display_chat.yview, bg="#2E2E2E")
    scrollbar.pack(side="right", fill="y")
    display_chat.config(yscrollcommand=scrollbar.set)

    # Message Entry Frame
    message_frame = ctk.CTkFrame(app, height=50, fg_color="#1F1F1F")
    message_frame.pack(fill="x", padx=10, pady=(0, 10))

    # Message Entry Frame
    message_frame = ctk.CTkFrame(app, height=50, fg_color="#1F1F1F")
    message_frame.pack(fill="x", padx=10, pady=(0, 10))

    entry_message = ctk.CTkEntry(message_frame, placeholder_text="Type a message...", width=400, font=("Arial", 14), fg_color="#2E2E2E", text_color="white", placeholder_text_color="gray")
    entry_message.grid(row=0, column=0, padx=(10, 5), pady=10)

    send_button = ctk.CTkButton(message_frame, image=send_img, text="Send", command=send_message, width=70, compound="left", fg_color="#2E2E2E", text_color="white")
    send_button.grid(row=0, column=1, padx=5)

    model_options = ["Azure LLM", "OpenAI GPT-4"]
    model_dropdown = ctk.CTkOptionMenu(app, values=model_options)  # Set default selection
    model_dropdown.pack(pady=10)

    # Run the window
    app.mainloop()

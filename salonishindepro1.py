import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# List of predefined commands
commands = ["hello", "goodbye", "turn on the light", "turn off the light", "play music", "stop music"]

class SpeechRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech Recognition App")
        self.root.geometry("400x300")

        # Set up the background image
        self.background_image = Image.open("C:/Users/Lenovo/Desktop/Desktop/jGlzr.png")  # Replace with your image path
        self.background_image = self.background_image.resize((400, 300))
        self.bg_image = ImageTk.PhotoImage(self.background_image)
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        # Decorative Label
        self.title_label = tk.Label(root, text="Speech Recognition App", font=("times new roman", 16, "bold"), bg="#ADD8E6")
        self.title_label.pack(pady=10)

        # Instruction Label
        self.instruction_label = tk.Label(root, text="Press the button and speak a command", font=("times new roman", 12), bg="#ADD8E6")
        self.instruction_label.pack(pady=10)

        # Start Listening Button
        self.start_button = tk.Button(root, text="Start Listening", font=("times new roman", 12), command=self.start_listening, bg="#90EE90", activebackground="#32CD32")
        self.start_button.pack(pady=10)

        # Recognized Text Label
        self.recognized_text_label = tk.Label(root, text="", font=("times new roman", 12), fg="blue", bg="#ADD8E6")
        self.recognized_text_label.pack(pady=10)

    def start_listening(self):
        self.instruction_label.config(text="Listening...")
        self.root.update()
        recognized_text = self.recognize_speech_from_mic()
        if recognized_text:
            for command in commands:
                if recognized_text.lower() == command:
                    self.recognized_text_label.config(text=f"Command recognized: {command}")
                    self.instruction_label.config(text="Press the button and speak a command")
                    return
            self.recognized_text_label.config(text="Command not recognized")
        else:
            self.recognized_text_label.config(text="No command recognized")
        self.instruction_label.config(text="Press the button and speak a command")

    def recognize_speech_from_mic(self):
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

            try:
                recognized_text = recognizer.recognize_google(audio)
                return recognized_text
            except sr.UnknownValueError:
                messagebox.showerror("Error", "Google Web Speech API could not understand the audio")
            except sr.RequestError as e:
                messagebox.showerror("Error", f"Could not request results from Google Web Speech API; {e}")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechRecognitionApp(root)
    root.mainloop()

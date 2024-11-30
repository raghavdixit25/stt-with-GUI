import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import threading

# Function for speech-to-text conversion
def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing...")

            # Convert speech to text using Google's speech recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)

            # Update the text field with the recognized text
            text_box.delete(1.0, tk.END)  # Clear the text box
            text_box.insert(tk.END, text)  # Insert the new text

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            text_box.delete(1.0, tk.END)  # Clear text box
            text_box.insert(tk.END, "Could not understand the audio.")

        except sr.RequestError as e:
            print(f"Could not request results from the service; {e}")
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, "Error with speech recognition service.")

        except Exception as e:
            print(f"An error occurred: {e}")
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, f"An error occurred: {e}")

# Function to start listening in a separate thread (to avoid GUI freezing)
def start_listening():
    # Create a new thread to run the speech recognition to keep the GUI responsive
    listening_thread = threading.Thread(target=speech_to_text)
    listening_thread.start()

# Create the main window
root = tk.Tk()
root.title("Speech to Text")
root.geometry("400x300")

# Create a text box to display the recognized speech
text_box = tk.Text(root, height=10, width=40)
text_box.pack(pady=20)

# Create a button with a microphone icon (using a text-based button for simplicity)
microphone_button = tk.Button(root, text="🎤 Start Listening", command=start_listening, font=("Arial", 14), height=2, width=20)
microphone_button.pack()

# Start the Tkinter main loop
root.mainloop()

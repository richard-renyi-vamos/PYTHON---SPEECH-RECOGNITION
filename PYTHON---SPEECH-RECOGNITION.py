import speech_recognition as sr
import tkinter as tk

def audio_captioning(language):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Open the audio stream (replace 'audio_file.wav' with your source)
    with sr.AudioFile('audio_file.wav') as source:
        print("Listening...")

        # Adjust for ambient noise if necessary
        recognizer.adjust_for_ambient_noise(source)

        # Listen for the audio and transcribe
        audio = recognizer.record(source)
        print("Processing...")

        try:
            # Recognize the speech from the audio using the selected language
            if language == "English":
                text = recognizer.recognize_google(audio, language='en-US')
            elif language == "German":
                text = recognizer.recognize_google(audio, language='de-DE')
            elif language == "Hungarian":
                text = recognizer.recognize_google(audio, language='hu-HU')
            else:
                print("Invalid language selection.")
                return None

            print("Transcription:")
            print(text)
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None

def start_transcription():
    selected_language = language_var.get()
    if selected_language:
        captions = audio_captioning(selected_language)
        # Do something with the captions, e.g., display in a GUI, save to a file, etc.
    else:
        print("Please select a language.")

# GUI setup
root = tk.Tk()
root.title("Audio Captioning")

# Language selection
language_var = tk.StringVar()
language_var.set("")  # Default value

languages = ["English", "German", "Hungarian"]
language_options = tk.OptionMenu(root, language_var, *languages)
language_options.pack()

# Start button
start_button = tk.Button(root, text="Start Transcription", command=start_transcription)
start_button.pack()

root.mainloop()

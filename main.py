import speech_recognition as sr
import tkinter as tk
import os

# initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


def transcribe_audio_file(file_path):
    # reading audio file
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)

    # speech recognition using Google Speech Recognition
    text = r.recognize_google(audio, language="en-US")

    # Writing the transcription to a text file with the same name as the audio file
    transcription_file_path = os.path.splitext(file_path)[0] + ".txt"
    with open(transcription_file_path, "w") as file:
        file.write(text)


def transcribe_audio_folder(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file_path.endswith(".wav"):
            transcribe_audio_file(file_path)


def transcribe_audio():
    file_path = entry.get()
    if os.path.isfile(file_path):
        transcribe_audio_file(file_path)
    elif os.path.isdir(file_path):
        transcribe_audio_folder(file_path)


# GUI window using tkinter
root = tk.Tk()
root.title("Audio Transcription")
root.geometry("500x200")

# Create a label for the file path input
label = tk.Label(root, text="Enter the file path or folder path:")
label.pack()

# Create an entry for the user to input the file path
entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

# Create a button to trigger the transcribe function
transcribe_button = tk.Button(root, text="Transcribe Audio", font=("Arial", 14), command=transcribe_audio)
transcribe_button.pack()

root.mainloop()

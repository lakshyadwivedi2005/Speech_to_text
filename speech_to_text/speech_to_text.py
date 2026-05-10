import speech_recognition as sr
import os

def transcribe_from_microphone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
<<<<<<< HEAD
        print(" Speak something... (press Ctrl+C to stop)")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)
=======
        print(" Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
>>>>>>> 301a7ce (Updated speech to text project)

    try:
        text = recognizer.recognize_google(audio)
        print("\n Transcription:")
        print(text)
        save_transcription(text)
    except sr.UnknownValueError:
        print(" Could not understand the audio.")
    except sr.RequestError:
        print(" Could not connect to the service. Check internet connection.")

def transcribe_from_file(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        print(" Processing audio file...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)


    try:
        text = recognizer.recognize_google(audio)
        print("\n Transcription:")
        print(text)
        save_transcription(text)
    except sr.UnknownValueError:
        print(" Could not understand the audio.")
    except sr.RequestError:
<<<<<<< HEAD
        print(" Could not connect to the service. Check internet connection.")
=======
        print("Could not connect to the service. Check internet connection.")
>>>>>>> 301a7ce (Updated speech to text project)

def save_transcription(text, filename="transcription.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f" Transcription saved to {filename}")

if __name__ == "__main__":
    print("====== Speech-to-Text Tool ======")
    print("1. Record from Microphone")
    print("2. Transcribe from Audio File")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        transcribe_from_microphone()
    elif choice == "2":
        file_path = input("Enter the audio file path (wav/mp3): ").strip()
        if os.path.exists(file_path):
            transcribe_from_file(file_path)
        else:
            print(" File not found. Please check the path.")
    else:
        print("Invalid choice!")

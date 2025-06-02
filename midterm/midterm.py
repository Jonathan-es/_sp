import pyttsx3
from datetime import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def format_time(current_time):
    """Format the time as hour o'clock, minute minutes, second seconds."""
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    return f"{hour} o'clock, {minute} minutes, {second} seconds"

def main():
    """Main program loop."""
    speak("Hello! Type '1' for time, '2' for date, or '3' to exit.")
    
    while True:
        option = input("Choose an option (1 for time, 2 for date, 3 for exit): ")

        if option == "1":
            current_time = datetime.now()
            formatted_time = format_time(current_time)
            speak(f"The current time is {formatted_time}")
            print(f"Time: {formatted_time}")
        
        elif option == "2":
            current_date = datetime.now().strftime("%A")
            speak(f"Today is {current_date}")
            print(f"Date: Today is {current_date}")
        
        elif option == "3":
            speak("Goodbye!")
            print("Exiting...")
            break  # Exit the program
        
        else:
            speak("Invalid option. Please type '1' for time, '2' for date, or '3' to exit.")
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

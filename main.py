from playsound import playsound
import time 

# Variables that clear the terminal
CLEAR = "\033[2J"
CLEARN_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        # wait for 1 second
        time.sleep(1)
        time_elapsed += 1
        
        # calculating the time left
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEARN_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    
    playsound("alarm2.mp3")
        
# Asking the user how much time the alarm should be set for 
minutes = int(input("How many minutes to wait: "))  
seconds = int(input("How many seconds to wait: "))  
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
from time import sleep
from random import randrange
import threading 
from task_manager import notification

motivational_phrases = [
    "Believe in yourself and all that you are.",
    "Every day is a new opportunity to grow and improve.",
    "Don't be afraid to make mistakes; they help you learn.",
    "Keep going, even if it feels hard; you're getting stronger.",
    "Dream big and don't let anyone limit you.",
    "You are capable of amazing things!",
    "Small steps lead to big achievements.",
    "Every effort you make is progress toward your goal.",
    "Stay positive, work hard, and enjoy the journey.",
    "Your potential is endless; keep pushing forward.",
    "Mistakes are proof that you're trying.",
    "You have the power to make a difference.",
    "Set your goals high, and don't stop until you reach them.",
    "Believe that you can, and you're halfway there.",
    "You're stronger than you think.",
    "Be proud of every step you take toward your dreams.",
    "You are braver, stronger, and smarter than you know.",
    "The more you practice, the better you'll get.",
    "Keep smiling, keep trying, and never give up!",
    "You are unique, and the world needs what you have to offer."
]


class Pomodoro_time:
    
    def __init__(self):
        self.work_time = 25 *60
        self.short_brake_time = 5 * 60
        self.notif = notification.Notifications()
        
    
    def start_timer(self, seconds):
        while seconds + 1:
            mins, secs = divmod(seconds, 60)
            timer = f"\033[1m{mins:02d}:{secs:02d}\033[0m"
            print(f"{timer}", end="\r")
            sleep(1)
            seconds -= 1
        print("\033[31m\nTime's up!\033[0m\n")
        sleep(1)
        return "00:00"
        
    
    def start_sessions(self):
        sessions = 4
        time_not = 20
        session_format = ["First", "Second", "Third", "Fourth"]
        for session in range(1, sessions + 1):
            print(f"**  It's time to work with focus.  **\n**  The {session_format[session - 1]} working period has begun.  **")
            sleep(0.5)
            print("\033[1m**  Get ready  **")
            sleep(0.5)
            for i in range(1, 3 + 1):
                print(f"**   {i}   **")
                sleep(1)
                if i == 3:
                    print("**  Ready  **")
            sleep(1)
            print("**  go  **\033[0m")
            print(f"Focus time ends in", end=":\n")
            
            self.start_timer(self.work_time)
            
            noet = threading.Thread(target=self.notif.app_notification, args=("Focus time end", time_not ))
            noet.start()
            noet.join()
            
            if session < sessions:
                noet2 = threading.Thread(target=self.notif.app_notification, args=("Break time end, come back to work",time_not,))
                i = randrange(0, 20)
                print(f"\033[1m\033[30m\033[47m****  {motivational_phrases[i]}  ****\033[0m\n")
                print("\033[1m* * \033[0m" * 20)
                sleep(1.5)
                
                
                print(f"The break will end in:", end=":\n")
                self.start_timer(self.short_brake_time)
                noet2.start()
                noet2.join()
                return "break time end"
            else:
                print("\033[1mCongratulations! You've finished a lot. Now relax and enjoy.\033[0m")
                return "all sessions done"
            
        
    








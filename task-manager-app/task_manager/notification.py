import threading
from playsound import playsound
from plyer import notification


class Notifications():
    def sound(self):
        playsound('task_manager/media/sound.wav')
    
    def app_notification(self, message , tim ):
        notification.notify(
            title="Task Manager",
            message=message,
            app_name="Task Manager",
            app_icon='task_manager/media/icon.ico',
            timeout=tim,
            toast=False
        )
        yswef = threading.Thread(target=self.sound())
        yswef.start()
        return "notification is sandeng"
    




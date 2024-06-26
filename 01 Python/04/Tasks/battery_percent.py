# from pynotifier import Notification, NotificationClient
# from pynotifier.backends import platform, smtp
# import psutil

# battery = psutil.sensors_battery()
# percent = battery.percent

# c = NotificationClient()

# c.register_backend(platform.Backend())

# notification = Notification(title = "Battery Percentage", message =  str(percent) + "% Percent Remaining")

# c.notify_all(notification)


from plyer import notification
import psutil

# Get the battery status
battery = psutil.sensors_battery()
percent = battery.percent

# send the notification
notification.notify(
    title = "Battery Percentage",
    message = f"{percent}% percent remaining",
    timeout = 10
)

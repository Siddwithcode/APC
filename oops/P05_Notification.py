class Notification:
    def send(self): pass
class EmailNotification(Notification):
    def send(self): print("Sending Email")
class SMSNotification(Notification):
    def send(self): print("Sending SMS")
class PushNotification(Notification):
    def send(self): print("Sending Push Notification")
for n in [EmailNotification(), SMSNotification(), PushNotification()]: n.send()

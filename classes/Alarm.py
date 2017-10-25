from threading import Timer

class Alarm(object):

    def __init__(self, successLight, warningLight, alarmLight):
        self.alarmArmed = False
        self.tiggred = True

        self.successLight = successLight
        self.warningLight = warningLight
        self.alarmLight = alarmLight

    def arm(self):
        self.successLight.on()
        self.alarmArmed = True

    def disarm(self):
        self.successLight.off()
        self.alarmArmed = False
        self.triggred = False

    def trigger(self):
        if self.alarmArmed:
            self.trigged = True
            self.warningLight.on()
            t = Timer(10, self.soundAlarm)

    def soundAlarm(self):
        if self.trigged:
            self.alarmLight.on()

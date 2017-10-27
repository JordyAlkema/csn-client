from threading import Timer

class Alarm(object):


    def __init__(self, server, successLight, warningLight, alarmLight, buzzer):
        self.alarmArmed = False
        self.tiggred = True
        self.server = server
        self.successLight = successLight
        self.warningLight = warningLight
        self.alarmLight = alarmLight
        self.alarmTimer = Timer(10, self.soundAlarm)
        self.buzzer = buzzer

    def arm(self):
        self.server.alarmIsArmed()
        self.successLight.on()
        self.alarmArmed = True

    def disarm(self):
        self.server.alarmIsDisarmed()
        self.buzzer.stop()
        self.alarmTimer.cancel()
        self.alarmLight.off()
        self.warningLight.off()
        self.successLight.off()
        self.alarmArmed = False
        self.triggred = False

    def trigger(self, force = False):
        if self.alarmArmed or force:
            self.server.alarmIsTriggered()
            self.trigged = True
            self.arm()
            self.warningLight.on()
            self.alarmTimer.cancel()
            self.alarmTimer = Timer(10, self.soundAlarm)
            self.alarmTimer.start()
            

    def soundAlarm(self, force = False):
        if self.trigged or force:
            self.arm()
            self.server.alarmIsGoingOff()
            self.alarmLight.on()
            self.buzzer.start()




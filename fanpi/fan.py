from gpiozero import DigitalOutputDevice


class Fan:
    @staticmethod
    def build_rpi(pin_nums):
        pins = [DigitalOutputDevice(
            pin=pin_num, active_high=True, initial_value=False) for pin_num in pin_nums]
        return Fan(pins)

    def __init__(self, pins):
        self.pins = pins
        self.speed = 0

    def get_current_speed(self):
        return self.speed

    def get_speeds(self):
        speeds = [0]
        for i in range(0, len(self.pins)):
            speeds.append(i + 1)
        return speeds

    def set_speed(speed):
        for pin in pins:
            pin.off()

        if speed == 0:
            return
        elif speed in range(0, len(self.pins)):
            self.pins[speed - 1].on()
        else:
            # TODO: raise
            pass

        self.speed = speed
        return self.speed

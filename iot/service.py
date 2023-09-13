import random
import string

from iot.device import Device

def generate_id(length: int = 8):
    return "".join(random.choices(string.ascii_lowercase, k=length))

class IOTService:
    def __int__(self):
        self.devices: dict[str, Device] = {}

    def register_device(self, device: Device):
        device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id





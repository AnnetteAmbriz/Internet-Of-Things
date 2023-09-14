import random
import string

from iot.device import Device
from iot.message import Message


def generate_id(length: int = 8):
    return "".join(random.choices(string.ascii_lowercase, k=length))


class IOTService:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    def register_device(self, device: Device) -> str:
        device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id

    def unregister_device(self, message: Message) -> None:
        device_id = message.device_id
        device = self.devices.get(device_id)
        device.disconnect()
        self.devices.pop(device_id)

    def unregister_device_2(self, device_id: str) -> None:
        self.devices[device_id].disconnect()
        del self.devices[device_id]

    def get_device(self, device_id: str) -> Device:
        return self.devices[device_id]

    def run_program(self, messages: list[Message]) -> None:
        print("===========Running program===========")
        for msg in messages:
            self.devices[msg.device_id].send_message(msg.msg_type, msg.data)
        print("======Completed running program=======")

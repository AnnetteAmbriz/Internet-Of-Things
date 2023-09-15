from iot.device import Device
from iot.message import MessageType


class SmartLight(Device):
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def send_message(self, message_type: MessageType, data: str) -> None:
        pass

    def get_status_update(self) -> None:
        pass


class SmartSpeaker(Device):
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def send_message(self, message_type: MessageType, data: str) -> None:
        pass

    def get_status_update(self) -> None:
        pass


class SmartCurtains(Device):
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def send_message(self, message_type: MessageType, data: str) -> None:
        pass

    def get_status_update(self) -> None:
        pass
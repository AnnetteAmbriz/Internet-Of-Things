from abc import ABC, abstractmethod

from iot.message import MessageType


# abstract base class
class Device(ABC):

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def send_message(self, message_type: MessageType, data: str) -> None:
        pass

    @abstractmethod
    def get_status_update(self) -> None:
        pass

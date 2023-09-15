from enum import Enum, auto
from dataclasses import dataclass


class MessageType(Enum):
    OPEN = auto()
    CLOSE = auto()
    SWITCH_ON = auto()
    SWITCH_OFF = auto()
    PLAY_SONG = auto()


@dataclass
class Message:
    device_id: str
    msg_type: MessageType
    data: str = ""


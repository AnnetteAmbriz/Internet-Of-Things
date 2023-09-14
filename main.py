from iot.devices import SmartLight, SmartSpeaker
from iot.message import Message, MessageType
from iot.service import IOTService


def main():

    # create iot service
    iot_service = IOTService()

    # morning program
    def wake_up_program():
        light = SmartLight()
        speaker = SmartSpeaker()

        light_id = iot_service.register_device(light)
        speaker_id = iot_service.register_device(speaker)

        morning_messages = []
        start_light = Message(light_id, MessageType.SWITCH_ON, "Start up")
        start_speaker = Message(speaker_id, MessageType.SWITCH_ON, "Start up")
        morning_messages.append(start_light)
        morning_messages.append(start_speaker)

        iot_service.run_program(morning_messages)

    wake_up_program()


if __name__ == '__main__':
    main()

from iot.devices import SmartLight, SmartSpeaker, SmartCurtains
from iot.message import Message, MessageType
from iot.service import IOTService


def main():

    # create iot service
    iot_service = IOTService()

    light = SmartLight()
    speaker = SmartSpeaker()
    curtains = SmartCurtains()

    light_id = iot_service.register_device(light)
    speaker_id = iot_service.register_device(speaker)
    curtains_id = iot_service.register_device(curtains)

    def wake_up_program():

        light.connect()
        speaker.connect()
        curtains.connect()

        wake_up_program_messages = [
            Message(light_id, MessageType.SWITCH_ON),
            Message(speaker_id, MessageType.SWITCH_ON),
            Message(speaker_id, MessageType.PLAY_SONG, "Miles Davis - Blue In Green"),
            Message(curtains_id, MessageType.OPEN)]

        iot_service.run_program(wake_up_program_messages)

    def sleep_program():
        sleep_program_messages = [
            Message(curtains_id, MessageType.CLOSE),
            Message(speaker_id, MessageType.SWITCH_OFF),
            Message(light_id, MessageType.SWITCH_OFF)
        ]

        iot_service.run_program(sleep_program_messages)

        curtains.disconnect()
        speaker.disconnect()
        light.disconnect()

    wake_up_program()


if __name__ == '__main__':
    main()

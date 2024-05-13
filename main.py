def on_received_number(receivedNumber):
    if receivedNumber == 0:
        music.play(music.tone_playable(784, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    if receivedNumber == 1:
        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            """)
    basic.clear_screen()
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
    if (receivedNumber == 1) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            . . . . .
            . . . . .
            `)
    }
    basic.clearScreen()
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(0)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(1)
})
radio.setGroup(1)

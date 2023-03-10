input.onButtonPressed(Button.A, function () {
    basic.showString("139")
    basic.showIcon(IconNames.No)
    music.playMelody("C5 B A G F E D C ", 500)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("138")
    basic.showIcon(IconNames.Yes)
    music.playMelody("C D E F G A B C5 ", 500)
})
basic.showString("69+69?")
basic.showString("A=139👋B=138")

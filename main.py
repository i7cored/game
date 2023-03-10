def on_button_pressed_a():
    basic.show_string("139")
    basic.show_icon(IconNames.NO)
    music.play_melody("C5 B A G F E D C ", 500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("138")
    basic.show_icon(IconNames.YES)
    music.play_melody("C D E F G A B C5 ", 500)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("69+69?")
basic.show_string("A=139👋B=138")
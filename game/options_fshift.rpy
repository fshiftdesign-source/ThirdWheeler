# Pattern | Diagonal scrolling background

init:
    image moving_pattern = Transform(
        Tile("gui/pattern.png"),
        xysize=(config.screen_width + 87, config.screen_height + 87),
        xanchor=0, yanchor=0
    )

    transform diagonal_scroll:
        subpixel True
        xpos -87 ypos -87
        linear 4.0 xpos 0 ypos 0
        repeat

screen background_pattern():
    add "moving_pattern" at diagonal_scroll
# -------------------------------------------------
# use background_pattern PARA EL PATRON EN DIAGONAL!!!!

#STARS
image stars = "gui/test.png"
image stars_der = "gui/test_2.png"

#STARS | Menu Anims + script
init python:
    import math

    def _swing_sine_func(trans, st, at, amp=12, speed=0.5):
        trans.rotate = amp * math.sin(st * speed)
        return 0

transform swing_soft_reversed:
    anchor (0.5, 0.0)
    align (0.5, 0.0)
    transform_anchor True

    function renpy.curry(_swing_sine_func)(amp=-8, speed=1.2)

    repeat

transform swing_soft:
    anchor (0.5, 0.0)
    align (0.5, 0.0)
    transform_anchor True

    function renpy.curry(_swing_sine_func)(amp=8, speed=1.2)

# ESTRELLAS POSICIONADAS LKDJFJLKA VVV
# -------------------------------------------------
screen stars_screen():

    hbox:
        spacing -40
        add "stars":
            at swing_soft
            xoffset 300

        add "stars_der":
            at swing_soft_reversed
            xoffset 60
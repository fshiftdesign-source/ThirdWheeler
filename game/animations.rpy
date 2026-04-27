
# This file contains the transforms used for animations in the game.

transform fade_overlay:
    alpha 0.0
    ease 0.3 alpha 1.0

transform fade_out:
    alpha 1.0
    ease 0.4 alpha 0.0

transform slide_out:
    xoffset 0
    alpha 1.0
    ease 0.3 xoffset 40 alpha 0.0

transform slide_out_left:
    xoffset 0
    alpha 1.0
    ease 0.3 xoffset -40 alpha 0.0

#Main menu buttons anims:

transform mm:
    alpha 0.5

    on hover:
        linear 0.2 alpha 1.0

    on idle:
        linear 0.2 alpha 0.5

transform entermm:
    alpha 0.0
    linear 2.0 alpha 1.0

# -------------------------------------------------
#PAUSE SCREEN
transform left_move:
    xoffset 0

    on hover:
        linear 0.2 xoffset -10

    on idle:
        linear 0.2 xoffset 0
transform fade_in_slow:
    alpha 0.0
    linear 1.5 alpha 1.0

transform slide_in_left:
    xoffset -50
    alpha 0.0
    easein 0.5 xoffset 0 alpha 1.0

transform slide_in:
    xoffset 20
    alpha 0.0
    easein 0.7 xoffset 0 alpha 1.0

transform enter_ftop:
    yoffset -30
    alpha 0.0
    easein 0.5 yoffset 0 alpha 1.0
transform enter_fbottom:
    yoffset 30
    alpha 0.0
    easein 0.5 yoffset 0 alpha 1.0

transform pulse:
    pause 2.0
    easein 0.18 zoom 1.04
    easeout 0.18 zoom 1.0
    pause 0.12
    easein 0.14 zoom 1.02
    easeout 0.16 zoom 1.0
    pause 2.0
    repeat

transform gallery_hover:
    on hover:
        easein 0.15 zoom 1.0090
    on idle:
        easeout 0.20 zoom 1.0



# Basic anims




transform fade_in:
    alpha 0.0
    linear 0.8 alpha 1.0

transform o_h: #Opacity on hover
    on hover:
        linear 0.2 alpha 1.0

    on idle:
        linear 0.2 alpha 0.5

transform s_up: #Slide up
    yoffset 50
    alpha 0.0
    linear 0.3 yoffset 0 alpha 1.0

transform s_up_slow: #Slide up but slow
    yoffset 20
    alpha 0.0
    linear 0.5 yoffset 0 alpha 1.0

transform s_down: #Slide down
    yoffset -50
    alpha 0.0
    linear 0.3 yoffset 0 alpha 1.0

transform zoomin:
    on hover:
        linear 0.2 zoom 1.05
    on idle:
        linear 0.2 zoom 1.0




#Side menu

transform m:
    on hover:
        easein 0.3 xoffset 10
    on idle:
        easein 0.3 xoffset 0

##

transform popit:
    zoom 0.5
    alpha 0.0
    linear 0.2 zoom 1.0 alpha 1.0

transform s_in:
    xoffset -200
    alpha 0.0
    linear 0.3 xoffset 0 alpha 1.0

transform l_in:
    xoffset -200
    alpha 0.0
    linear 0.3 xoffset 0 alpha 1.0

##Save/Load

transform slots:
    on hover:
        linear 0.1 alpha 1.0
    on idle:
        linear 0.1 alpha 0.8

## Quick Menu

transform qm:
    on hover:
        linear 0.2 yoffset -10
    on idle:
        linear 0.2 yoffset 0

transform choice:
    on hover:
        linear 0.2 xoffset -10
    on idle:
        linear 0.2 xoffset 0

#Gallery anims

transform glow:
    alpha 0.5
    linear 0.7 alpha 1.0
    linear 0.7 alpha 0.3
    repeat

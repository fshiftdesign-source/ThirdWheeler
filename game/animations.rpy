
# This file contains the transforms used for animations in the game.

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

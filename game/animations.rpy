

# This file contains the transforms used for animations in the game.
transform title_pause:
    subpixel True
    anchor (0.5, 0.5)
    pos (0.5, 0.5) 
    
    xoffset 0
    yoffset 0
    
    parallel:
        easein_quad 3.5 xoffset -25
        easeout_quad 3.5 xoffset 25
        repeat
        
    parallel:
        easein_quad 4.2 yoffset 15
        easeout_quad 4.2 yoffset -15
        repeat

    parallel:
        easein_quad 5.0 rotate -1.5
        easeout_quad 5.0 rotate 1.5
        repeat
transform slot_enter(delay=0.0):
    alpha 0.0
    xoffset -30
    pause delay
    linear 0.4 alpha 1.0 xoffset 0
transform fade_overlay:
    subpixel True
    alpha 0.0
    easein 0.2 alpha 0.6
    easeout 0.3 alpha 1.0
transform star:
    subpixel True
    xoffset -30
    alpha 0.0
    easein 0.5 xoffset 0 alpha 1.0
transform ripple:
    subpixel True
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    
    alpha 0.0
    xzoom 0.8
    yzoom 0.2
    
    parallel:
        
        easein 0.1 xzoom 1.03 yzoom 1.03
        easeout 0.25 xzoom 1.0 yzoom 1.0
    parallel:
        
        linear 0.1 alpha 1.0
        
        linear 0.32 alpha 0.0
transform fadechoice:
    subpixel True
    alpha 0.0
    linear 0.5 alpha 0.6

transform opacitymm:
    subpixel True
    alpha 0.5

    on hover:
        linear 0.2 alpha 1.0

    on idle:
        linear 0.2 alpha 0.8
transform mm:
    subpixel True
    alpha 0.5

    on hover:
        linear 0.2 alpha 1.0

    on idle:
        linear 0.2 alpha 0.5
transform opacity_confirm:
    subpixel True
    alpha 0.0
    easein 0.2 alpha 1.0

transform zoom:
    xalign 0.5
    yalign 0.5
    zoom 1.09

# -------------------------------------------------
#PAUSE SCREEN
transform left_move:
    subpixel True
    xoffset 0

    on hover:
        linear 0.2 xoffset -10

    on idle:
        linear 0.2 xoffset 0
transform fade_in_slow:
    subpixel True
    alpha 0.0
    linear 1.5 alpha 1.0

transform slide_in_left:
    subpixel True
    xoffset -50
    alpha 0.0
    easein 0.5 xoffset 0 alpha 1.0

transform slide_in:
    subpixel True
    xoffset 20
    alpha 0.0
    easein 0.7 xoffset 0 alpha 1.0

transform enter_ftop:
    subpixel True
    yoffset -30
    alpha 0.0
    easein 0.5 yoffset 0 alpha 1.0
transform enter_fbottom:
    subpixel True
    yoffset 30
    alpha 0.0
    easein 0.5 yoffset 0 alpha 1.0

transform pulse:
    subpixel True
    pause 2.0
    easein 0.18 zoom 1.04
    easeout 0.18 zoom 1.0
    pause 0.12
    easein 0.14 zoom 1.02
    easeout 0.16 zoom 1.0
    pause 2.0
    repeat

transform gallery_hover:
    subpixel True
    on hover:
        easein 0.15 zoom 1.0090
    on idle:
        easeout 0.20 zoom 1.0


transform fade_in:
    subpixel True
    alpha 0.0
    linear 0.8 alpha 1.0

transform s_down: #Slide down
    subpixel True
    yoffset -50
    alpha 0.0
    linear 0.3 yoffset 0 alpha 1.0

transform zoomin:
    subpixel True
    on hover:
        linear 0.2 zoom 1.05
    on idle:
        linear 0.2 zoom 1.0




#Side menu

transform m:
    subpixel True
    on hover:
        easein 0.3 xoffset 5
    on idle:
        easein 0.3 xoffset 0

##

transform slots:
    subpixel True
    on hover:
        linear 0.1 alpha 1.0
    on idle:
        linear 0.1 alpha 0.8

## Quick Menu

transform qm:
    subpixel True
    on hover:
        linear 0.2 yoffset -10
    on idle:
        linear 0.2 yoffset 0

transform bottle_button(rot=0):
    subpixel True

    anchor (0.5, 0.5)

    rotate rot

    on hover:
        zoom 1.05

    on idle:
        zoom 1.0

# SLOT

transform slot_number:
    subpixel True

    rotate 12

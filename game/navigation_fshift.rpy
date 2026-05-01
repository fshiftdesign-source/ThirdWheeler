# =================================================
# STARS
# =================================================

image stars = "gui/test.png"
image stars_der = "gui/test_2.png"


# =================================================
# STARS | Menu animation script
# =================================================

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

    repeat


# =================================================
# STARS SCREEN
# =================================================

screen stars_screen():

    hbox:
        spacing -40

        add "stars":
            at swing_soft
            xoffset 300

        add "stars_der":
            at swing_soft_reversed
            xoffset 60


# =================================================
# NAVIGATION BUTTON HOVER
# =================================================

transform nav_button_hover:

    zoom 1.0

    on hover:
        ease 0.15 zoom 1.08

    on idle:
        ease 0.15 zoom 1.0


# =================================================
# CUSTOM NAVIGATION
# Replaces default Ren'Py navigation
# =================================================

screen custom_navigation():

    zorder 50

    


    # =============================================
    # STARS
    # =============================================

    use stars_screen


    # =============================================
    # BUTTONS
    # =============================================

    hbox:
        xalign 0.5
        yalign 0.94

        spacing 46

        # SAVE
        imagebutton:

            idle "gui/menu-screens_fshift/navigation/save_idle.png"
            hover "gui/menu-screens_fshift/navigation/save_hover.png"

            at nav_button_hover

            action ShowMenu("save")


        # LOAD
        imagebutton:

            idle "gui/menu-screens_fshift/navigation/load_idle.png"
            hover "gui/menu-screens_fshift/navigation/load_hover.png"

            at nav_button_hover

            action ShowMenu("load")


        # SETTINGS
        imagebutton:

            idle "gui/menu-screens_fshift/navigation/settings_idle.png"
            hover "gui/menu-screens_fshift/navigation/settings_hover.png"

            at nav_button_hover

            action ShowMenu("preferences")


        # HISTORY
        imagebutton:

            idle "gui/menu-screens_fshift/navigation/history_idle.png"
            hover "gui/menu-screens_fshift/navigation/history_hover.png"

            at nav_button_hover

            action ShowMenu("history")


        # MAIN MENU
        imagebutton:

            idle "gui/menu-screens_fshift/navigation/home_idle.png"
            hover "gui/menu-screens_fshift/navigation/home_hover.png"

            at nav_button_hover

            action MainMenu()


        # QUIT
        imagebutton:

            idle "gui/menu-screens_fshift/navigation/quit_idle.png"
            hover "gui/menu-screens_fshift/navigation/quit_hover.png"

            at nav_button_hover

            action Quit(confirm=True)
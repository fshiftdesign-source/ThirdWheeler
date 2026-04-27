image bg_pause = "gui/menu-screens_fshift/pause/bg1.png"
image frame_pause = "gui/menu-screens_fshift/pause/frame2.png"
image column_pause = "gui/menu-screens_fshift/pause/column3.png"
image pause_title = "gui/menu-screens_fshift/pause/title4.png"


screen pause_screen():

    modal True
    zorder 100

    key "K_ESCAPE" action Hide("pause_screen")

    add "bg_pause":
        at fade_in
        align (0.5, 0.5)

    add "frame_pause":
        at fade_in_slow
        align (0.5, 0.5)

    add "column_pause":
        at slide_in
        align (1.0, 0.5)

    # 🏷️ TÍTULO
    add "pause_title":
        at slide_in_left
        align (0.65, 0.14)

    # 🎮 BOTÓN GALERÍA
    hbox:
        yoffset -100
        xalign 1.1
        xoffset -10
        at pulse

        imagebutton auto "gui/menu-screens_fshift/pause/gallery_%s.png":
            action ShowMenu("cg_gallery")
            at gallery_hover

    # 🔴 NEW (esto es lo importante que querías mantener)
    fixed:
        if has_new_cg():
            add "gui/menu-screens_fshift/pause/new.png":
                xalign 0.9
                yalign 0.1

    # ⬅️ BOTONES IZQUIERDA
    hbox:
        at enter_ftop
        xalign 0.15
        yoffset 50

        imagebutton auto "gui/menu-screens_fshift/pause/resume_%s.png":
            at qm
            yoffset -25
            action Hide("pause_screen")

        imagebutton auto "gui/menu-screens_fshift/pause/mainmenu_%s.png":
            at qm
            action MainMenu()

        imagebutton auto "gui/menu-screens_fshift/pause/history_%s.png":
            at qm
            action ShowMenu("history")

    # ➡️ BOTONES DERECHA
    vbox:
        xalign 0.80
        yalign 0.7
        spacing -5
        at enter_fbottom

        imagebutton auto "gui/menu-screens_fshift/pause/load_%s.png":
            at left_move
            action ShowMenu("load")

        imagebutton auto "gui/menu-screens_fshift/pause/save_%s.png":
            at left_move
            xoffset -75
            action ShowMenu("save")

        imagebutton auto "gui/menu-screens_fshift/pause/settings_%s.png":
            at left_move
            xoffset -75
            action ShowMenu("preferences")

        imagebutton auto "gui/menu-screens_fshift/pause/quit_%s.png":
            at left_move
            action Quit()

define config.keymap['game_menu'] = []

screen key_listener():
    key "K_ESCAPE" action If(
        renpy.get_screen("pause_screen"),
        Hide("pause_screen"),
        Show("pause_screen")
    )
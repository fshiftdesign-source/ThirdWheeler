image bg_pause = "gui/menu-screens_fshift/pause/bg1.png"
image frame_pause = "gui/menu-screens_fshift/pause/frame2.png"
image column_pause = "gui/menu-screens_fshift/pause/column3.png"
image pause_title = "gui/menu-screens_fshift/pause/title4.png"
    

default pause_hover = ""
screen ondas_agua_screen():
    zorder 250 
    
    
    add sistema_ondas.sm


screen pause_screen():
    
    modal True
    zorder 100
    use key_listener
    add "bg_pause":
        at fade_in
        align (0.5, 0.5)
    use stars_screen
    add "frame_pause":
        at fade_in_slow
        align (0.5, 0.5)

    add "column_pause":
        at slide_in
        align (1.0, 0.5)

    
    fixed:
        at title_pause
        add "pause_title":
            at slide_in_left
            align (0.65, 0.14)

    
    hbox:
        yoffset -100
        xalign 1.1
        xoffset -10
        at pulse

        imagebutton auto "gui/menu-screens_fshift/pause/gallery_%s.png":
            action ShowMenu("cg_gallery")
            at gallery_hover

    
    fixed:
        if has_new_cg():
            add "gui/menu-screens_fshift/pause/new.png":
                xalign 0.9
                yalign 0.1

    
    
    hbox:
        at enter_ftop
        xalign 0.15
        yoffset 50

        imagebutton auto "gui/menu-screens_fshift/pause/resume_%s.png":
            style "audio_1"
            at qm
            yoffset -25
            action Hide("pause_screen")
            hovered SetVariable("pause_hover", "resume")
            unhovered SetVariable("pause_hover", "")

        imagebutton auto "gui/menu-screens_fshift/pause/mainmenu_%s.png":
            style "audio_1"
            at qm
            action MainMenu()
            hovered SetVariable("pause_hover", "mainmenu")
            unhovered SetVariable("pause_hover", "")

        imagebutton auto "gui/menu-screens_fshift/pause/history_%s.png":
            style "audio_1"
            at qm
            action ShowMenu("history")
            hovered SetVariable("pause_hover", "history")
            unhovered SetVariable("pause_hover", "")
    fixed:
        yoffset 10
        if pause_hover == "resume":
            text "resume":
                at s_down
                font "fonts/Fredoka-Light.ttf"
                size 36
                xalign 0.14
                yalign 0.18
                style "qm_hover_outline"

        if pause_hover == "mainmenu":
            text "main menu":
                at s_down
                xalign 0.23
                yalign 0.13
                size gui.interface_text_size
                style "qm_hover_outline"

        if pause_hover == "history":
            text "history":
                at s_down
                xalign 0.3
                yalign 0.13
                size gui.interface_text_size
                style "qm_hover_outline"
    
    vbox:
        xalign 0.80
        yalign 0.7
        spacing -5
        at enter_fbottom

        imagebutton auto "gui/menu-screens_fshift/pause/load_%s.png":
            style "audio_2"
            at left_move
            action ShowMenu("load")

        imagebutton auto "gui/menu-screens_fshift/pause/save_%s.png":
            style "audio_2"
            at left_move
            xoffset -75
            action ShowMenu("save")

        imagebutton auto "gui/menu-screens_fshift/pause/settings_%s.png":
            style "audio_2"
            at left_move
            xoffset -75
            action ShowMenu("preferences")

        imagebutton auto "gui/menu-screens_fshift/pause/quit_%s.png":
            style "audio_2"
            at left_move
            action Quit()

define config.keymap['game_menu'] = []

screen key_listener():
    key "K_ESCAPE" action If(
        renpy.get_screen("pause_screen"),
        Hide("pause_screen"),
        Show("pause_screen")
    )
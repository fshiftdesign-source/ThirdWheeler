default rollback_side_pref = "left"




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

screen side_menu:
    tag menu
    fixed:
        xoffset 15
        if _in_replay or main_menu:
            pass
        else:
            imagebutton auto "gui/menu-screens_fshift/options/home_%s.png" action MainMenu():
                style "audio_4"
                xoffset 215
                yoffset 162
                at zoomin
        imagebutton auto "gui/menu-screens_fshift/options/load_%s.png" action ShowMenu("load"):
            style "audio_4"
            xoffset 213
            yoffset 309
            at zoomin

        
        imagebutton auto "gui/menu-screens_fshift/options/save_%s.png" action ShowMenu("save"):
            style "audio_4"
            xoffset 231
            yoffset 455
            at zoomin

        
        imagebutton auto "gui/menu-screens_fshift/options/options_%s.png" action ShowMenu("preferences"):
            style "audio_4"
            xoffset 275
            yoffset 605
            at zoomin

        
        imagebutton auto "gui/menu-screens_fshift/options/history_%s.png" action ShowMenu("history"):
            style "audio_4"
            xoffset 363
            yoffset 745
            at zoomin

        
        imagebutton auto "gui/menu-screens_fshift/options/quit_%s.png" action Quit(confirm=True):
            style "audio_4"
            xoffset 475
            yoffset 869
            at zoomin

screen background_pattern():
    add "moving_pattern" at diagonal_scroll

screen back():
    
    fixed:
        imagebutton auto "gui/back_%s.png":
            style "audio_2"
            action Return()
            xoffset -60
            yoffset 811
            at slots
screen preferences():
    
    tag menu

    add "gui/menu-screens_fshift/options/bg_1.png"
    
    add "gui/menu-screens_fshift/options/bg_2.png":
        xalign 1.0


    use background_pattern
    

    add "gui/menu-screens_fshift/options/waves.png"


    key "K_ESCAPE" action Return()

    add "gui/menu-screens_fshift/options/title.png":
        xalign 0.52
        yoffset 50
    vbox:
        xoffset -420
        use stars_screen()
        
    use side_menu
    use back
 
    fixed:
        xpos 600
        ypos 250

        hbox:
            spacing 120

           
            vbox:
                spacing 20

                # DISPLAY
                text "Display" style "pref_title"

                hbox:
                    spacing 30

                    imagebutton:
                        idle "gui/menu-screens_fshift/options/fullscreen_idle.png"
                        hover "gui/menu-screens_fshift/options/fullscreen_hover.png"
                        action Preference("display", "fullscreen")
                        at qm

                    imagebutton:
                        idle "gui/menu-screens_fshift/options/windowed_idle.png"
                        hover "gui/menu-screens_fshift/options/windowed_hover.png"
                        action Preference("display", "window")
                        at qm

                # ROLLBACK
                text "Rollback" style "pref_title"

                hbox:
                    spacing 5

                    # LEFT
                    hbox:
                        spacing 10
                        yalign 0.5

                        imagebutton:
                            idle "gui/menu-screens_fshift/options/check_idle.png"
                            hover "gui/menu-screens_fshift/options/check_selected.png"
                            selected_idle "gui/menu-screens_fshift/options/check_selected.png"

                            xsize 53
                            ysize 53

                            action [
                                SetVariable("rollback_side_pref", "left"),
                                Preference("rollback side", "left")
                            ]

                            selected (rollback_side_pref == "left")

                        text "Left" style "pref_text" yalign 0.5

                    # RIGHT
                    hbox:
                        spacing 10
                        yalign 0.5

                        imagebutton:
                            idle "gui/menu-screens_fshift/options/check_idle.png"
                            hover "gui/menu-screens_fshift/options/check_selected.png"
                            selected_idle "gui/menu-screens_fshift/options/check_selected.png"

                            xsize 53
                            ysize 53

                            action [
                                SetVariable("rollback_side_pref", "right"),
                                Preference("rollback side", "right")
                            ]

                            selected (rollback_side_pref == "right")

                        text "Right" style "pref_text" yalign 0.5

                    # DISABLE
                    hbox:
                        spacing 10
                        yalign 0.5

                        imagebutton:
                            idle "gui/menu-screens_fshift/options/check_idle.png"
                            hover "gui/menu-screens_fshift/options/check_selected.png"
                            selected_idle "gui/menu-screens_fshift/options/check_selected.png"

                            xsize 53
                            ysize 53

                            action [
                                SetVariable("rollback_side_pref", "disable"),
                                Preference("rollback side", "disable")
                            ]

                            selected (rollback_side_pref == "disable")

                        text "Disable" style "pref_text" yalign 0.5

                # SKIPPING
                text "Skipping" style "pref_title"

                hbox:
                    spacing 15

                    hbox:
                        spacing 10

                        imagebutton:
                            idle "gui/menu-screens_fshift/options/check_idle.png"
                            hover "gui/menu-screens_fshift/options/check_selected.png"
                            selected_idle "gui/menu-screens_fshift/options/check_selected.png"

                            xsize 53
                            ysize 53

                            action Preference("after choices", "toggle")

                        text "After Choices" style "pref_text"

                    hbox:
                        spacing 10

                        imagebutton:
                            idle "gui/menu-screens_fshift/options/check_idle.png"
                            hover "gui/menu-screens_fshift/options/check_selected.png"
                            selected_idle "gui/menu-screens_fshift/options/check_selected.png"

                            xsize 53
                            ysize 53

                            action Preference("skip", "toggle")

                        text "All Text" style "pref_text"

          
            vbox:
                spacing 10

                # MUSIC
                text "Music Volume" style "pref_title"

                bar:
                    style "custom_slider"
                    value Preference("music volume")

                # SFX
                text "SFX Volume" style "pref_title"

                bar:
                    style "custom_slider"
                    value Preference("sound volume")

                # TEXT SPEED
                text "Text Speed" style "pref_title"

                bar:
                    style "custom_slider"
                    value Preference("text speed")

                # AUTO
                text "Auto Speed" style "pref_title"

                bar:
                    style "custom_slider"
                    value Preference("auto-forward time")
    fixed:
        

        imagebutton auto "gui/menu-screens_fshift/pause/gallery_%s.png":
            yoffset -100
            xalign 1.1
            xoffset -10
            action ShowMenu("cg_gallery")
            at gallery_hover
                


style pref_title:
    size 40
    color "#82ABD4"

    outlines [
        (7, "#A3C5E0", 0, 2),      
        (4, "#ffffffff", 0, 0)     
    ]
style pref_text:
    size 28
    color "#869dc9"

style custom_slider is slider:
    xsize 424
    ysize 58
    

    left_bar Frame("gui/menu-screens_fshift/options/slider_full.png", 0, 0)
    right_bar Frame("gui/menu-screens_fshift/options/slider_empty.png", 0, 0)
    
    thumb "gui/menu-screens_fshift/options/thumb_idle.png"
    thumb_offset -24
    
transform slider_thumb_center:
    yalign 0.5
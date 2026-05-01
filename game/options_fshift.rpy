default rollback_side_pref = "left"


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





##screen options
screen preferences():

    tag menu

    add "gui/menu-screens_fshift/options/bg_1.png"
    add "gui/menu-screens_fshift/options/bg_2.png":
        xalign 1.0
    add "gui/menu-screens_fshift/options/corner_stars.png":
        xalign 1.0
    use background_pattern
    #use stars_screen
    use navigation

    key "K_ESCAPE" action Return()

    # =========================
    # TITLE
    # =========================
    add "gui/menu-screens_fshift/options/title.png":
        xalign .52
        yoffset 50

    # =========================
    # LEFT COLUMN
    # =========================
    
    fixed:
        xpos 350
        ypos 250

        vbox:
            spacing 30

            # DISPLAY
            text "Display" style "pref_title"

            hbox:
                spacing 30
                imagebutton:
                    idle "gui/menu-screens_fshift/options/fullscreen_idle.png"
                    hover "gui/menu-screens_fshift/options/fullscreen_hover.png"
                    action Preference("display", "fullscreen")

                imagebutton:
                    idle "gui/menu-screens_fshift/options/windowed_idle.png"
                    hover "gui/menu-screens_fshift/options/windowed_hover.png"
                    action Preference("display", "window")

                

            # ROLLBACK
            text "Rollback" style "pref_title"

            hbox:
                spacing 15

                # LEFT
                hbox:
                    spacing 10
                    yalign 0.5

                    imagebutton:
                        idle "gui/menu-screens_fshift/options/check_idle.png"
                        hover "gui/menu-screens_fshift/options/check_selected.png"
                        selected_idle "gui/menu-screens_fshift/options/check_selected.png"

                        xsize 54
                        ysize 54
                        
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

                        xsize 54
                        ysize 54
                        

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

                        xsize 54
                        ysize 54
                        

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
                        action Preference("after choices", "toggle")
                    text "After Choices" style "pref_text"

                hbox:
                    spacing 10
                    imagebutton:
                        idle "gui/menu-screens_fshift/options/check_idle.png"
                        hover "gui/menu-screens_fshift/options/check_selected.png"
                        action Preference("skip", "toggle")
                    text "All Text" style "pref_text"

    # =========================
    # RIGHT COLUMN
    # =========================
    fixed:
        xpos 1000
        ypos 250

        # MUSIC
        text "Music Volume" style "pref_title"

        bar:
            ypos 60
            style "custom_slider"
            value Preference("music volume")

        # SFX
        text "SFX Volume" style "pref_title":
            ypos 140

        bar:
            ypos 200
            style "custom_slider"
            value Preference("sound volume")

        # TEXT SPEED
        text "Text Speed" style "pref_title":
            ypos 280

        bar:
            ypos 340
            style "custom_slider"
            value Preference("text speed")

        # AUTO
        text "Auto Speed" style "pref_title":
            ypos 420

        bar:
            ypos 480
            style "custom_slider"
            value Preference("auto-forward time")


style pref_title:
    size 40
    color "#8fabdf"
    outlines [(4, "#FFFFFF80", 0, 0)]

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
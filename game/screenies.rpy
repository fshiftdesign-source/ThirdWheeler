screen orbital_choice(items):
    # items: list of (caption, value, dir)
    # only for 2/3 options
    zorder 200
    modal True

    fixed:
        xysize (config.screen_width, config.screen_height)

        $ count = len(items)

        for idx, (caption, value, dir) in enumerate(items):

            # Default positions
            $ xpos = 0.5
            $ ypos = 0.5

            if count == 3:
                if idx == 0:
                    $ xpos, ypos = 0.20, 0.62
                elif idx == 1:
                    $ xpos, ypos = 0.50, 0.22
                else:
                    $ xpos, ypos = 0.80, 0.62

            elif count == 2:
                if idx == 0:
                    $ xpos, ypos = 0.30, 0.62
                else:
                    $ xpos, ypos = 0.70, 0.62

            else:
                $ xpos, ypos = 0.50, 0.22

            button:
                xalign xpos
                yalign ypos
                xsize 600
                ysize 110

                action Return(value)

                hovered SetVariable("mc_dir", dir)
                unhovered SetVariable("mc_dir", "center")

                # Blue button with white text
                background Solid("#1E4AFFCC")
                hover_background Solid("#3A63FFFF")
                padding (20, 16)

                at choice_pop

                text caption:
                    xalign 0.5
                    yalign 0.5
                    color "#FFFFFF"
                    size 34
                    outlines [ (3, "#000000CC", 0, 0) ]
                    at choice_text_pop

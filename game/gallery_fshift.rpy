init python:

    TOTAL_CGS = 8
    ITEMS_PER_PAGE = 4
    GALLERY_MAX_PAGE = max(0, (TOTAL_CGS - 1) // ITEMS_PER_PAGE)

    config.overlay_screens.append("key_listener")

    if not hasattr(persistent, "cg_unlocked") or persistent.cg_unlocked is None:
        persistent.cg_unlocked = [False] * (TOTAL_CGS + 1)

    if not hasattr(persistent, "cg_seen") or persistent.cg_seen is None:
        persistent.cg_seen = [False] * (TOTAL_CGS + 1)

    def unlock_cg(index):
        if index <= TOTAL_CGS:
            persistent.cg_unlocked[index] = True
            renpy.save_persistent()

    def mark_cg_seen(index):
        if index < len(persistent.cg_seen):
            persistent.cg_seen[index] = True
            renpy.save_persistent()

    def has_new_cg():
        for i in range(1, TOTAL_CGS + 1):
            if persistent.cg_unlocked[i] and not persistent.cg_seen[i]:
                return True
        return False

transform cg_thumb:
    xysize (380, 280)
    fit "contain"


screen cg_gallery():

    tag menu
    modal True

    default page = 0

    key "K_ESCAPE" action Return()

    add "gui/menu-screens_fshift/cg_gallery/bg_base.png"
    

    fixed:
        $ start = page * ITEMS_PER_PAGE

   
        $ col1_x = 935
        $ col2_x = 1380
        $ gap_y = 260

        $ positions = [
            (col1_x, 400),
            (col2_x, 400),
            (col1_x, 397 + gap_y),
            (col2_x, 397 + gap_y),
        ]

        for i in range(ITEMS_PER_PAGE):

            $ cg_index = start + i + 1

            if cg_index <= TOTAL_CGS:

                $ xpos, ypos = positions[i]

                if cg_index < len(persistent.cg_unlocked) and persistent.cg_unlocked[cg_index]:


                    button:
                        at zoomin
                        xpos xpos
                        ypos ypos
                        anchor (0.5, 0.5)

                        add "images/cg/cg%d.png" % cg_index at cg_thumb

                        action Show("cg_full", cg_number=cg_index)
  
                else:

                
                    button:
                        xpos xpos
                        ypos ypos
                        anchor (0.5, 0.5)

                        add "images/cg/locked.png" at cg_thumb

                        action NullAction()

    add "gui/menu-screens_fshift/cg_gallery/bg_gallery.png"
    


    if page > 0:
        imagebutton auto "gui/menu-screens_fshift/cg_gallery/arrow_l_%s.png":
            at gallery_hover
            xalign 0.28
            xoffset 30
            yalign 0.5
            action SetScreenVariable("page", page - 1)

  
    if page < GALLERY_MAX_PAGE:
        imagebutton auto "gui/menu-screens_fshift/cg_gallery/arrow_r_%s.png":
            at gallery_hover
            xalign 0.9
            xoffset 100
            yalign 0.5
            action SetScreenVariable("page", page + 1)

   
    text "[page+1] / [GALLERY_MAX_PAGE+1]":
        xalign 0.6
        yalign 0.9
        yoffset -84
        xoffset 10
        size 40
        color "#ffffff"
        outlines [(2, "#00000080", 0, 0)]
    fixed:
        xoffset -420
        use stars_screen
    use side_menu
    use back
    

transform cg_zoom_in:
    alpha 0.0
    zoom 0.70
    easein 0.35 alpha 1.0 zoom 1.0

transform cg_zoom_out:
    alpha 1.0
    zoom 1.0
    easeout 0.3 alpha 0.0 zoom 1.0
screen cg_full(cg_number):

    modal True

    default closing = False   

    on "show" action Function(mark_cg_seen, cg_number)
    fixed:
        add "images/cg/cg%d.png" % cg_number:
            align (0.5, 0.5)
            fit "contain"
            at (cg_zoom_out if closing else cg_zoom_in)   

    
    key "mouseup_1" action If(closing, NullAction(), [SetScreenVariable("closing", True), Hide("cg_full", transition=Dissolve(0.3))])
    key "mouseup_3" action If(closing, NullAction(), [SetScreenVariable("closing", True), Hide("cg_full", transition=Dissolve(0.3))])
    key "K_ESCAPE"  action If(closing, NullAction(), [SetScreenVariable("closing", True), Hide("cg_full", transition=Dissolve(0.3))])


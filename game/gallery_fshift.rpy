init python:

    TOTAL_CGS = 8
    ITEMS_PER_PAGE = 4

    GALLERY_MAX_PAGE = max(0, (TOTAL_CGS - 1) // ITEMS_PER_PAGE)

    if not hasattr(persistent, "cg_unlocked") or persistent.cg_unlocked is None:
        persistent.cg_unlocked = [False] * (TOTAL_CGS + 1)

    def unlock_cg(index):
        if index <= TOTAL_CGS:
            if index >= len(persistent.cg_unlocked):
                persistent.cg_unlocked.extend(
                    [False] * (index - len(persistent.cg_unlocked) + 1)
                )
            persistent.cg_unlocked[index] = True
            renpy.save_persistent()


# 🎯 THUMB CONSISTENTE
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

        # 🧠 grilla centrada REAL
        $ center_x = 1150
        $ gap_x = 400
        $ gap_y = 260

        $ positions = [
            (center_x - gap_x//2, 400),
            (center_x + gap_x//2, 400),
            (center_x - gap_x//2, 400 + gap_y),
            (center_x + gap_x//2, 400 + gap_y),
        ]

        for i in range(ITEMS_PER_PAGE):

            $ cg_index = start + i + 1

            if cg_index <= TOTAL_CGS:

                $ xpos, ypos = positions[i]

                if cg_index < len(persistent.cg_unlocked) and persistent.cg_unlocked[cg_index]:

                    # ✅ DESBLOQUEADA
                    button:
                        xpos xpos
                        ypos ypos
                        anchor (0.5, 0.5)

                        add "images/cg/cg%d.png" % cg_index at cg_thumb

                        action Show("cg_full", cg_number=cg_index)

                else:

                    # 🔒 BLOQUEADA
                    button:
                        xpos xpos
                        ypos ypos
                        anchor (0.5, 0.5)

                        add "images/cg/locked.png" at cg_thumb

                        action NullAction()

    add "gui/menu-screens_fshift/cg_gallery/bg_gallery.png"
    use navigation

    # ◀
    if page > 0:
        imagebutton:
            at glow
            xalign 0.1
            yalign 0.5
            idle "gui/menu-screens_fshift/cg_gallery/arrow_l.png"
            hover "gui/menu-screens_fshift/cg_gallery/arrow_l.png"
            action SetScreenVariable("page", page - 1)

    # ▶
    if page < GALLERY_MAX_PAGE:
        imagebutton:
            at glow
            xalign 0.9
            yalign 0.5
            idle "gui/menu-screens_fshift/cg_gallery/arrow_r.png"
            hover "gui/menu-screens_fshift/cg_gallery/arrow_r.png"
            action SetScreenVariable("page", page + 1)

    # 📄 páginas centrado
    text "[page+1] / [GALLERY_MAX_PAGE+1]":
        xalign 0.5
        yalign 0.9
        size 40
        color "#ffffff"
        outlines [(2, "#00000080", 0, 0)]


screen cg_full(cg_number):

    modal True

    add Solid("#000000")

    add "images/cg/cg%d.png" % cg_number:
        align (0.5, 0.5)
        fit "contain"

    key "mouseup_1" action Hide("cg_full")
    key "mouseup_3" action Hide("cg_full")
    key "K_ESCAPE" action Hide("cg_full")
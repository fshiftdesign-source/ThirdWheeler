image bg_pause = "gui/menu-screens_fshift/pause/bg1.png"
image frame_pause = "gui/menu-screens_fshift/pause/frame2.png"
image column_pause = "gui/menu-screens_fshift/pause/column3.png"
image pause_title = "gui/menu-screens_fshift/pause/title4.png"



# -------------------------
# 🧠 PAUSE SCREEN
# -------------------------

screen pause_screen():

    modal True
    zorder 100

    default closing = False
    default next_action = None

    # ESC → iniciar cierre
    key "K_ESCAPE" action SetScreenVariable("closing", True)

    # -------------------------
    # 🎨 FONDOS
    # -------------------------

    add "bg_pause":
        at (fade_out if closing else fade_in)
        align (0.5, 0.5)

    add "frame_pause":
        at (fade_out if closing else fade_in_slow)
        align (0.5, 0.5)

    add "column_pause":
        at (slide_out if closing else slide_in)
        align (1.0, 0.5)

    # -------------------------
    # 🏷️ TÍTULO
    # -------------------------

    add "pause_title":
        at (slide_out_left if closing else slide_in_left)
        align (0.65, 0.14)

    # -------------------------
    # 🎮 BOTÓN GALERÍA
    # -------------------------

    hbox:
        yoffset -100
        xalign 1.1
        xoffset -10

        imagebutton auto "gui/menu-screens_fshift/pause/gallery_%s.png":
            action [
                SetScreenVariable("next_action", ShowMenu("cg_gallery")),
                SetScreenVariable("closing", True)
            ]

    # 🔴 indicador NEW
    fixed:
        if has_new_cg():
            add "gui/menu-screens_fshift/pause/new.png":
                xalign 0.9
                yalign 0.1

    # -------------------------
    # ⬅️ BOTONES IZQUIERDA
    # -------------------------

    hbox:
        xalign 0.15
        yoffset 50

        imagebutton auto "gui/menu-screens_fshift/pause/resume_%s.png":
            yoffset -20
            action [
                SetScreenVariable("next_action", Hide("pause_screen")),
                SetScreenVariable("closing", True)
            ]

        imagebutton auto "gui/menu-screens_fshift/pause/mainmenu_%s.png":
            action [
                SetScreenVariable("next_action", MainMenu()),
                SetScreenVariable("closing", True)
            ]

        imagebutton auto "gui/menu-screens_fshift/pause/history_%s.png":
            action [
                SetScreenVariable("next_action", ShowMenu("history")),
                SetScreenVariable("closing", True)
            ]

    # -------------------------
    # ➡️ BOTONES DERECHA
    # -------------------------

    vbox:
        xalign 0.80
        yalign 0.7
        spacing -5

        imagebutton auto "gui/menu-screens_fshift/pause/load_%s.png":
            action [
                SetScreenVariable("next_action", ShowMenu("load")),
                SetScreenVariable("closing", True)
            ]

        imagebutton auto "gui/menu-screens_fshift/pause/save_%s.png":
            action [
                SetScreenVariable("next_action", ShowMenu("save")),
                SetScreenVariable("closing", True)
            ]

        imagebutton auto "gui/menu-screens_fshift/pause/settings_%s.png":
            action [
                SetScreenVariable("next_action", ShowMenu("preferences")),
                SetScreenVariable("closing", True)
            ]

        imagebutton auto "gui/menu-screens_fshift/pause/quit_%s.png":
            action [
                SetScreenVariable("next_action", Quit()),
                SetScreenVariable("closing", True)
            ]

    # -------------------------
    # 🌑 OVERLAY FADE (tipo dissolve)
    # -------------------------

    if closing:
        add Solid("#000"):
            at (fade_overlay if closing else fade_overlay_out)
    # -------------------------
    # ⏱️ CIERRE REAL + ACCIÓN
    # -------------------------

    fixed:
        if closing:
            timer 0.3 action [
                Hide("pause_screen"),
                If(next_action, next_action)
            ]


# -------------------------
# ⌨️ KEY LISTENER
# -------------------------

define config.keymap['game_menu'] = []

screen key_listener():
    key "K_ESCAPE" action If(
        renpy.get_screen("pause_screen"),
        SetScreenVariable("closing", True),
        Show("pause_screen")
    )


# -------------------------
# 📌 LABELS
# -------------------------

label pause_call:
    call screen pause_screen
    return

label open_gallery:
    $ persistent.cg_seen = persistent.cg_unlocked[:]
    $ renpy.save_persistent()
    call screen cg_gallery
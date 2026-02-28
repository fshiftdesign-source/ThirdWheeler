default mc_dir = "center"

image girl_head = ConditionSwitch(
    "mc_dir == 'left'",   "girl_left.png",
    "mc_dir == 'right'",  "girl_right.png",
    "True",               "girl_center.png",
)
transform choice_pop:
    anchor (0.5, 0.5)
    alpha 0.0
    zoom 0.75
    yoffset 20

    # Pop in
    parallel:
        easeout 0.18 alpha 1.0 yoffset 0
    easeout 0.18 zoom 1.08
    easein 0.10 zoom 1.00


transform choice_text_pop:
    alpha 0.0
    zoom 0.90

    easeout 0.18 alpha 1.0 zoom 1.00

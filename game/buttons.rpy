# DEFAULT
default action_pressed = None
default action_buttons_visible = True
default action_cooldown = False
default current_scene = "gtest"

# Per button availability
default fire_available  = True
default water_available = True
default earth_available = True
default wind_available  = True

define sayScreen = True

# LABEL MAPPING

init python:
    ACTION_LABELS = {
        "fire": {
            "gtest":   "test_chop",
            "swamp":   "swamp_walk",
            "cliff":   "cliff_jump",
            "eldritch":"forest_attack",
            "bandit":  "bandit_chop",
            "illusion":"chop_il",
            "tree":    "chop_severin_tree",
            "geralda": "chop_geralda",
            "dragun":  "dragon_mika_attack",
        },

        "water": {
            "gtest":   "test_block",
            "cliff":   "cliff_block",
            "eldritch":"forest_protect",
            "bandit":  "bandit_block",
            "illusion":"block_il",
            "geralda": "block_geralda",
        },

        "earth": {
            "gtest":   "test_mock",
            "eldritch":"forest_taunt",
            "bandit":  "bandit_mock",
            "illusion":"mock_il",
            "geralda": "mock_geralda",
            "dragun":  "dragon_mika_mock",
        },

        "wind": {
            "gtest":   "test_bolt",
            "swamp":   "swamp_turnback",
            "cliff":   "cliff_run",
            "eldritch":"forest_retreat",
            "bandit":  "bandit_bolt",
            "illusion":"bolt_il",
            "tree":    "bolt_severin_tree",
            "geralda": "bolt_geralda",
            "dragun":  "dragon_mika_bolt",
        },
    }

    # Per scene tooltips for each action
    ACTION_TOOLTIPS = {
        "fire": {
            "gtest":   "FIRE: ATTACK!",
            "swamp":   "FIRE: KEEP GOIN'!",
            "cliff":   "FIRE: JUMP!!!",
            "eldritch":"FIRE: GOO VIOLENCE!",
            "bandit":  "FIRE: SOCK 'EM!",
            "illusion":"FIRE: ATTACK!",
            "tree":    "FIRE: CHOP THE TREE!",
            "geralda": "FIRE: ATTACK THE ILLUSION!",
            "dragun":  "FIRE: SMASH!",
        },
        "water": {
            "gtest":   "WATER: GET 'IM TO HEAL ME!",
            "cliff":   "WATER: HOLY BUBBLE!",
            "eldritch":"WATER: PROTECT GERALD!",
            "bandit":  "WATER: BLOCK EM!",
            "illusion":"WATER: BE DEFENSIVE!",
            "geralda": "WATER: DEFEND GERALD!",
        },
        "earth": {
            "gtest":   "EARTH: TAUNT!",
            "eldritch":"EARTH: MOCK!!",
            "bandit":  "EARTH: MOCK 'EM!",
            "illusion":"EARTH: TALK BACK!",
            "geralda": "EARTH: TAUNT THE ILLUSION!",
            "dragun":  "EARTH: SASS!",
        },
        "wind": {
            "gtest":   "WIND: BOLT!",
            "swamp":   "WIND: TURN BACK!",
            "cliff":   "WIND: NOPE!",
            "eldritch":"WIND: RUN RUN RUN!",
            "bandit":  "WIND: BOLT!",
            "illusion":"WIND: RUN! RUN! RUN!",
            "tree":    "WIND: NOPE, BYE!",
            "geralda": "WIND: DRAG GERALD AWAY!",
            "dragun":  "WIND: PASS!",
        },
    }

    def get_action_tooltip(action, scene):
        # Helper so the screen code stays clean
        defaults = {
            "fire":  "FIRE.",
            "water": "WATER.",
            "earth": "EARTH.",
            "wind":  "WIND.",
        }
        return ACTION_TOOLTIPS.get(action, {}).get(scene, defaults.get(action, ""))


screen action_buttons():

    if action_buttons_visible and not action_cooldown:

        # Read current scene once
        $ scene = current_scene

        # Get tooltips for this scene
        $ fire_tip  = get_action_tooltip("fire", scene)
        $ water_tip = get_action_tooltip("water", scene)
        $ earth_tip = get_action_tooltip("earth", scene)
        $ wind_tip  = get_action_tooltip("wind", scene)

        # Get labels for this scene
        $ fire_label  = ACTION_LABELS.get("fire", {}).get(scene, None)
        $ water_label = ACTION_LABELS.get("water", {}).get(scene, None)
        $ earth_label = ACTION_LABELS.get("earth", {}).get(scene, None)
        $ wind_label  = ACTION_LABELS.get("wind", {}).get(scene, None)

        fixed:

            # FIRE
            if fire_available:
                imagebutton:
                    idle "chop.png"
                    hover "chop_hover.png"
                    action [
                        SetVariable("action_pressed", "fire"),
                        If(fire_label, Call(fire_label), NullAction())
                    ]
                    tooltip fire_tip
                    xpos 100 ypos 30
                    at swirl_in

            # WATER
            if water_available:
                imagebutton:
                    idle "block.png"
                    hover "block_hover.png"
                    action [
                        SetVariable("action_pressed", "water"),
                        If(water_label, Call(water_label), NullAction())
                    ]
                    tooltip water_tip
                    xpos 20 ypos 100
                    at swirl_in

            # EARTH
            if earth_available:
                imagebutton:
                    idle "mock.png"
                    hover "mock_hover.png"
                    action [
                        SetVariable("action_pressed", "earth"),
                        If(earth_label, Call(earth_label), NullAction())
                    ]
                    tooltip earth_tip
                    xpos 180 ypos 100
                    at swirl_in

            # WIND
            if wind_available:
                imagebutton:
                    idle "bolt.png"
                    hover "bolt_hover.png"
                    action [
                        SetVariable("action_pressed", "wind"),
                        If(wind_label, Call(wind_label), NullAction())
                    ]
                    tooltip wind_tip
                    xpos 100 ypos 180
                    at swirl_in

            $ tooltip = GetTooltip()

        if tooltip:

            add Solid("#0008")

            frame:
                xalign 0.5
                yalign 0.5
                padding (40, 22)
                background Solid("#0000")

                text tooltip:
                    xalign 0.5
                    yalign 0.5
                    size 72
                    bold True
                    color "#ffffff"
                    outlines [(6, "#000000", 0, 0)]
                    textalign 0.5


transform swirl_in(d=0.35, radius=40, start_zoom=0.2, spins=1.0):
    alpha 0.0
    zoom start_zoom
    xoffset radius
    yoffset 0
    rotate -180

    parallel:
        linear d alpha 1.0 zoom 1.0 rotate 0
    parallel:
        ease d xoffset 0 yoffset 0
    parallel:
        linear d rotate (spins * 360)

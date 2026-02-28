# DEFAULT
default action_pressed = None
default action_buttons_visible = True
default action_cooldown = False
default current_scene = "gtest"

# Per button availability
default chop_available = True
default block_available = True
default mock_available = True
default bolt_available = True

define sayScreen = True

# LABEL MAPPING

init python:
    ACTION_LABELS = {
        "chop": {
            "gtest": "test_chop",
            "swamp": "swamp_walk",
            "cliff": "cliff_jump",
            "eldritch": "forest_attack",
            "bandit": "bandit_chop",
            "illusion": "chop_il",
            "tree": "chop_severin_tree",
            "geralda": "chop_geralda",
            "dragun": "dragon_mika_attack",
        },

        "block": {
            "gtest": "test_block",
            "cliff": "cliff_block",
            "eldritch": "forest_protect",
            "bandit": "bandit_block",
            "illusion": "block_il",
            "geralda": "block_geralda",

        },

        "mock": {
            "gtest": "test_mock",
            "eldritch": "forest_taunt",
            "bandit": "bandit_mock",
            "illusion": "mock_il",
            "geralda": "mock_geralda",
            "dragun": "dragon_mika_mock",
        },

        "bolt": {
            "gtest": "test_bolt",
            "swamp": "swamp_turnback",
            "cliff": "cliff_run",
            "eldritch": "forest_retreat",
            "bandit": "bandit_bolt",
            "illusion": "bolt_il",
            "tree": "bolt_severin_tree",
            "geralda": "bolt_geralda",
            "dragun": "dragon_mika_bolt",
        },
    }

    # Per scene tooltips for each action
    ACTION_TOOLTIPS = {
        "chop": {
            "gtest": "ATTACK!",
            "swamp": "KEEP GOIN'!",
            "cliff": "JUMP!!!",
            "eldritch": "GOO VIOLENCE!",
            "bandit": "SOCK 'EM!",
            "illusion": "ATTACK!",
            "tree": "CHOP THE TREE!",
            "geralda": "ATTACK THE ILLUSION!",
            "dragun": "SMASH!",
        },
        "block": {
            "gtest": "GET 'IM TO HEAL ME!",
            "cliff": "HOLY BUBBLE!",
            "eldritch": "PROTECT GERALD!",
            "bandit": "BLOCK EM!",
            "illusion": "BE DEFENSIVE!",
            "geralda": "DEFEND GERALD!",
        },
        "mock": {
            "gtest": "TAUNT!",
            "eldritch": "MOCK!!",
            "bandit": "MOCK 'EM!",
            "illusion": "TALK BACK!",
            "geralda": "TAUNT THE ILLUSION!",
            "dragun": "SASS!",
        },
        "bolt": {
            "gtest": "BOLT!",
            "swamp": "TURN BACK!",
            "cliff": "NOPE!",
            "eldritch": "RUN RUN RUN!",
            "bandit": "BOLT!",
            "illusion": "RUN! RUN! RUN!",
            "tree": "NOPE, BYE!",
            "geralda": "DRAG GERALD AWAY!",
            "dragun": "PASS!",
        },
    }

    def get_action_tooltip(action, scene):
        # Helper so the screen code stays clean
        defaults = {
            "chop": "Chop (Attack).",
            "block": "Block (Defend).",
            "mock": "Mock (Taunt).",
            "bolt": "Bolt (Run).",
        }
        return ACTION_TOOLTIPS.get(action, {}).get(scene, defaults.get(action, ""))


screen action_buttons():

    if action_buttons_visible and not action_cooldown:

        # Read current scene once
        $ scene = current_scene

        # Get tooltips for this scene
        $ chop_tip = get_action_tooltip("chop", scene)
        $ block_tip = get_action_tooltip("block", scene)
        $ mock_tip  = get_action_tooltip("mock", scene)
        $ bolt_tip  = get_action_tooltip("bolt", scene)

        # Get labels for this scene
        $ chop_label = ACTION_LABELS.get("chop", {}).get(scene, None)
        $ block_label = ACTION_LABELS.get("block", {}).get(scene, None)
        $ mock_label = ACTION_LABELS.get("mock", {}).get(scene, None)
        $ bolt_label = ACTION_LABELS.get("bolt", {}).get(scene, None)

        fixed:

            # Chop (attack)
            if chop_available:
                imagebutton:
                    idle "chop.png"
                    hover "chop_hover.png"
                    action [
                        SetVariable("action_pressed", "chop"),
                        If(chop_label, Call(chop_label), NullAction())
                    ]
                    tooltip chop_tip
                    xpos 100 ypos 30
                    at swirl_in

            # Block (defend)
            if block_available:
                imagebutton:
                    idle "block.png"
                    hover "block_hover.png"
                    action [
                        SetVariable("action_pressed", "block"),
                        If(block_label, Call(block_label), NullAction())
                    ]
                    tooltip block_tip
                    xpos 20 ypos 100
                    at swirl_in

            # Mock (taunt)
            if mock_available:
                imagebutton:
                    idle "mock.png"
                    hover "mock_hover.png"
                    action [
                        SetVariable("action_pressed", "mock"),
                        If(mock_label, Call(mock_label), NullAction())
                    ]
                    tooltip mock_tip
                    xpos 180 ypos 100
                    at swirl_in

            # Bolt (run)
            if bolt_available:
                imagebutton:
                    idle "bolt.png"
                    hover "bolt_hover.png"
                    action [
                        SetVariable("action_pressed", "bolt"),
                        If(bolt_label, Call(bolt_label), NullAction())
                    ]
                    tooltip bolt_tip
                    xpos 100 ypos 180
                    at swirl_in

            $ tooltip = GetTooltip()

        if tooltip:

            # optional: dim behind tooltip a bit (comment out if you don't want it)
            add Solid("#0008")

            frame:
                xalign 0.5
                yalign 0.5
                padding (40, 22)
                background Solid("#0000")  # keep transparent; change if you want a box

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

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    scene black
    $ mc_dir = "center"

    show girl_head at Position(xcenter=0.5, yanchor=1.0, ypos=900)

    "Testtt"
    call screen orbital_choice([
        ("Check the left path", "left_path", "left"),
        ("Think for a moment", "middle_path", "center"),
        ("Check the right path", "right_path", "right"),
    ])
    $ result = _return

    jump expression result


label left_path:
    "You chose the left option."
    jump testim


label middle_path:
    "You chose the middle option."
    jump testim


label right_path:
    "You chose the right option."
    jump testim

label testim:

    # MENU BUTTONS – elemental version

    "Don't click, only for show."

    $ fire_available  = True
    $ water_available = True
    $ earth_available = True
    $ wind_available  = False

    $ current_scene = "gtest"
    $ action_buttons_visible = True

    show screen action_buttons

    jump testim2

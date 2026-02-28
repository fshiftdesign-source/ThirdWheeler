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
    return

label middle_path:
    "You chose the middle option."
    return

label right_path:
    "You chose the right option."
    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image placeholder = "bg_placeholder.png"

# The game starts here.

label start:
    scene black
    $ mc_dir = "center"

    jump particle_demo

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

label gallerytest:
    e "Unlocking CGs for testing."
    $ unlock_cg(1)
    e "CG 1 unlocked."
    $ unlock_cg(2)
    e "CG 2 unlocked."
    e "End of test."
    return

label options_test:
    show placeholder
    #show screen key_listener
    e "Testing options menu."

label particle_demo:

    show screen particle_system

    #$ active_particles = spawn_particles(960, 540)

    "Hacé click en cualquier parte."

    "Boom de partículas ✨"

    menu:
        "continuar":
            jump particle_demo
        "terminar":
            pass

    return
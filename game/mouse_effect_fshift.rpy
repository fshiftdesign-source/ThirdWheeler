# ==============================
# 🌊 RIPPLE SYSTEM
# usando tus imágenes actuales
# ==============================

default active_particles = []

init -20 python:
    config.gl2 = True

init -10 python:

    import random
    import time

    config.top_layers.append("particles")

    # ==============================
    # 🖼️ TUS IMÁGENES
    # ==============================

    PARTICLE_IMAGES = [
        "particle1.png",
        "particle2.png",
        "particle3.png",
        "particle4.png"
    ]

    MAX_PARTICLES = 50
    RIPPLE_LIFETIME = 0.6

    # ==============================
    # 🌊 CREAR RIPPLE
    # ==============================

    def add_particles(x, y):

        imgs = PARTICLE_IMAGES[:]
        random.shuffle(imgs)

        for i, img in enumerate(imgs):

            store.active_particles.append({
                "img": img,
                "x": x,
                "y": y,
                "time": time.time(),

                # primeras 2 internas
                "inner": i % 2 == 0,
            })

        # Limita partículas
        if len(store.active_particles) > MAX_PARTICLES:
            store.active_particles = store.active_particles[-MAX_PARTICLES:]

        renpy.restart_interaction()

    # ==============================
    # 🧹 LIMPIEZA
    # ==============================

    def cleanup_particles():

        now = time.time()

        store.active_particles = [
            p for p in store.active_particles
            if now - p["time"] < RIPPLE_LIFETIME
        ]


# ==============================
# 🌊 RIPPLE EXTERIOR
# ==============================

transform ripple_outer:

    alpha 1.0
    zoom 0.15

    parallel:
        easeout 0.55 zoom 1.5

    parallel:
        easeout 0.55 alpha 0.0


# ==============================
# 🌊 RIPPLE INTERIOR
# ==============================

transform ripple_inner:

    alpha 0.8
    zoom 0.05

    parallel:
        easeout 0.35 zoom 0.75

    parallel:
        easeout 0.35 alpha 0.0

# ==============================
# 🖱️ CLICK
# ==============================

label spawn_particles_click:

    $ x, y = renpy.get_mouse_pos()

    $ add_particles(x, y)

    return


# ==============================
# 🎬 SCREEN
# ==============================

screen particle_system():

    layer "particles"

    # Limpieza automática
    timer 0.05 repeat True action Function(cleanup_particles)

    # Click / tap
    key "mousedown_1" action Function(
        renpy.call_in_new_context,
        "spawn_particles_click"
    )

    for p in active_particles:

        add p["img"]:

            xpos p["x"]
            ypos p["y"]

            anchor (0.5, 0.5)

            if p["inner"]:
                at ripple_inner
            else:
                at ripple_outer
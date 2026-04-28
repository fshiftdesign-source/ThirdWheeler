# ==============================
# ✨ PARTICLE SYSTEM (IMPROVED)
# ==============================
default active_particles = []

init -20 python:
    config.gl2 = True

init -10 python:
    import random

    config.top_layers.append("particles")

    PARTICLE_IMAGES = [
        "particle1.png",
        "particle2.png",
        "particle3.png",
        "particle4.png"
    ]

    MAX_PARTICLES = 80   # 🔴 límite

    def spawn_particles(x, y, amount=6):  # 🔴 menos cantidad
        particles = []

        for i in range(amount):
            particles.append({
                "img": random.choice(PARTICLE_IMAGES),
                "x": x,
                "y": y,
                "dx": random.randint(-140, 140),
                "dy": random.randint(-140, 140),
                "rot": random.randint(-180, 180),
                "dur": random.uniform(0.3, 0.6),  # 🔴 menos duración
            })

        return particles


    def add_particles(x, y):

        store.active_particles.extend(spawn_particles(x, y))

        # 🔴 recorte (clave performance)
        if len(store.active_particles) > MAX_PARTICLES:
            store.active_particles = store.active_particles[-MAX_PARTICLES:]

    # ==============================
    # 🎲 GENERADOR
    # ==============================
    def spawn_particles(x, y, amount=12):

        particles = []

        for i in range(amount):
            particles.append({
                "img": random.choice(PARTICLE_IMAGES),
                "x": x,
                "y": y,

                # Movimiento
                "dx": random.randint(-180, 180),
                "dy": random.randint(-180, 180),

                # Rotación
                "rot": random.randint(-360, 360),

                # Duración
                "dur": random.uniform(0.5, 0.9),
            })

        return particles


    # ==============================
    # 🖱️ CLICK
    # ==============================
    def add_particles(x, y):

        # 👉 ACUMULA en vez de reemplazar
        store.active_particles.extend(spawn_particles(x, y))

        renpy.restart_interaction()

        


    def clear_particles_safe():

        # Limpia TODO (simple)
        store.active_particles = []

        renpy.restart_interaction()


# ==============================
# 🎬 ANIMACIÓN
# ==============================

transform particle_anim(dx, dy, rot, dur):

    alpha 1.0

    linear dur xoffset dx yoffset dy rotate rot alpha 0.0

# ==============================
label spawn_particles_click:

    $ x, y = renpy.get_mouse_pos()

    $ add_particles(x, y)

    return

screen particle_system():

    layer "particles"

    key "mousedown_1" action Function(renpy.call_in_new_context, "spawn_particles_click")

    for p in active_particles:

        add p["img"]:
            xpos p["x"]
            ypos p["y"]
            anchor (0.5, 0.5)
            at particle_anim(p["dx"], p["dy"], p["rot"], p["dur"])
init python:
    import pygame
    
    _parallax_current = [0.0, 0.0]  
    _parallax_target  = [0.0, 0.0]  
    
    
    PARALLAX_SMOOTH = 0.010          

    def parallax_transform(layer, max_depth=6):
        def apply(trans, st, at):
            trans.subpixel = True
            global _parallax_current, _parallax_target

            mx, my = pygame.mouse.get_pos()
            sw, sh = renpy.get_physical_size()
            nx = (mx / float(sw) - 0.5) * 2
            ny = (my / float(sh) - 0.5) * 2

            
            _parallax_target[0] = nx
            _parallax_target[1] = ny

            
            _parallax_current[0] += (_parallax_target[0] - _parallax_current[0]) * PARALLAX_SMOOTH
            _parallax_current[1] += (_parallax_target[1] - _parallax_current[1]) * PARALLAX_SMOOTH

            strength = (layer / float(max_depth)) * 30
            
            
            trans.xoffset = _parallax_current[0] * strength * -1
            trans.yoffset = _parallax_current[1] * strength * -1

            
            return 0.016 
            
        return apply
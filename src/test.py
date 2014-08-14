import pilasengine
import escenas

pilas = pilasengine.iniciar(1366, 768, capturar_errores=False)


escena = escenas.EscenaJuego(pilas)

pilas.definir_escena(escena)






"""
fondos = True


if fondos:

    capa_gradiente = Capa(pilas)
    capa_gradiente.definir_propiedades("fondos/fondo_pampa.png", 0.9, 1)


    capa_gradiente = Capa(pilas)
    capa_gradiente.definir_propiedades("fondos/arboleda3_capafondo.png", 0.05, 1)

    capa_gradiente = Capa(pilas)
    capa_gradiente.definir_propiedades("fondos/capa_medio.png", 0.2, 1)


    capa_gradiente = Capa(pilas)
    capa_gradiente.definir_propiedades("fondos/arbol_pp.png", 2, 1)

    '''
    capa_cielo = Capa(pilas)
    capa_cielo.definir_propiedades("fondo/cielo.png", 0.2, 1)
    capa_cielo.y = 89

    capa_bg0 = Capa(pilas)
    capa_bg0.definir_propiedades("fondo/bg0.png", 0.3, 1)
    capa_bg0.y = 75

    capa_bg1 = Capa(pilas)
    capa_bg1.definir_propiedades("fondo/bg1.png", 0.4, 1)
    capa_bg1.y = -33

    capa_bg2 = Capa(pilas)
    capa_bg2.definir_propiedades("fondo/bg2.png", 0.5, 1)
    capa_bg2.y = -19
    '''


def crear_arbusto_o_arbol():
    obj = ObjetoFondo(pilas)
    imagenes = [
                "fondos/algarrobo1.png",
                "fondos/algarrobo2.png",
                "fondos/eucalipto.png",
                "fondos/eucalipto2.png",
                "fondos/arbusto1.png",
                "fondos/arroyo.png",
                ]
    azar = pilas.azar(0, len(imagenes))
    obj.definir_propiedades(imagenes[azar], 0.9, 1)

if fondos:
    pilas.tareas.siempre(2, crear_arbusto_o_arbol)





pilas.camara.escala = 1
"""

pilas.ejecutar()

import pilasengine
import escenas

pilas = pilasengine.iniciar(1366, 768, capturar_errores=False)

escena = escenas.EscenaJuego(pilas)

pilas.definir_escena(escena)

pilas.ejecutar()

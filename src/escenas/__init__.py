import pilasengine
import actores

class EscenaJuego(pilasengine.escenas.Escena):


    def _crear_al_actor_vaca(self):
        vaca = actores.vaca.Vaca(self.pilas)
        vaca.y = -227
        vaca.x = 0
        vaca.escala = 1.0
        vaca.rotacion = 0

    def iniciar(self):
        self._crear_al_actor_vaca()

    def actualizar(self):
        pass
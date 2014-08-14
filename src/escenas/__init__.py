import os

import pilasengine
import actores

class EscenaJuego(pilasengine.escenas.Escena):

    def iniciar(self):
        self._crear_fondo('fondos/pampa')
        self._crear_al_actor_vaca()
        self.contador = 0

    def _crear_al_actor_vaca(self):
        vaca = actores.vaca.Vaca(self.pilas)
        vaca.y = -227
        vaca.x = 0
        vaca.escala = 1.0
        vaca.rotacion = 0

    def _crear_fondo(self, prefijo):
        self.__crear_fondo_cielo(prefijo)
        self.__crear_fondo_suelo(prefijo)

    def __crear_fondo_cielo(self, prefijo):
        ruta_cielo = os.path.join(prefijo, 'cielo')
        imagen_cielo = os.path.join(ruta_cielo, "cielo.png")
        capa = actores.capa.Capa(self.pilas)
        capa.definir_propiedades(imagen_cielo, 0.1, 1)

        objetos_cielo = self._obtener_archivos(ruta_cielo)
        objetos_cielo.remove('cielo.png')


        for objeto in objetos_cielo:
            obj = actores.objeto_fondo.ObjetoFondo(self.pilas)
            x = self.pilas.azar(-678, 678)
            y = self.pilas.azar(0, 378)
            obj.definir_propiedades(os.path.join(ruta_cielo, objeto), 0.15, z=1, x=x, y=y)


    def _obtener_archivos(self, ruta):
        listado = os.listdir(os.path.join('../data', ruta))
        return [x for x in listado if x.endswith('.png')]

    def actualizar(self):
        self.contador += 1

    def __crear_fondo_suelo(self, prefijo):
        imagen_suelo = os.path.join(prefijo, 'suelo', "suelo.png")
        capa = actores.capa.Capa(self.pilas)
        capa.definir_propiedades(imagen_suelo, 0.9, 1)


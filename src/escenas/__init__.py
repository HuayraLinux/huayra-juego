import os

import pilasengine
import actores

class EscenaJuego(pilasengine.escenas.Escena):

    def iniciar(self):
        prefijo = 'fondos/pampa'
        self._crear_fondo(prefijo)
        self._crear_al_actor_vaca()
        self.__crear_plano_frontal(prefijo)
        self.contador = 0

    def actualizar(self):
        self.contador += 1

    def _obtener_archivos(self, ruta):
        listado = os.listdir(os.path.join('../data', ruta))
        return [x for x in listado if x.endswith('.png')]

    def _crear_al_actor_vaca(self):
        vaca = actores.vaca.Vaca(self.pilas)
        vaca.y = -227
        vaca.x = 0
        vaca.escala = 1.0
        vaca.rotacion = 0

    def _crear_fondo(self, prefijo):
        self.__crear_fondo_cielo(prefijo)
        self.__crear_fondo_suelo(prefijo)
        self.__crear_fondo_capa_fondo(prefijo)
        self.__crear_fondo_capa_medio(prefijo)
        self.__crear_fondo_objetos_del_suelo(prefijo)

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
            y = self.pilas.azar(100, 378)
            obj.definir_propiedades(os.path.join(ruta_cielo, objeto), 0.15, z=1, x=x, y=y)

    def __crear_fondo_suelo(self, prefijo):
        ruta_suelo = os.path.join(prefijo, 'suelo')
        imagen_suelo = os.path.join(ruta_suelo, "suelo.png")
        capa = actores.capa.Capa(self.pilas)
        capa.definir_propiedades(imagen_suelo, 0.9, 1)

    def __crear_fondo_objetos_del_suelo(self, prefijo):
        ruta_suelo = os.path.join(prefijo, 'capa_1')
        objetos_suelo = self._obtener_archivos(ruta_suelo)
        dx = -500

        for objeto in objetos_suelo:
            obj = actores.objeto_fondo.ObjetoFondo(self.pilas)
            dx += self.pilas.azar(200, 500)
            x = dx
            y = 0
            obj.definir_propiedades(os.path.join(ruta_suelo, objeto), 0.9, z=1, x=x, y=y)

    def __crear_fondo_capa_fondo(self, prefijo):
        ruta_suelo = os.path.join(prefijo, 'capa_4')
        objetos_suelo = self._obtener_archivos(ruta_suelo)
        dx = -500

        for objeto in objetos_suelo:
            obj = actores.objeto_fondo.ObjetoFondo(self.pilas)
            dx += self.pilas.azar(200, 500)
            x = dx
            y = 0
            obj.definir_propiedades(os.path.join(ruta_suelo, objeto), 0.15, z=1, x=x, y=y)

    def __crear_fondo_capa_medio(self, prefijo):
        ruta_suelo = os.path.join(prefijo, 'capa_2')
        objetos_suelo = self._obtener_archivos(ruta_suelo)
        dx = -500

        for objeto in objetos_suelo:
            obj = actores.objeto_fondo.ObjetoFondo(self.pilas)
            dx += self.pilas.azar(200, 500)
            x = dx
            y = 0
            obj.definir_propiedades(os.path.join(ruta_suelo, objeto), 0.3, z=1, x=x, y=y)

    def __crear_plano_frontal(self, prefijo):
        ruta_capa_frontal = os.path.join(prefijo, 'capa_0')

        objetos_cielo = self._obtener_archivos(ruta_capa_frontal)
        dx = -400

        for objeto in objetos_cielo:
            obj = actores.objeto_fondo.ObjetoFondo(self.pilas)
            dx += self.pilas.azar(300, 600)
            x = dx
            y = 0
            obj.definir_propiedades(os.path.join(ruta_capa_frontal, objeto), 3, z=-1, x=x, y=y)
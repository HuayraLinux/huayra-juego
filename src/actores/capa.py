# -*- encoding: utf-8 -*-
import pilasengine

class Capa(pilasengine.actores.Actor):

    def iniciar(self):
        self.velocidad = 0

    def definir_propiedades(self, imagen, velocidad, z=0, x=0, y=0):
        self.imagen = imagen
        self.imagen.repetir_horizontal = True
        self.velocidad = velocidad * 10
        self.z = z
        self.x = x
        self.y = y

    def actualizar(self):
        self.x -= self.velocidad
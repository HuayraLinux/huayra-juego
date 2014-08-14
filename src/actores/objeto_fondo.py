# -*- encoding: utf-8 -*-
import pilasengine

class ObjetoFondo(pilasengine.actores.Actor):

    def iniciar(self):
        self.velocidad = 0
        self.x = 800 + 100 * self.pilas.azar(0, 2)
        self.y = 0

    def definir_propiedades(self, imagen, velocidad, z=0, x=0, y=0):
        self.imagen = imagen
        self.velocidad = velocidad * 10
        self.z = z
        self.x = x
        self.y = y

    def actualizar(self):
        self.x -= self.velocidad

        if self.derecha < -700:
            self.izquierda = self.pilas.azar(700, 800)

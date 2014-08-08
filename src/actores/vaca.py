import pilasengine
import estados

class Vaca(pilasengine.actores.Actor):

    def iniciar(self):
        self.animaciones = {}

        self.animaciones["camina"] = self.pilas.imagenes.cargar_animacion('animacion_nueva.png', 12)
        self.animaciones['camina'].definir_animacion('corre', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 24)
        self.animaciones['camina'].cargar_animacion('corre')

        self.animaciones["salto"] = self.pilas.imagenes.cargar_animacion('salto_reducido.png', 20)

        self.animaciones['salto'].definir_animacion('comienzo', [0, 1, 2, 3, 4, 5], 50)
        self.animaciones['salto'].definir_animacion('curso', [6, 7, 8, 9, 8, 7], 24)
        self.animaciones['salto'].definir_animacion('fin', [13, 14, 15, 16, 17, 18, 19], 50)

        self.definir_estado(estados.Correr(self))
        #print pilas.pad.listar()

    def definir_estado(self, estado):
        self.estado = estado

    def cambiar_animacion(self, animacion, secuencia):
        self.imagen = self.animaciones[animacion]
        self.imagen.cargar_animacion(secuencia)

    def actualizar(self):
        self.estado.actualizar()
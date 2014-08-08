import pilasengine

class Estado(object):

    def __init__(self, receptor):
        self.receptor = receptor
        self.iniciar()

    def iniciar(self):
        pass

    def actualizar(self):
        pass

    def actualizar_posicion_horizontal(self):
        velocidad = 8

        if self.receptor.pilas.control.izquierda:
            self.receptor.x -= velocidad

        if self.receptor.pilas.control.derecha:
            self.receptor.x += velocidad

        if self.receptor.x < -420:
            self.receptor.x = -420

        if self.receptor.x > 400:
            self.receptor.x = 400

class Correr(Estado):

    def iniciar(self):
        self.receptor.cambiar_animacion('camina', 'corre')

    def actualizar(self):
        self.receptor.imagen.avanzar()
        #self.receptor.x = self.receptor.pilas.pad.x

        if self.receptor.pilas.control.arriba:
            self.receptor.definir_estado(SaltoComienza(self.receptor))

        self.actualizar_posicion_horizontal()


class SaltoComienza(Estado):

    def iniciar(self):
        self.receptor.cambiar_animacion('salto', 'comienzo')

    def actualizar(self):
        continua = self.receptor.imagen.avanzar()

        if not continua:
            self.receptor.definir_estado(SaltoVuela(self.receptor))
        self.actualizar_posicion_horizontal()

class SaltoVuela(Estado):

    def iniciar(self):
        self.receptor.cambiar_animacion('salto', 'curso')
        self.vy = 10
        self.y_suelo = self.receptor.y

    def actualizar(self):
        self.receptor.imagen.avanzar()

        self.vy -= 0.5
        self.receptor.rotacion = self.vy * 2
        self.receptor.y += self.vy

        if self.receptor.y < self.y_suelo:
            self.receptor.y = self.y_suelo
            self.receptor.definir_estado(SaltoCae(self.receptor))

        self.actualizar_posicion_horizontal()

class SaltoCae(Estado):

    def iniciar(self):
        self.receptor.cambiar_animacion('salto', 'fin')
        self.receptor.rotacion = 0

    def actualizar(self):
        continua = self.receptor.imagen.avanzar()

        if not continua:
            self.receptor.definir_estado(Correr(self.receptor))

        self.actualizar_posicion_horizontal()
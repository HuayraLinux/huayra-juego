import pilasengine

pilas = pilasengine.iniciar(800, 600, capturar_errores=False)

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

class Capa(pilasengine.actores.Actor):

    def iniciar(self):
        self.velocidad = 0

    def definir_propiedades(self, imagen, velocidad, z):
        self.imagen = imagen
        self.imagen.repetir_horizontal = True
        self.velocidad = velocidad * 10
        self.z = z

    def actualizar(self):
        self.x -= self.velocidad

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

        self.definir_estado(Correr(self))
        print pilas.pad.listar()

    def definir_estado(self, estado):
        self.estado = estado

    def cambiar_animacion(self, animacion, secuencia):
        self.imagen = self.animaciones[animacion]
        self.imagen.cargar_animacion(secuencia)

    def actualizar(self):
        self.estado.actualizar()


fondos = True


if fondos:
    capa_gradiente = Capa(pilas)
    capa_gradiente.definir_propiedades("fondo/Gradient.png", 0.1, 1)

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


vaca = Vaca(pilas)
vaca.y = -227
vaca.x = 0
vaca.escala = 1.0
vaca.rotacion = 0

pilas.camara.escala = 1


pilas.ejecutar()

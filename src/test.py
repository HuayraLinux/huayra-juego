import pilasengine

pilas = pilasengine.iniciar(800,600, capturar_errores=False)

class Estado(object):

    def __init__(self, receptor):
        self.receptor = receptor
        self.iniciar()

    def iniciar(self):
        pass

    def actualizar(self):
        pass

class Correr(Estado):

    def actualizar(self):
        self.receptor.imagen.avanzar()
        self.receptor.x = self.receptor.pilas.pad.x * 300

class Salta(Estado):

    def actualizar(self):
        pass

class Capa(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "fondo/fondo.png"
        self.imagen.repetir_horizontal= True

class Vaca(pilasengine.actores.Actor):

    def iniciar(self):
        self.animaciones = {}

        self.animaciones["camina"] = self.pilas.imagenes.cargar_animacion('animacion.png', 10)
        self.animaciones['camina'].definir_animacion('corre', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 24)
        self.animaciones['camina'].cargar_animacion('corre')

        self.animaciones["salto"] = self.pilas.imagenes.cargar_animacion('salto.png', 20)

        self.animaciones['salto'].definir_animacion('comienzo', [0, 1, 2, 3, 4, 5], 12)
        self.animaciones['salto'].definir_animacion('curso', [6, 7, 8, 9, 8, 7], 12)
        self.animaciones['salto'].definir_animacion('fin', [10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 12)

        #self.cambiar_animacion('salto', 'fin')
        self.cambiar_animacion('camina', 'corre')
        self.definir_estado(Correr(self))
        print pilas.pad.listar()

    def definir_estado(self, estado):
        self.estado = estado

    def cambiar_animacion(self, animacion, secuencia):
        self.imagen = self.animaciones[animacion]
        self.imagen.cargar_animacion(secuencia)

    def actualizar(self):
        self.estado.actualizar()

capa = Capa(pilas)
vaca = Vaca(pilas)
capa.x = [-4000], 10


pilas.ejecutar()
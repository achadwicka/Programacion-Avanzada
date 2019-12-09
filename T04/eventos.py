

class Horario_Almuerzo:
    def __init__(self, tiempo_horario, simulacion):
        self.tiempo_horario = tiempo_horario
        self.simulacion = simulacion
        self.alumnos = []
        self.funcionarios = []


        for alumno in self.simulacion.alumnos:
            if alumno.horario_almuerzo == self.tiempo_horario and \
                    alumno.in_campus:
                self.alumnos.append(alumno)

        for funcionario in self.simulacion.funcionarios:
            if funcionario.horario_almuerzo == self.tiempo_horario and \
                    funcionario.in_campus:
                self.funcionarios.append(funcionario)

class Evento:

    def __init__(self, tiempo_inicio, simulacion):
        self.tiempo_inicio = tiempo_inicio
        self.simulacion = simulacion

    def horario_almuerzo(self):
        return "a"

    def comer_snack(self):
        pass

    def llegar_al_campus(self, persona):
        pass


a = Evento(1,2)
b = a.horario_almuerzo()
c = b.tiempo_inicio
print(c)
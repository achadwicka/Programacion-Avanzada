

# crearemos las clases de las nuevas excepciones
# y creamos tambien los diferentes tests.

class BadRequest(TypeError):
    def __init__(self):
        super().__init__("Error: Bad Request")


class NotFound(ValueError):
    def __init__(self):
        super().__init__("Error: Not Found")


class NotAcceptable(ReferenceError):
    def __init__(self):
        super().__init__("Error: Not Acceptable")


class GenomeError(ValueError):
    def __init__(self):
        super().__init__("Error: Genome Error")


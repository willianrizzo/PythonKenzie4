class Person():
    life_expectancy = 80  # valor mutavel
    pets = ["cat"]  # valor imutavel
    person_list = []

    # dunder init e oque inicia a instanica da classe
    def __init__(self, nome: str, cpf: str):  # self = this object
        self.nome = nome
        self.cpf = cpf
        self.wakeuptime = "8hrs"
        self.fav_mov = ["comedy"]

    # metodos:

    # intancias - faz referencia ao objeto especifico
    def save_person(self):
        # wiu.person_list.append(wiu)
        self.person_list.append(self)
        print("cadastro realizado")

    # classe
    @classmethod  # usar semptr que for methodo classe
    def get_person(cls, cpf: str):  # cls vemde classe
        for person in cls.person_list:
            if person.cpf == cpf:
                return person

    # estatico
    @staticmethod  # nao precisa de parametro obrigatorio
    def change_to_upper(nome: str):
        return nome.upper()

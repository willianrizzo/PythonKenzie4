from persons.person import Person


def class_attr():
    wiu = Person("teste", "12121")
    print(wiu.life_expectancy)

    wiu.life_expectancy = 90
    print(wiu.life_expectancy)
    # muda valor para apenas essa objeto

    wiu.pets.append("dog")  # nao muda "cat" esim adciona outro na lista
    print(wiu.pets)
    print(Person.pets)


def instance_attr():
    wiu = Person("wiu", "123")
    print(wiu.nome)
    # print(wiu.cpf)
    # print(wiu.wakeuptime)

    wiu.fav_mov.append("horror")
    print(wiu.fav_mov)


def methods():
    Bill = Person("Bill", "1231")
    Lucira = Person("Lucira", "1231")
    print(Bill.save_person())
    # print(Lucira.save_person())
    # print(Person.person_list)

    found_person = Person.get_person("1231")
    print(f"{found_person.nome} foi encontrado")
    print(Person.change_to_upper(Bill.nome))
    # Bill.get_person


def main():
    # instance_attr()
    methods()


if __name__ == "__main__":
    main()

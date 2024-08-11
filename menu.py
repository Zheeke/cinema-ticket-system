from cinema_ticket_system import CinemaTicketSystem

cinemaSystem = CinemaTicketSystem()

movieId1 = cinemaSystem.addMovie('Inception')
movieId2 = cinemaSystem.addMovie('The Matrix')
movieId3 = cinemaSystem.addMovie('KungFu Panda')

userId1 = cinemaSystem.addUser('Alice')#creates user record
userId2 = cinemaSystem.addUser('Bob')#creates user record
userId3 = cinemaSystem.addUser('Zheke')#creates user record

def getKeyByValue(d, value):
    for key, val in d.items():
        if val == value:
            return key
    return f"{value} нету в базе"

def menu():   
    while True: 
        print("Здравствуйте, у вас есть следующие доступные функции:")
        print("1. Добавить новый фильм;")
        print("2. Показать все доступные фильмы;")
        print("3. Добавить нового пользователя;")
        print("4. Купить билет;")
        print("5. Отменить покупку билета;")
        print("6. Завершить сеанс")
        a = input("Ваш выбор?(цифра)")

        if a == "1":
            newMovie = input("Введите название фильма:")
            cinemaSystem.addMovie(newMovie)
            print(f"{newMovie} добавлен.")
        elif a == "2":
            cinemaSystem.showAllMovies()
        elif a == "3":
            print("помните, имя пользователя должно состоять из букв и цифр но не должно включать пробел и любые символы")
            cinemaSystem.addUser(input("Введите имя пользователя: "))
        elif a == "4":
            userName, movieName = input("Введите имя пользователя и название фильма на который желаете приобрести билет: ").split(maxsplit=1)
            userId = getKeyByValue(cinemaSystem.users, userName)
            movieId = getKeyByValue(cinemaSystem.movies, movieName)
            newTicket = cinemaSystem.buyTicket(userId, movieId)
            if newTicket is not None:
                print(f"Ваш номер билета: {newTicket}")
            else:
                print("Не удалось купить билет. Проверьте username и/или название фильма")
        elif a == "5":
            bilet = input("Введите ваш номер билета:")
            cinemaSystem.cancelTicket(bilet)
            if bilet not in cinemaSystem.tickets:
                print("Такого билета не существует")
            else:
                print("Ваша покупка билета была успешно отменена")
        elif a == "6":
            print("Завершение сеанса. Спасибо за использование системы!")
            break
        else:
            print("Неверный выбор. попробуйте снова")
            print("")
            continue


if __name__ == "__main__":
    menu()
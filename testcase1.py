from cinema_ticket_system import CinemaTicketSystem

cinemaSystem = CinemaTicketSystem()

print(cinemaSystem.showAllMovies())
#Нет доступныз фильмов для показа.
#

movieId1 = cinemaSystem.addMovie('Inception')
movieId2 = cinemaSystem.addMovie('The Matrix')
movieId3 = cinemaSystem.addMovie('KungFu Panda')

print(cinemaSystem.showAllMovies())
"""Вывод:
1. Inception
2. The Matrix
3. KungFu Panda
"""

userId1 = cinemaSystem.addUser('Alice')#creates user record
userId2 = cinemaSystem.addUser('Bob')#creates user record
userId3 = cinemaSystem.addUser('Zheke')#creates user record

ticketId1 = cinemaSystem.buyTicket(userId1, movieId1)#creates ticket record
ticketId2 = cinemaSystem.buyTicket(userId2, movieId2)#creates ticket record
ticketId3 = cinemaSystem.buyTicket(userId1, movieId2)#creates ticket record
ticketId4 = cinemaSystem.buyTicket(userId3, movieId3)#creates ticket record

print(cinemaSystem.tickets) #shows all tickets
print(f"{cinemaSystem.cancelTicket(ticketId2)}") #True
print(f"{cinemaSystem.cancelTicket(999)}") #False, since there's no ticket with such id
print(cinemaSystem.tickets) #shows all tickets after canceling ticket with id 2
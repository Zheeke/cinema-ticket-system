#sequence generator
def counter(start=0, next=1):
    n = start
    while True:
        yield n
        n += next

#class Cinema Ticket System
class CinemaTicketSystem():
    def __init__(self):
        self.users = {}  #a dictionary to store the users records
        self.movies = {}#a dictionary to store the movies records
        self.tickets = {}#a dictionary to store the tickets records

        #id generators for each of the variable
        self.user_id_generator = counter(1)
        self.movie_id_generator = counter(1)
        self.ticket_id_generator = counter(1)

    #next 2 functions are for assigning id for variables and saving the record to the dict
    def addUser(self,userName):
        userId = next(self.user_id_generator)
        self.users[userId] = userName
        return userId
    
    def addMovie(self, movieName):
        movieId = next(self.movie_id_generator)
        self.movies[movieId] = movieName
        return movieId
    
    #shows unsorted list of movies 
    def showAllMovies(self):
        if not self.movies:
            print("Нет фильмов для показа.")
        else:
            print("Вывод:")
            for movieId, movieName in self.movies.items():
                print(f"{movieId}. {movieName}")
        return "" #to get rid of "None" after function executes
               
    def buyTicket(self, userId, movieId):
        if userId not in self.users: #check if the user is authorised
            print("Вы не авторизованы")
            return None
        if movieId not in self.movies: #check if such film exists
            print("Фильма нет в списке")
            return None
        
        #saving ticket record to the ticket dict
        ticketId = next(self.ticket_id_generator)
        self.tickets[ticketId] = (userId, movieId)
        return ticketId
    
    #deleting the ticket record from the ticket's dict
    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True
        return False
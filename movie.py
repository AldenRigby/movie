movies = """The Shawshank Redemption, (1994), Frank Darabont, R, Drama, [Tim Robbins, Morgan Freeman]
Pulp Fiction, (1994), Quentin Tarantino, R, Crime, [John Travolta, Uma Thurman, Samuel L. Jackson]
The Godfather, (1972), Francis Ford Coppola, R, Crime, [Marlon Brando, Al Pacino, James Caan]
Inception, (2010), Christopher Nolan, PG-13, Sci-Fi, [Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page]
The Matrix, (1999), Lana Wachowski, Lilly Wachowski, R, Sci-Fi, [Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss]
Forrest Gump, (1994), Robert Zemeckis, PG-13, Drama, [Tom Hanks, Robin Wright, Gary Sinise]
The Dark Knight, (2008), Christopher Nolan, PG-13, Action, [Christian Bale, Heath Ledger, Aaron Eckhart]
Schindler's List, (1993), Steven Spielberg, R, Drama, [Liam Neeson, Ben Kingsley, Ralph Fiennes]
Fight Club, (1999), David Fincher, R, Drama, [Brad Pitt, Edward Norton, Helena Bonham Carter]
Goodfellas, (1990), Martin Scorsese, R, Crime, [Robert De Niro, Ray Liotta, Joe Pesci]
The Silence of the Lambs, (1991), Jonathan Demme, R, Thriller, [Jodie Foster, Anthony Hopkins, Scott Glenn]
Forrest Gump, (1994), Robert Zemeckis, PG-13, Drama, [Tom Hanks, Robin Wright, Gary Sinise]
Titanic, (1997), James Cameron, PG-13, Romance, [Leonardo DiCaprio, Kate Winslet, Billy Zane]
The Lord of the Rings: The Fellowship of the Ring, (2001), Peter Jackson, PG-13, Fantasy, [Elijah Wood, Ian McKellen, Orlando Bloom]
Gladiator, (2000), Ridley Scott, R, Action, [Russell Crowe, Joaquin Phoenix, Connie Nielsen]
The Green Mile, (1999), Frank Darabont, R, Drama, [Tom Hanks, Michael Clarke Duncan, David Morse]
Saving Private Ryan, (1998), Steven Spielberg, R, War, [Tom Hanks, Matt Damon, Tom Sizemore]
Jurassic Park, (1993), Steven Spielberg, PG-13, Adventure, [Sam Neill, Laura Dern, Jeff Goldblum]
The Departed, (2006), Martin Scorsese, R, Crime, [Leonardo DiCaprio, Matt Damon, Jack Nicholson]
The Lion King, (1994), Roger Allers, Rob Minkoff, G, Animation, [Matthew Broderick, Jeremy Irons, James Earl Jones]
Eternal Sunshine of the Spotless Mind, (2004), Michel Gondry, R, Romance, [Jim Carrey, Kate Winslet, Kirsten Dunst]
Inglourious Basterds, (2009), Quentin Tarantino, R, War, [Brad Pitt, Christoph Waltz, Mélanie Laurent]
The Sixth Sense, (1999), M. Night Shyamalan, PG-13, Thriller, [Bruce Willis, Haley Joel Osment, Toni Collette]
The Usual Suspects, (1995), Bryan Singer, R, Mystery, [Kevin Spacey, Gabriel Byrne, Chazz Palminteri]
Memento, (2000), Christopher Nolan, R, Thriller, [Guy Pearce, Carrie-Anne Moss, Joe Pantoliano]
Braveheart, (1995), Mel Gibson, R, Biography, [Mel Gibson, Sophie Marceau, Patrick McGoohan]
The Terminator, (1984), James Cameron, R, Sci-Fi, [Arnold Schwarzenegger, Linda Hamilton, Michael Biehn]
Back to the Future, (1985), Robert Zemeckis, PG, Adventure, [Michael J. Fox, Christopher Lloyd, Lea Thompson]
Alien, (1979), Ridley Scott, R, Horror, [Sigourney Weaver, Tom Skerritt, John Hurt]
The Truman Show, (1998), Peter Weir, PG, Drama, [Jim Carrey, Laura Linney, Noah Emmerich]""".split("\n")
moviesData = movies.copy() #make sure it's the same length as movies.
moviesObjects = [] #where all the objects will be stored
class Movie(): #class !
    #initialize all
    def __init__(self, title, year, director, rating, genre, cast):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast
    #print everything in a nice format
    def __str__(self):
        return f"{self.title} ({str(self.year)})\n    Directed by {self.director}, rated {self.rating}. {self.genre}\n    Featuring {self.cast}"
    #sort using lambda, pretty easy
    def sortYear(self):
        moviesObjects.sort(key=lambda x: x.year)
        print("Sorted successfully.\n")
    def sortName(self):
        moviesObjects.sort(key=lambda x: x.title)
        print("Sorted successfully.\n")
    #only show everything that contains the substring for all searches. really simple
    def search(self, type):
        userInput = input("What is your search term? ").upper()
        found = False
        for i in range(len(moviesObjects)):
            if type == "genre":
                if userInput in moviesObjects[i].genre.upper():
                    found = True
                    print(moviesObjects[i])
            if type == "director":
                if userInput in moviesObjects[i].director.upper():
                    found = True
                    print(moviesObjects[i])
            if type == "cast":
                if userInput in moviesObjects[i].cast.upper():
                    found = True
                    print(moviesObjects[i])
        if not found:
            print("No movies found.")
        print("")
for i in range(len(moviesData)): #this chunk of code takes all of the movie lines and turns it into objects
    moviesData[i] = []
    #pretty janky. but use the thing to determine what chunk of the line belongs to where
    moviesData[i].extend((movies[i].split(",")[0], int(movies[i].split(",")[1][2:6]), movies[i].split(",")[2][1:], movies[i].split(",")[3][1:], movies[i].split(",")[4][1:], movies[i].split("[")[1][0:-1]))
    #title, year, director, rating, genre, cast in order
    moviesObjects.append(Movie(*moviesData[i]))
while True: #continue to ask the user stuff
    print("What would you like to do?\nS - Show all movies\nA - Sort movies alphabetically\nY - Sort movies by release year\nG - Search genre\nD - Search director\nC - Search cast\nE - Exit program")
    validInputs = ["S","A","Y","G","D","C","E"]
    userInput = input("Input: ").upper()
    print("")
    if userInput in validInputs:
        if userInput == "S":
            for i in range(len(moviesObjects)):
                print(moviesObjects[i])
            print("")
        elif userInput == "A":
            moviesObjects[0].sortName()
        elif userInput == "Y":
            moviesObjects[0].sortYear()
        elif userInput == "G":
            moviesObjects[0].search("genre")
        elif userInput == "D":
            moviesObjects[0].search("director")
        elif userInput == "C":
            moviesObjects[0].search("cast")
        elif userInput == "E":
            print("You quit the program.")
            quit() #got it in 100 lines!
# Program name: sujan_acharya_A5.py A5 Oscar Movie List Maintenance Author: Sujan Acharya

movies = [[1939, 'Gone With the Wind', 'drama'],
          [1943, 'Casablanca', 'drama'],
          [1953, 'From Here to Eternity', 'historical'],
          [1954, 'On the Waterfront', 'drama'],
          [1957, 'The Bridge on the River Kwai', 'historical'],
          [1961, 'West Side Story', 'musical'],
          [1965, 'The Sound of Music', 'musical'],
          [1969, 'Midnight Cowboy', 'drama'],
          [1971, 'The French Connection', 'crime'],
          [1972, 'The Godfather', 'drama'],
          [1977, 'Annie Hall', 'comedy'],
          [1981, 'Chariots of Fire', 'drama'],
          [1982, 'Gandhi', 'historical'],
          [1984, 'Amadeus', 'historical'],
          [1986, 'Platoon', 'action'],
          [1988, 'Rain Man', 'drama'],
          [1990, 'Dances with Wolves', 'western'],
          [1991, 'The Silence of the Lambs', 'crime'],
          [1992, 'Unforgiven', 'western'],
          [1993, 'Schindler s List', 'historical'],
          [1994, 'Forrest Gump', 'comedy'],
          [1995, 'Braveheart', 'historical'],
          [1998, 'Shakespeare in Love', 'comedy'],
          [2001, 'A Beautiful Mind', 'historical'],
          [2002, 'Chicago', 'musical'],
          [2007, 'No Country for Old Men', 'crime'],
          [2008, 'Slumdog Millionaire', 'drama'],
          [2009, 'The Hurt Locker', 'action'],
          [2010, 'The Kings Speech', 'historical'],
          [2011, 'The Artist', 'comedy'],
          [2012, 'Argo', 'historical'],
          [2013, '12 Years a Slave', 'drama'],
          [2014, 'Birdman', 'comedy'],
          [2015, 'Spotlight', 'drama'],
          [2016, 'Moonlight', 'drama'],
          [2017, 'The Shape of Water', 'fantasy'],
          [2018, 'Green Book', 'drama'],
          [2019, 'Parasite', 'drama'],
          [2020, 'Nomadland', 'drama'],
          [2021, 'CODA', 'drama'],
          [2022, 'Everything Everywhere All at Once', 'comedy-drama']]

def add_movie():
    while True:
        year = int(input("\nEnter the year to add a winning movie: "))
        if year < 1927 or year > 2022:
         print("Invalid year. Year must be between 1927 and 2022.\n")
         continue
        else:
         break
    while True:
        title = input("Enter the movie title: ")
        if len(title) > 40:
            print("Invalid title. Title must be less than 40 characters.\n")
            continue
        else:
            break
    while True:
        category = input("Enter the movie category: ")
        if category not in ['drama', 'western', 'historical', 'musical', 'comedy', 'action', 'fantasy', 'scifi']:
            print("Invalid category. Valid categories are: drama, western, historical, musical, comedy, action, fantasy, scifi\n")
            continue
        else:
            break

    movie_exists = False
    for m in movies:
            if year == m[0]:
                replace = input("Movie for this year already exists. Do you want to replace it? (yes/no): ")
                if replace.lower() == 'yes':
                    m[1] = title
                    m[2] = category
                    print("Movie for the year " + str(year) + " " + "has been replaced.\n")
                movie_exists = True
                break

    if not movie_exists:
            movies.append([year, title, category])
            print("Movie for the year " + str(year) + ' '+ "has been added.\n")

            
menu = """
 D - display winning movie for a selected year
 A - add movie title and category for a selected year
 L - display entire movie list – year, title, category
 C - display movies in a selected category – year and title
 q - quit
 Select one of the menu options above
"""
while True:
    print(menu)
    selection = input("\nSelect one of the menu options above: ")
    if selection == 'q':
        break

    if selection == "D":
        year = input(
            "\nType the year for which you want to see winning movie: ")
        year = int(year)
        found = False
        for m in movies:
            if year == m[0]:
                input("\nIn " + str(year) + ' ' + "the winning movie was " +
                      m[1]+'.\n\nPress Enter to continue:')
                found = True
        if not found:
            print("The", year, "is not listed.")
    elif selection == 'A':
        add_movie()
    elif selection == 'L':
        for x in movies:
            print(str(x[0]), '     ', str(x[1]), "     ", str(x[2]))
        input("\nPress enter to continue: ")
    elif selection == 'C':
        cat = input('Enter the category of the movie: ')
        found = False
        print("\nFor" + " " + cat + " " + "here are all the movies: ")

        for c in movies:
            if cat == c[2]:
                print(str(c[1]))
                found = True
        input("Press enter to continue: ")
        if not found:
            input("No Match")

    else:
        print("\nInvalid, try again!!")
input('\n\nHit Enter to end program')
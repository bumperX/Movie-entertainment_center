import media
import fresh_tomatoes

# Create my favorite movie instances with related infomation
harry_potter = media.Movie(
    "Harry Potter",
    "A young boy with a great destiny proves his worth while attending "
    "Hogwarts School of Witchcraft and Wizardry",
    "https://i.pinimg.com/736x/26/cb/93/26cb93765b28d5b39b2465f1717f2d8c"
    "--harry-potter-world-harry-potter-stuff.jpg",
    "https://www.youtube.com/watch?v=PbdM1db3JbY"
    )

your_name = media.Movie(
    "Your Name",
    "A teenage boy and girl embark on a quest to meet each other for the "
    "first time after they magically swap bodies",
    "https://d32qys9a6wm9no.cloudfront.net/images/movies/poster/58/"
    "0d42fdbd1e7bca33d677d57d999a29e0_500x735.jpg",
    "https://www.youtube.com/watch?v=o4-URMnBOPU"
    )

lion_king = media.Movie(
    "The Lion King",
    "the adventures of the young lion Simba",
    "http://www.eatbrie.com/large_posters_files/Lionking7.jpg",
    "https://www.youtube.com/watch?v=px-X3drhJ7U"
    )

monsters_inc = media.Movie(
    "Monsters Inc",
    "The story of Lovable Sulley and his wisecracking sidekick Mike"
    " Wazowski at Monsters Inc.",
    "https://i.pinimg.com/originals/59/10/23/59102333312c8"
    "ceae749027c5193539d.jpg",
    "https://www.youtube.com/watch?v=6tCxnHCqqxg"
    )

pride_prejudice = media.Movie(
    "Pride and Prejudice",
    "the emotional development of the protagonist, Elizabeth Bennet,"
    " who learns the error of making hasty judgments and comes to "
    "appreciate the difference between the superficial and the essential",
    "http://img.moviepostershop.com/pride-and-prejudice-movie"
    "-poster-2005-1020451320.jpg",
    "https://www.youtube.com/watch?v=UykqkIqRTU8"
    )

imitation_game = media.Movie(
    "The Imitation Game",
    "During World War II, mathematician Alan Turing tries to crack"
    " the enigma code with help from fellow mathematicians",
    "http://tr.web.img3.acsta.net/pictures/15/02/16/15/49/166413.jpg",
    "https://www.youtube.com/watch?v=5DcOR6r31X0"
    )

# Create a list containing my favorite movies
movies = [
    harry_potter,
    your_name,
    lion_king,
    monsters_inc,
    pride_prejudice,
    imitation_game
    ]

# Open web with my favorite movies in a browser
fresh_tomatoes.open_movies_page(movies)
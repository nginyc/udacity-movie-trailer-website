from media import Movie
from fresh_tomatoes import open_movies_page


# Populate list of movies
movies = [
    Movie(
        'Christopher Robin',
        'http://www.impawards.com/2018/posters/christopher_robin.jpg',
        'https://youtu.be/mecs05sjbRU'
    ),
    Movie(
        'Ocean\'s 8',
        'http://www.impawards.com/2018/posters/oceans_eight_ver2.jpg',
        'https://youtu.be/g681XwMUpFc'
    ),
    Movie(
        'Won\'t You Be My Neighbor?',
        'http://www.impawards.com/2018/posters/wont_you_be_my_neighbor.jpg',
        'https://youtu.be/jxgiMggVNVg'
    ),
    Movie(
        'Mowgli',
        'http://www.impawards.com/2018/posters/mowgli.jpg',
        'https://youtu.be/FB1KTG-O1V0'
    ),
    Movie(
        'Hearts Beat Loud',
        'http://www.impawards.com/2018/posters/hearts_beat_loud.jpg',
        'https://youtu.be/7czG5jr71Q8'
    ),
    Movie(
        'Mission: Impossible - Fallout',
        'http://www.impawards.com/2018/posters/' +
        'mission_impossible__fallout.jpg',
        'https://youtu.be/P5_iNAWUUQA'
    ),
    Movie(
        'Deadpool 2',
        'http://www.impawards.com/2018/posters/deadpool_two.jpg',
        'https://youtu.be/f0iUDcm-xck'
    ),
    Movie(
        'Mile 22',
        'http://www.impawards.com/2018/posters/mile_twenty_two.jpg',
        'https://youtu.be/eJU6S5KOsNI'
    )
]

# Open up movies page in browser
open_movies_page(movies)

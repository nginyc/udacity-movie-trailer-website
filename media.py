import webbrowser


class Movie():
    '''
      Abstraction of a movie on the website
    '''

    # Initializes a movie with a title, post image and trailer
    def __init__(self, title, poster_image_url, trailer_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_url

    # Opens up youtube trailer in browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

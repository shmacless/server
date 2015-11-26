import tornado.ioloop
import tornado.web
import json
import os
import random


movies = [['Pulp Fiction', 'http://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SX214_AL_.jpg'],
              ['Good Will Hunting', 'http://ia.media-imdb.com/images/M/MV5BMTk0NjY0Mzg5MF5BMl5BanBnXkFtZTcwNzM1OTM2MQ@@._V1_SY317_CR1,0,214,317_AL_.jpg'],
              ['The Big Lebowski', 'http://ia.media-imdb.com/images/M/MV5BMTQ0NjUzMDMyOF5BMl5BanBnXkFtZTgwODA1OTU0MDE@._V1_SX214_AL_.jpg'],
              ['V for Vendetta', 'http://ia.media-imdb.com/images/M/MV5BOTI5ODc3NzExNV5BMl5BanBnXkFtZTcwNzYxNzQzMw@@._V1_SY317_CR0,0,214,317_AL_.jpg'],
              ['Fight Club', 'http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_SX214_AL_.jpg'],
              ['Gladiator', 'http://ia.media-imdb.com/images/M/MV5BMjA4ODQ3ODkzNV5BMl5BanBnXkFtZTYwOTc4NDI3._V1_SX214_AL_.jpg'],
              ['Interstellar', 'http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX214_AL_.jpg'],
              ['Into the Wild', 'http://ia.media-imdb.com/images/M/MV5BMTAwNDEyODU1MjheQTJeQWpwZ15BbWU2MDc3NDQwNw@@._V1_SY317_CR0,0,214,317_AL_.jpg'],
              ['The Imitation Game', 'http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SY317_CR0,0,214,317_AL_.jpg'],
              ['The Truman Show', 'http://ia.media-imdb.com/images/M/MV5BMTg4NTU3NTAyMF5BMl5BanBnXkFtZTgwNjYwNzc3NjE@._V1_SX214_AL_.jpg'],
              ['Toy Story 3', 'http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SY317_CR5,0,214,317_AL_.jpg'],
              ['Shawshank Redemption', 'http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg'],
              ['Forrest Gump', 'http://ia.media-imdb.com/images/M/MV5BMTQwMTA5MzI1MF5BMl5BanBnXkFtZTcwMzY5Mzg3OA@@._V1_SX214_AL_.jpg'],
              ['Matrix', 'http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg'],
              ['Life Is Beautiful', 'http://ia.media-imdb.com/images/M/MV5BMTQwMTM2MjE4Ml5BMl5BanBnXkFtZTgwODQ2NTYxMTE@._V1_SX214_AL_.jpg'],
              ['Inside Out', 'http://ia.media-imdb.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_SX214_AL_.jpg'],
              ['Snatch', 'http://ia.media-imdb.com/images/M/MV5BMTk5NzE0MDQyNl5BMl5BanBnXkFtZTcwNzk4Mjk3OA@@._V1_SY317_CR2,0,214,317_AL_.jpg'],
              ['The Good, the Bad and the Ugly', 'http://ia.media-imdb.com/images/M/MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_SX214_AL_.jpg'],
              ['Goodfellas', 'http://ia.media-imdb.com/images/M/MV5BMTY2OTE5MzQ3MV5BMl5BanBnXkFtZTgwMTY2NTYxMTE@._V1_SX214_AL_.jpg'],
              ['City of God', 'http://ia.media-imdb.com/images/M/MV5BMjA4ODQ3ODkzNV5BMl5BanBnXkFtZTYwOTc4NDI3._V1_SX214_AL_.jpg']]


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")


class Collector(tornado.web.RequestHandler):
    def get(self):
        self.render("collector.html")


class getInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        (movie_name, movie_image) = movies[random.randrange(20)]
        json_dict = {"movieId": random.randrange(5), "movieName": movie_name, "movieImage": movie_image,
                     "recipeId": random.randrange(5), "recipeName": random.randrange(5), "recipeImage": random.randrange(5)}
        self.finish(json.dump(json_dict, self))


class postRate(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        print('POST')
        print('FOODID POST EREZ')
        print(self.get_argument('foodId'))
        print('MOVIEID')
        print(self.get_argument('movieId'))
        print('RATE')
        print(self.get_argument('rate'))
        self.finish()


settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static")
)


def make_app():
    return tornado.web.Application([
        (r"/", Collector),
        (r"/getInfo", getInfo),
        (r"/postRate", postRate),
        (r"/mainSite", MainHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()

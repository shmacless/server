import tornado.ioloop
import tornado.web
import json
import os
import random


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("DeliciouSeret")


class Collector(tornado.web.RequestHandler):
    def get(self):
        self.render("collector.html")


class getInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        json_dict = {"movieId": random.randrange(5), "movieName": random.randrange(5), "movieImage": "movie_image", "recipeId": random.randrange(5), "recipeName": random.randrange(5), "recipeImage": "movie_image"}
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


settings = dict(
        static_path = os.path.join(os.path.dirname(__file__), "static")
    )


def make_app():
    return tornado.web.Application([
        (r"/", Collector),
        (r"/getInfo", getInfo),
        (r"/postRate", postRate),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()

import urllib

import tornado.ioloop
import tornado.web
import json
import os
import random
import urllib.request


movies = [['Pulp Fiction', 'http://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SX214_AL_.jpg'],
          ['Good Will Hunting', 'http://ia.media-imdb.com/images/M/MV5BMTk0NjY0Mzg5MF5BMl5BanBnXkFtZTcwNzM1OTM2MQ@@._V1_SY317_CR1,0,214,317_AL_.jpg'],
          ['The Big Lebowski', 'http://www.movieposterdb.com/posters/09_02/1998/118715/l_118715_e3aa6190.jpg'],
          ['V for Vendetta', 'http://ia.media-imdb.com/images/M/MV5BOTI5ODc3NzExNV5BMl5BanBnXkFtZTcwNzYxNzQzMw@@._V1_SY317_CR0,0,214,317_AL_.jpg'],
          ['Fight Club', 'http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_SX214_AL_.jpg'],
          ['Gladiator', 'http://www.movieposterdb.com/posters/08_08/2000/172495/l_172495_2cce6a7c.jpg'],
          ['Interstellar', 'http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX214_AL_.jpg'],
          ['Into the Wild', 'http://www.movieposterdb.com/posters/08_03/2007/758758/l_758758_cf9ee8b4.jpg'],
          ['The Imitation Game', 'http://ia.media-imdb.com/images/M/MV5BNDkwNTEyMzkzNl5BMl5BanBnXkFtZTgwNTAwNzk3MjE@._V1_SY317_CR0,0,214,317_AL_.jpg'],
          ['The Truman Show', 'http://ia.media-imdb.com/images/M/MV5BMTg4NTU3NTAyMF5BMl5BanBnXkFtZTgwNjYwNzc3NjE@._V1_SX214_AL_.jpg'],
          ['Toy Story 3', 'http://www.movieposterdb.com/posters/10_04/2010/435761/l_435761_1e6b9c8e.jpg'],
          ['Shawshank Redemption', 'http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg'],
          ['Forrest Gump', 'http://ia.media-imdb.com/images/M/MV5BMTQwMTA5MzI1MF5BMl5BanBnXkFtZTcwMzY5Mzg3OA@@._V1_SX214_AL_.jpg'],
          ['Matrix', 'http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg'],
          ['Life Is Beautiful', 'http://ia.media-imdb.com/images/M/MV5BMTQwMTM2MjE4Ml5BMl5BanBnXkFtZTgwODQ2NTYxMTE@._V1_SX214_AL_.jpg'],
          ['Inside Out', 'http://ia.media-imdb.com/images/M/MV5BOTgxMDQwMDk0OF5BMl5BanBnXkFtZTgwNjU5OTg2NDE@._V1_SX214_AL_.jpg'],
          ['Snatch', 'http://ia.media-imdb.com/images/M/MV5BMTk5NzE0MDQyNl5BMl5BanBnXkFtZTcwNzk4Mjk3OA@@._V1_SY317_CR2,0,214,317_AL_.jpg'],
          ['The Good, the Bad and the Ugly', 'http://ia.media-imdb.com/images/M/MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_SX214_AL_.jpg'],
          ['Goodfellas', 'http://www.movieposterdb.com/posters/05_09/1990/0099685/l_50996_0099685_be22f728.jpg'],
          ['City of God', 'http://ia.media-imdb.com/images/M/MV5BMjA4ODQ3ODkzNV5BMl5BanBnXkFtZTYwOTc4NDI3._V1_SX214_AL_.jpg']]


foods = [['Black and White Affogato', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/05/Black-and-White-Affogato1-410x546.jpg'],
         ['Marvelous Meatballs!', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/04/Meatballs1-410x307.jpg'],
         ["Lia's Dark Chocolate Truffles", 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2010/12/5240497441_3188a021b4_o-420x280.jpg'],
         ['Spice Rubbed Flank Steak', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2014/10/Coffee-7-410x273.jpg'],
         ['Mile High Caramel Bars', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/05/0061-410x361.jpg'],
         ['Lentil Vegetable Soup with Whipped Feta', 'https://s-media-cache-ak0.pinimg.com/736x/24/87/2a/24872a474b46b4b821d788d560369cb4.jpg'],
         ['Lentil, Rice, and Raisin Pilaf', 'http://1.bp.blogspot.com/-3zKMEryxu1c/UnaoXYCkbyI/AAAAAAAAgN4/g5LVy6QBD7E/s1600/Persian-rice-pilaf-and-lentil.jpg'],
         ['Roasted Garlic Dungeness Crab', 'http://media-cache-ak0.pinimg.com/736x/e8/6b/0e/e86b0e4fb7caff9666526fccd9f416ee.jpg'],
         ['Whole Wheat Peanut Butter Chocolate Bread', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/03/DSCN5435-410x307.jpg'],
         ['Spicy Chipotle Shrimp Skewers', 'http://tastykitchen.com/recipes/wp-content/uploads/sites/2/2011/05/spicy-chipotle-shrimp-skewers-cropped-410x307.jpg'],
         ['Szechwan Green Beans', 'http://julievr.wpengine.netdna-cdn.com/wp-content/uploads/2012/05/Szechuan-green-beans-2.jpg'],
         ['Roasted Brussels Sprouts with Winter Squash', 'http://www.ihavenet.com/images/Roasted-Brussels-Sprouts-and-Winter-Squash-Recipe_DRW_12031.jpg'],
         ['Spinach and Mushroom Lasagna', 'http://www.jewelosco.com/wp-content/uploads/2014/10/spinach-mushroom-lasagna.png'],
         ['Sweet and Savoury Stir Fried Pork and Cashews', 'http://media-cache-ak0.pinimg.com/736x/64/da/75/64da751276ee12b7ca026593e3f9fb05.jpg'],
         ['Lentil, Walnut and Raisin Salad with Red Peppers','http://media-cache-ak0.pinimg.com/736x/c5/c2/84/c5c284de5cef2668ec155b13dcb008da.jpg'],
         ['Taco Flavored Ground Turkey', 'http://consumerrecipe.conagrafoods.com/uploadedImages/img_7417_7275.jpg'],
         ['Light BBQ Chicken Pizza', 'http://media-cache-ec0.pinimg.com/736x/a7/3c/92/a73c921920b09594507db1b4e31b80aa.jpg'],
         ['Pecan Pie Caramel Cheesecake', 'http://media-cache-ak0.pinimg.com/736x/fa/39/27/fa3927cc7f3bb009f00a893727c7beab.jpg'],
         ['Quick and Easy Cinnamon Walnut Bread', 'http://media-cache-ak0.pinimg.com/736x/5b/1f/32/5b1f3294830e0c2fdcbbdc491b247417.jpg'],
         ["Mom's Famous BBQ Pulled Chicken", 'http://www.eatingwell.com/sites/default/files/imagecache/standard/recipes/MP5102A_Scrivani.JPG']]


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")


class Collector(tornado.web.RequestHandler):
    def get(self):
        self.render("collector.html")


class getInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        (movie_name, movie_image) = movies[random.randrange(20)]
        (food_name, food_image) = foods[random.randrange(20)]
        # new_path = "static/tmp/" + str(movie_name).strip().lower() # todo remove
        # urllib.request.urlretrieve(movie_image, new_path) # todo remove
        json_dict = {"movieId": random.randrange(5), "movieName": movie_name, "movieImage": movie_image,
                     "recipeId": random.randrange(5), "recipeName": food_name, "recipeImage": food_image}
        self.finish(json.dump(json_dict, self))


class postRate(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        print('POST')
        food_name = self.get_argument('foodId')
        movie_name = self.get_argument('movieId')
        rate = self.get_argument('rate')
        with open("static/data/ratingDB", "a") as ratingDB:
            ratingDB.write("[" + food_name + ", " + movie_name + ", " + rate + "]" + ", \n")
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

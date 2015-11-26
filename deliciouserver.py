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


foods = [['Lescó', 'http://tastykitchen.com/recipes/soups/lesco/'],
         ['Marvelous Meatballs!', 'http://tastykitchen.com/recipes/main-courses/marvelous-meatballs/'],
         ['Spice Rubbed Flank Steak', 'http://tastykitchen.com/recipes/main-courses/spice-rubbed-flank-steak/'],
         ['Taco Sauce', 'http://tastykitchen.com/recipes/condiments/taco-sauce/'],
         ['Lentil Vegetable Soup with WhippedFeta', 'http://tastykitchen.com/recipes/soups/lentil-vegetable-soup-with-whipped-feta/'],
         ['Lentil, Rice, and Raisin Pilaf', 'http://tastykitchen.com/recipes/sidedishes/lentil-rice-and-raisin-pilaf/'],
         ['Roasted Garlic Dungeness Crab', 'http://tastykitchen.com/recipes/main-courses/roasted-garlic-dungeness-crab/'],
         ['Whole Wheat Peanut Butter Chocolate Bread', 'http://tastykitchen.com/recipes/breads/whole-wheat-peanut-butter-chocolate-bread/'],
         ['Spicy Chipotle Shrimp Skewers', 'http://tastykitchen.com/recipes/main-courses/spicy-chipotle-shrimp-skewers/'],
         ['Szechwan Green Beans', 'http://tastykitchen.com/recipes/main-courses/szechwan-green-beans/'],
         ['Spinach and Mushroom Lasagna', 'http://tastykitchen.com/recipes/main-courses/spinach-and-mushroom-lasagna/'],
         ['Roasted Brussels Sprouts with Winter Squash', 'http://tastykitchen.com/recipes/sidedishes/roasted-brussels-sprouts-with-winter-squash/'],
         ['Sweet and Savoury Stir Fried Pork and Cashews', 'http://tastykitchen.com/recipes/main-courses/sweet-and-savoury-stir-fried-pork-and-cashews/'],
         ['Lentil, Walnut and Raisin Salad with Red Peppers', 'http://tastykitchen.com/recipes/salads/lentil-walnut-and-raisin-salad-with-red-peppers/'],
         ['Taco Flavored Ground Turkey', 'http://tastykitchen.com/recipes/main-courses/taco-flavored-ground-turkey/'],
         ['Light BBQ Chicken Pizza', 'http://tastykitchen.com/recipes/main-courses/light-bbq-chicken-pizza/'],
         ['Pecan Pie Caramel Cheesecake', 'http://tastykitchen.com/recipes/desserts/pecan-pie-caramel-cheesecake/'],
         ['Quick and Easy Cinnamon Walnut Bread', 'http://tastykitchen.com/recipes/breads/quick-and-easy-cinnamon-walnut-bread/']]


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

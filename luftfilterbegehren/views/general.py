from random import shuffle
from flask import Blueprint, render_template, abort
from database.models import Cities

mod = Blueprint("general", __name__)
citiesObjects = Cities()


@mod.route("/")
def index():
    return render_template("general/index.html")


@mod.route("/gemeinden/")
def cities():
    cities_random = citiesObjects.cities
    shuffle(cities_random)
    return render_template(
        "act/cities.html",
        cities=cities_random
    )


@mod.route("/gemeinde/<prettyname>/")
def city(prettyname):
    city = citiesObjects.get_city_by_name(prettyname)
    if city:
        return render_template(
            "act/city.html",
            city=city
        )
    else:
        abort(404)


@mod.route("/weitersagen/")
def share():
    return render_template("general/share.html")


@mod.route("/unterstützer/")
def supporters():
    return render_template("general/supporters.html")


@mod.route("/faq/")
def faq():
    return render_template("general/faq.html")


@mod.route("/datenschutz/")
def privacy():
    return render_template("general/privacy.html")

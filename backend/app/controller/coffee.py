from flask_restx import Resource
from flask import request, send_file, render_template
from app.util.coffee_dto import CoffeeDto
from app.model import Coffee
from app import db
from flask_cors import  cross_origin
from app.service.coffee_service import make_coffee, number_of_espresso
from app import mqtt
from datetime import datetime
from app.service.visualization_service import create_coffee_usage_png

api = CoffeeDto.api
_coffee = CoffeeDto.model
_coffee_getter = CoffeeDto.model_get_coffee


@api.route('/GetCoffeeUsageEspresso')
class SentimentAnalysis(Resource):
    @api.doc('Get coffee history for Espressi')
    @api.response(404, 'Error in getting Coffee history')
    def get(self):
        create_coffee_usage_png()
        return send_file("../pics/espresso_usage.png")

@api.route('/GetNumberOfEspresso')
class SentimentAnalysis(Resource):
    @api.doc('Get number of Espressi all together')
    @api.response(404, 'Error in getting Coffee history')
    def get(self):
        return {"number" : number_of_espresso()}

@api.route('/GetCoffeeUsageDoubleEspresso')
class SentimentAnalysis(Resource):
    @api.doc('Get coffee history for doouble Espressi')
    @api.response(404, 'Error in getting Coffee history')
    def get(self):
        return send_file("../pics/double_espresso_usage.png")

@api.route('/TestCoffee')
class SentimentAnalysis(Resource):
    @api.doc('Test')
    @api.response(404, 'Error in getting Coffee history')
    def get(self):
        coffee = Coffee(datetime="test", type_coffee="test")
        db.session.add(coffee)
        db.session.commit()
        return {"data" : "success"} #get_coffee_history()}

@api.route('/MakeCoffee')
class MakeCoffee(Resource):
    @api.doc('Make a Coffee: "espresso" or "double_espresso"')
    @api.expect(_coffee_getter, envelope='data')
    @api.response(404, 'Error while making coffee')
    def post(self):
        data = request.json
        type_coffee = data["type_coffee"] #["espresso" "double_espresso"]
        make_coffee(type_coffee)
        return {"status": "success", "type_coffee" : type_coffee}

# @api.route('/GetCoffeeUsageAll')
# class SentimentAnalysis(Resource):
#     @api.doc('Get coffee history for all types of coffee')
#     @api.response(404, 'Error in getting Coffee history')
#     def get(self):
#         create_coffee_usage_png()
#         return send_file("../pics/all_usage.png")
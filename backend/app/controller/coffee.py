from flask_restx import Resource
from flask import request, send_file, render_template
from app.util.coffee_dto import CoffeeDto
from app.model import Coffee
from app import db
from flask_cors import  cross_origin
from app.service.coffee_service import make_coffee
from app import mqtt
from datetime import datetime
from app.service.visualization_service import get_df, print_df

api = CoffeeDto.api
_coffee = CoffeeDto.model
_coffee_getter = CoffeeDto.model_get_coffee


@api.route('/GetCoffeeHistory')
class SentimentAnalysis(Resource):
    @api.doc('Get coffee history')
    @api.response(404, 'Error in getting Coffee history')
    def get(self):
        print_df()
        return {"data" : get_df()}

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



# @api.route('/WordloudAll')
# class WordloudAll(Resource):
#     @api.doc('WordloudAll')
#     @api.response(404, 'Error')
#     def get(self):
#         return send_file("../output/wordcloud_all.png")

# @api.route('/WordloudPositive')
# class WordloudPositive(Resource):
#     @api.doc('WordloudPositive')
#     @api.response(404, 'Error')
#     def get(self):
#         return send_file("../output/wordcloud_positive.png")

# @api.route('/WordloudNegative')
# class WordloudNegative(Resource):
#     @api.doc('WordloudNegative')
#     @api.response(404, 'Error')
#     def get(self):
#         return send_file("../output/wordcloud_negative.png")

# @api.route('/SentimentAmount')
# class SentimentAmount(Resource):
#     @api.doc('SentimentAmount')
#     @api.response(404, 'Error')
#     def get(self):
#         return send_file("../output/Sentiment_Amount.png")

# @api.route('/SentimentBoxplot')
# class SentimentBoxplot(Resource):
#     @api.doc('SentimentBoxplot')
#     @api.response(404, 'Error')
#     def get(self):
#         return send_file("../output/Sentiment_Boxplot.png")

# @api.route('/PriceHistory')
# class PriceHistory(Resource):
#     @api.doc('PriceHistory')
#     @api.response(404, 'Error')
#     def get(self):
#         return send_file("../output/PriceHistory.png")

# @api.route('/ModelPrediction')
# class ModelPrediction(Resource):
#     @api.doc('ModelPrediction')
#     @api.response(404, 'Error')
#     def get(self):
#         return send_file("../output/ModelPrediction.png")


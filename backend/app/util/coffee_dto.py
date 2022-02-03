from flask_restx import Namespace, fields

class CoffeeDto():
    api = Namespace('Coffee', description='')
    model = api.model('Coffee model', {
        'type_coffee': fields.String(required=True),
        'datetime': fields.String(required=True),
    })
    model_get_coffee = api.model('TSA', {
        'type_coffee': fields.String(required=True),
    })

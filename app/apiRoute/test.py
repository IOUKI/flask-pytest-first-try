from flask import Blueprint, request, jsonify
from flask.views import MethodView

router = Blueprint('testRouter', __name__)

class Test(MethodView):

    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return jsonify({'hello': 'world'}), 200
    
    def post(self):
        try:
            content = request.get_json()['content']
            return jsonify({'content': content}), 200
        
        except Exception as e:
            return jsonify({'Error': e}), 200
        

class TestWithId(MethodView):
    
    def __init__(self) -> None:
        super().__init__()

    def get(self, id):
        return jsonify({'id': id}), 200
    
router.add_url_rule('', view_func=Test.as_view('Test'))
router.add_url_rule('/<id>', view_func=TestWithId.as_view('TestWithId'))
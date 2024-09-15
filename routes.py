from flask import Blueprint, request, jsonify
from models import db, Faq
from schemas import FaqSchema

faqs_bp = Blueprint('faqs', __name__)

faq_schema = FaqSchema()
faqs_schema = FaqSchema(many=True)

@faqs_bp.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = Faq.query.all()
    return jsonify(faqs_schema.dump(faqs))

@faqs_bp.route('/faqs/<int:id>', methods=['GET'])
def get_faq(id):
    faq = Faq.query.get_or_404(id)
    return faq_schema.jsonify(faq)

@faqs_bp.route('/faqs', methods=['POST'])
def create_faq():
    data = request.json
    errors = faq_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    new_faq = Faq(question=data['question'], answer=data['answer'])
    db.session.add(new_faq)
    db.session.commit()
    return faq_schema.jsonify(new_faq), 201

@faqs_bp.route('/faqs/<int:id>', methods=['PUT'])
def update_faq(id):
    faq = Faq.query.get_or_404(id)
    data = request.json
    errors = faq_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    faq.question = data['question']
    faq.answer = data['answer']
    db.session.commit()
    return faq_schema.jsonify(faq)

@faqs_bp.route('/faqs/<int:id>', methods=['DELETE'])
def delete_faq(id):
    faq = Faq.query.get_or_404(id)
    db.session.delete(faq)
    db.session.commit()
    return '', 204

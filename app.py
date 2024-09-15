import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Railway!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


# In-memory storage for FAQs
faqs = []

# Fetch all FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

# Create a new FAQ
@app.route('/faqs', methods=['POST'])
def add_faq():
    data = request.get_json()
    new_faq = {
        "id": len(faqs) + 1,
        "question": data['question'],
        "answer": data['answer']
    }
    faqs.append(new_faq)
    return jsonify(new_faq), 201

# Update an FAQ
@app.route('/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    data = request.get_json()
    for faq in faqs:
        if faq['id'] == faq_id:
            faq['question'] = data['question']
            faq['answer'] = data['answer']
            return jsonify(faq)
    return jsonify({"error": "FAQ not found"}), 404

# Delete an FAQ
@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    global faqs
    faqs = [faq for faq in faqs if faq['id'] != faq_id]
    return jsonify({"message": "FAQ deleted"}), 200

from flask import Flask
from routes import faqs_bp
from database import create_app, db

app = create_app()
app.register_blueprint(faqs_bp)

with app.app_context():
    db.create_all()  

if __name__ == '__main__':
    app.run(debug=True)

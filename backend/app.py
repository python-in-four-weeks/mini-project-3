from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"

    from .utils.custom_json_provider import CustomJsonProvider

    app.json = CustomJsonProvider(app)

    from .config.cors import cors
    from .config.sqlalchemy import db
    from .config.marshmallow import marshmallow

    features = cors, db, marshmallow
    for feature in features:
        feature.init_app(app)

    from .models.book import Book
    from .models.customer import Customer
    from .models.loan import Loan

    tables = Book, Customer, Loan
    with app.app_context():
        db.create_all()
        if not any(table.query.first() for table in tables):
            from .database.sample_data import books, customers, loans

            db.session.add_all(books)
            db.session.add_all(customers)
            db.session.add_all(loans)
            db.session.commit()

    from .views.book_endpoints import book_endpoints
    from .views.customer_endpoints import customer_endpoints
    from .views.loan_endpoints import loan_endpoints

    app.register_blueprint(book_endpoints)
    app.register_blueprint(customer_endpoints)
    app.register_blueprint(loan_endpoints)

    return app

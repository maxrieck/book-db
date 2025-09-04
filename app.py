from application import create_app, db

# Runs the app

app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# To mmigrate changes with models, run these commands in terminal

# flask --app app.py db migrate -m "describe your change"

# flask --app app.py db upgrade
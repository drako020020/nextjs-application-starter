from app import create_app
from app.extensions import db
from app.models import User

app = create_app()

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

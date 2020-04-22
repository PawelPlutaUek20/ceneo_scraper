#import bibliotek
from flask import Flask

#utworzenie obiektu (instacji) klasy Flask reprezentującrgo aplikację
app = Flask(__name__)

#import widoków/routungów z aplikacji
from app import views

if __name__ == "__main__": 
    app.run(debug=True)
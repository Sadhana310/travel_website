import flask

app = flask.Flask(__name__)

# Sample destination data
destinations = [
    {
        "id": 1,
        "name": "Similan Islands, Thailand",
        "country": "Thailand, Asia",
        "rating": "4.8",
        "price": "$160 / 4 days",
        "image": "similan.png",
        "reviews": "1,230 reviews",
        "description": "Known for crystal-clear waters, coral reefs, and white sand beaches."
    },
    {
        "id": 2,
        "name": "Bora Bora, French Polynesia",
        "country": "French Polynesia",
        "rating": "4.9",
        "price": "$500 / 5 days",
        "image": "similan.png",
        "reviews": "2,500 reviews",
        "description": "Famous for its luxury overwater bungalows and turquoise lagoon."
    },
    {
        "id": 3,
        "name": "Santorini, Greece",
        "country": "Greece, Europe",
        "rating": "4.7",
        "price": "$300 / 3 days",
        "image": "similan.png",
        "reviews": "3,100 reviews",
        "description": "Iconic for its whitewashed, cubiform houses and stunning sunsets."
    }
]

@app.route('/')
def index():
    print("Serving the index page.")
    sorted_destinations = sorted(destinations, key=lambda d: d['name'])
    return flask.render_template("index.html", destinations=sorted_destinations)

@app.route('/destination/<int:id>')
def detail(id):
    dest = next((d for d in destinations if d["id"] == id), None)
    return flask.render_template("detail.html", destination=dest)

if __name__ == '__main__':
    app.run(debug=True)

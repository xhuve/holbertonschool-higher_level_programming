from flask import Flask, render_template
import csv
import json

app = Flask(__name__)

@app.route('/<string:source>', defaults={'id': None})
@app.route('/<string:source>/<string:id>')
def hello(source, id):
    if source == "json":
        with open("./products.json") as f:
            parsed_data = json.load(f)
            if id:
                return render_template("product_display.html", allProducts=((value for value in parsed_data if id == value.get("id", None)), None))
            else:
                return render_template("product_display.html", allProducts=parsed_data)
    elif source == "csv":
        with open("./products.csv", mode="r") as f:
            reader = csv.DictReader(f)
            if id:
                csvData = next((value for value in reader if id == value["id"]), None)
                if not csvData:
                    return render_template("product_display.html", error="Product not found")
                return render_template("product_display.html", allProducts=csvData)
            else:
                return render_template("product_display.html", allProducts=[value for value in reader])

    return render_template("product_display.html", error="Wrong source")

if __name__ == '__main__':
    app.run(debug=True)
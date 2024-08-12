from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__)

@app.route('/products')
def hello():
    source = request.args.get("source")
    if source == "json":
        with open("./products.json") as f:
            parsed_data = json.load(f)
            id = request.args.get("id")
            if id:
                specificData = [value for value in parsed_data if int(id) == value.get("id", None)]
                if not specificData:
                    return render_template("product_display.html", error="Product not found")
                return render_template("product_display.html", allProducts=specificData)
            return render_template("product_display.html", allProducts=parsed_data)
    elif source == "csv":
        with open("./products.csv", mode="r") as f:
            reader = csv.DictReader(f)
            id = request.args.get("id")
            if id:
                csvData = [value for value in reader if id == value.get("id", None)]
                if not csvData:
                    return render_template("product_display.html", error="Product not found")
                return render_template("product_display.html", allProducts=csvData)
            return render_template("product_display.html", allProducts=[value for value in reader])

    return render_template("product_display.html", error="Wrong source")

if __name__ == '__main__':
    app.run(debug=True)
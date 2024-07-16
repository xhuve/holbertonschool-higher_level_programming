import sqlite3
from flask import Flask, render_template, request
import csv, json

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

@app.route('/products')
def hello():
    source = request.args.get("source")
    id = request.args.get("id")
    if source == "json":
        with open("./products.json") as f:
            parsed_data = json.load(f)
            if id:
                specificData = [value for value in parsed_data if int(id) == value.get("id", None)]
                if not specificData:
                    return render_template("product_display.html", error="Product not found")
                return render_template("product_display.html", allProducts=specificData)
            return render_template("product_display.html", allProducts=parsed_data)
    elif source == "csv":
        with open("./products.csv", mode="r") as f:
            reader = csv.DictReader(f)
            if id:
                csvData = [value for value in reader if id == value.get("id", None)]
                if not csvData:
                    return render_template("product_display.html", error="Product not found")
                return render_template("product_display.html", allProducts=csvData)
            return render_template("product_display.html", allProducts=[value for value in reader])
    elif source == "sql":
        create_database()
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        if id:
            sqlData = cur.execute(f"SELECT * FROM Products WHERE id = {int(id)}").fetchone()
            if not sqlData:
                return render_template("product_display.html", error="Product not found")
            return render_template("product_display.html", allProducts=[sqlData])
        else:
            print(cur.execute("SELECT * FROM Products").fetchall())
            return render_template("product_display.html", allProducts=cur.execute("SELECT * FROM Products").fetchall())

    return render_template("product_display.html", error="Wrong source")

if __name__ == '__main__':
    app.run(debug=True)
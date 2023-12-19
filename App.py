from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class MerchandiseItem:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

class MerchandiseMarket:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return f"{item.nama} added to the merchandise market."

    def update_item(self, kode, new_nama, new_harga):
        for item in self.items:
            if item.kode == kode:
                item.nama = new_nama
                item.harga = new_harga
                return f"{item.nama} updated successfully."
        return "Item not found."

    def delete_item(self, kode):
        for item in self.items:
            if item.kode == kode:
                self.items.remove(item)
                return f"{item.nama} deleted successfully."
        return "Item not found."

    def display_items(self):
        items_data = []
        for item in self.items:
            items_data.append({
                'kode': item.kode,
                'nama': item.nama,
                'harga': item.harga
            })
        return items_data

merchandise_market = MerchandiseMarket()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add your registration logic here (e.g., store credentials)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    items_data = merchandise_market.display_items()
    return render_template('dashboard.html', items=items_data)

if __name__ == '__main__':
    app.run(debug=True)

# app.py

from flask import Flask, render_template, request
from controller.menu_controller import MenuController

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/menu")
def show_menu():
    controller = MenuController()
    return controller.request_menu()

@app.route("/createMenu")
def create_menu():
    controller = MenuController()
    return controller.create_menu()

@app.route("/storeMenu", methods=['POST'])
def store_menu():
    controller = MenuController()
    return controller.store_menu()

if __name__ == "__main__":
    app.run(debug=True)

# menu_controller.py

from flask import render_template, request, redirect, url_for
from model.menu_model import MenuModel

class MenuController:
    def __init__(self):
        self.model = MenuModel()

    def request_menu(self):
        """
        Fetch menu items from the model, then render a template.
        """
        menu_items = self.model.get_menu()
        # Render 'menu.html' and pass menu_items as 'items'
        return render_template("menu.html", items=menu_items)

    def create_menu(self):
        return render_template("menu_form.html")

    def store_menu(self):
        name = request.form.get("name")
        price = request.form.get("price")
        description = request.form.get("description")

        self.model.store_menu(name,price,description)

        return redirect(url_for("show_menu"))



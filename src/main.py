import flet as ft
from routes import setup_routes

def main(page: ft.Page):
    page.title = "Mini curso de Flet"
    page.theme_mode = ft.ThemeMode.SYSTEM
    setup_routes(page)  # Toda la lógica delegada

ft.app(target=main, assets_dir="assets")

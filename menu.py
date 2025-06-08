import flet as ft
from theme import set_theme_light, set_theme_dark, set_theme_system

def create_theme_menu(page):
    return ft.PopupMenuButton(
        content=ft.Row([ft.Icon(ft.Icons.BRIGHTNESS_4_OUTLINED), ft.Text("Tema")]),
        items=[
            ft.PopupMenuItem(content=ft.Row([ft.Icon(ft.Icons.LIGHT_MODE), ft.Text("Claro")]), on_click=lambda e: set_theme_light(page)),
            ft.PopupMenuItem(content=ft.Row([ft.Icon(ft.Icons.DARK_MODE), ft.Text("Oscuro")]), on_click=lambda e: set_theme_dark(page)),
            ft.PopupMenuItem(content=ft.Row([ft.Icon(ft.Icons.SETTINGS_BRIGHTNESS), ft.Text("Sistema")]), on_click=lambda e: set_theme_system(page)),
        ]
    )

def create_social_media_and_options_menu(page):
    def launch(url):
        return lambda e: page.launch_url(url)

    def go_to_about_page(e):
        page.go("/about")

    return ft.PopupMenuButton(
        icon=ft.Icons.MENU,
        tooltip="Opciones y Redes Sociales",
        items=[
            ft.PopupMenuItem(content=ft.Row([ft.Image(src="discord.png", width=24, height=24), ft.Text("Discord")]), on_click=launch("https://discord.com/users/1374560616404226209")),
            ft.PopupMenuItem(content=ft.Row([ft.Image(src="gh.png", width=24, height=24), ft.Text("Github")]), on_click=launch("https://github.com/andromux/")),
            ft.PopupMenuItem(content=ft.Row([ft.Image(src="facebook.png", width=24, height=24), ft.Text("Facebook")]), on_click=launch("https://www.facebook.com/andromux")),
            ft.PopupMenuItem(content=ft.Row([ft.Image(src="youtube.png", width=24, height=24), ft.Text("YouTube")]), on_click=launch("https://www.youtube.com/@Retired64")),
            ft.PopupMenuItem(content=ft.Row([ft.Image(src="web.png", width=24, height=24), ft.Text("Andromux.org")]), on_click=launch("https://www.andromux.org")),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(content=create_theme_menu(page)),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(text="Acerca de", icon=ft.Icons.INFO, on_click=go_to_about_page),
        ]
    )

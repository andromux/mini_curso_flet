import flet as ft
from theme import set_theme_light, set_theme_dark, set_theme_system
from clase_boton import get_social_menu_items

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
    theme_submenu = create_theme_menu(page)
    menu_items = get_social_menu_items(page) + [
        ft.PopupMenuItem(content=theme_submenu),
        ft.PopupMenuItem(),
        ft.PopupMenuItem(text="Acerca de", icon=ft.Icons.INFO, on_click=lambda e: page.go("/about")),
    ]

    return ft.PopupMenuButton(
        icon=ft.Icons.MENU,
        tooltip="Menú",
        items=menu_items,
    )

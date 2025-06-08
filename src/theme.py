import flet as ft

def set_theme_light(page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

def set_theme_dark(page):
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

def set_theme_system(page):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.update()

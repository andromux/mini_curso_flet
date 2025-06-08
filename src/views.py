import flet as ft
from menu import create_social_media_and_options_menu

def home_view(page):
    return ft.View(
        "/",
        controls=[
            ft.AppBar(
                title=ft.Text("Mini curso Flet + GitHub Actions", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.BLUE_800,
                actions=[create_social_media_and_options_menu(page)],
            ),
            ft.Container(
                padding=30,
                expand=True,
                content=ft.Column(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Text("📦 Bienvenido a la Introducción de GitHub Actions", size=22, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ft.Text(
                            "GitHub Actions te permite automatizar tareas de desarrollo como testeo, despliegue y CI/CD directamente desde tu repositorio.",
                            size=16,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        ft.Divider(height=30),
                        ft.Text("🔀 ¿Qué es la navegación y rutas en Flet?", size=20, weight=ft.FontWeight.W_600),
                        ft.Text(
                            "La navegación en Flet te permite construir aplicaciones tipo SPA (Single Page Application), donde puedes cambiar de página sin recargar todo.",
                            size=16
                        ),
                        ft.Text(
                            "Gracias a `page.route`, puedes detectar la URL actual, navegar entre vistas y mantener sincronía con el historial del navegador.",
                            size=16
                        ),
                        ft.Divider(height=20),
                        ft.ElevatedButton(
                            "Ver ejemplo de rutas",
                            icon=ft.Icons.ARROW_FORWARD,
                            on_click=lambda e: page.go("/about"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE)
                        ),
                        ft.Container(height=50),  # extra espacio para evitar solape con la barra inferior en móviles
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        ],
        bgcolor=page.bgcolor
    )


def about_view(page):
    return ft.View(
        "/about",
        [
            ft.AppBar(
                title=ft.Text("Acerca de", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.BLUE_800,
                actions=[create_social_media_and_options_menu(page)],
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Bienvenido al Mini Curso de Flet!", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ft.Text("Esta es una aplicación de ejemplo simple para demostrar navegación y temas en Flet.", size=16, text_align=ft.TextAlign.CENTER),
                        ft.Divider(),
                        ft.Text("Desarrollado por: Andromux", size=14, italic=True),
                        ft.Text("Versión: 1.0", size=14, italic=True),
                        ft.Container(height=20),
                        ft.ElevatedButton(
                            "Volver al Inicio",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: page.go("/"),
                            style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                ),
                padding=20,
                expand=True,
            )
        ],
        bgcolor=page.bgcolor
    )

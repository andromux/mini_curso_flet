import flet as ft

# Modulo para usar en el menu.py y simplificar la creacion de botones de redes sociales
def social_button(name: str, url: str, icon_path: str = None, page=None):
    return ft.PopupMenuItem(
        content=ft.Row(
            [
                ft.Image(src=icon_path, width=24, height=24) if icon_path else ft.Icon(ft.icons.LINK),
                ft.Text(name),
            ]
        ),
        on_click=lambda e: page.launch_url(url),
    )

def get_social_menu_items(page):
    return [
        social_button("Discord", "https://discord.com/users/1374560616404226209", "discord.png", page),
        social_button("GitHub", "https://github.com/andromux/", "github.png", page),
        social_button("YouTube", "https://www.youtube.com/@Retired64", "youtube.png", page),
        social_button("Facebook", "https://www.facebook.com/andromux", "facebook.png", page),
        social_button("Sitio Web", "https://www.andromux.org", "web.png", page),
        #Aca puedes agregar mas botones de redes sociales reemplazando los enlaces y nombres y añadiendo los iconos correspondientes en la carpeta assets
        # social_button("Instagram", "https://www.instagram.com/andromux", "instagram.png", page),
        # social_button("Twitter", "https://twitter.com/andromuxorg", "twitter.png", page),
        # social_button("Sitio Web", "https://www.andromux.org", "web.png", page),
        ft.PopupMenuItem(),  # divisor
    ]

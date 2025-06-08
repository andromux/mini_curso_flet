import flet as ft

def main(page: ft.Page):
    page.title = "Mini curso de Flet"

    # --- Theme Mode Functions ---
    def set_theme_light(e):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def set_theme_dark(e):
        page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def set_theme_system(e):
        page.theme_mode = ft.ThemeMode.SYSTEM
        page.update()
    # --- End Theme Mode Functions ---

    # Function to open social media links
    def open_facebook(e):
        page.launch_url("https://www.facebook.com/your_facebook_page")

    def open_youtube(e):
        page.launch_url("youtube.com") # Replace with your YouTube channel URL

    def open_website(e):
        page.launch_url("https://www.andromux.org")

    # Create the PopupMenuButton for Theme Selection (nested menu)
    theme_submenu = ft.PopupMenuButton(
        content=ft.Row([
            ft.Icon(ft.Icons.BRIGHTNESS_4_OUTLINED), # Icon for Theme option
            ft.Text("Tema"),
        ]),
        items=[
            ft.PopupMenuItem(
                content=ft.Row([
                    ft.Icon(ft.Icons.LIGHT_MODE),
                    ft.Text("Claro"),
                ]),
                on_click=set_theme_light,
            ),
            ft.PopupMenuItem(
                content=ft.Row([
                    ft.Icon(ft.Icons.DARK_MODE),
                    ft.Text("Oscuro"),
                ]),
                on_click=set_theme_dark,
            ),
            ft.PopupMenuItem(
                content=ft.Row([
                    ft.Icon(ft.Icons.SETTINGS_BRIGHTNESS),
                    ft.Text("Sistema"),
                ]),
                on_click=set_theme_system,
            ),
        ]
    )

    # Create the main PopupMenuButton with social media options and the theme submenu
    social_media_and_options_menu = ft.PopupMenuButton(
        icon=ft.Icons.MENU, # Main icon for the whole menu
        tooltip="Opciones y Redes Sociales",
        items=[
            # Social Media Items
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Image(src="facebook.png", width=24, height=24), # Path to your custom Facebook icon
                        ft.Text("Facebook"),
                    ]
                ),
                on_click=open_facebook,
            ),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Image(src="youtube.png", width=24, height=24), # Path to your custom YouTube icon
                        ft.Text("YouTube"),
                    ]
                ),
                on_click=open_youtube,
            ),
            ft.PopupMenuItem(
                content=ft.Row(
                    [
                        ft.Image(src="web.png", width=24, height=24), # Path to your custom website icon
                        ft.Text("Andromux.org"),
                    ]
                ),
                on_click=open_website,
            ),
            ft.PopupMenuItem(), # Divider
            # Theme Submenu Item
            ft.PopupMenuItem(
                content=theme_submenu # Embed the theme submenu here
            ),
            ft.PopupMenuItem(), # Another Divider if needed
            ft.PopupMenuItem(text="Acerca de", icon=ft.Icons.INFO), # Example of another option
        ]
    )

    # Add the PopupMenuButton to the app bar
    page.appbar = ft.AppBar(
        title=ft.Text("Welcome!", color=ft.Colors.WHITE), # Keep appbar title white on blue
        bgcolor=ft.Colors.BLUE_800,
        actions=[
            social_media_and_options_menu,
        ],
    )

    # THIS IS THE KEY CHANGE: Remove explicit color from the main text
    page.add(ft.Text("Click el ícono del menú en la barra superior para explorar opciones y redes sociales!"))
    # Optionally, you could also set page.theme_mode initially based on system preference
    # page.theme_mode = ft.ThemeMode.SYSTEM # Or ft.ThemeMode.DARK / LIGHT based on your default preference

# Important: Make sure you have an 'assets' folder in the same directory as your Python script.
# Place your 'facebook.png', 'youtube.png', and 'web.png' files inside this 'assets' folder.
ft.app(target=main, assets_dir="assets")
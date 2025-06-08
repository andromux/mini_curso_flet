import flet as ft

def main(page: ft.Page):
    page.title = "Mini curso de Flet"
    # Set an initial theme mode for consistency and immediate adaptation
    page.theme_mode = ft.ThemeMode.SYSTEM # Start with system theme

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
    def open_discord(e):
        page.launch_url("https://discord.com/users/1374560616404226209")

    def open_github(e):
        page.launch_url("https://github.com/andromux/")

    def open_youtube(e):
        page.launch_url("https://www.youtube.com/@Retired64") # Replace with your YouTube channel URL

    def open_website(e):
        page.launch_url("https://www.andromux.org")
    
    def open_facebook(e):
        page.launch_url("https://www.facebook.com/andromux")

    # Function to navigate to the About page
    def go_to_about_page(e):
        page.go("/about") # Navigate to the /about route

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

    # The social media and options menu needs to be a function
    # because it's used in both home_view and about_view.
    def create_social_media_and_options_menu():
        return ft.PopupMenuButton(
            icon=ft.Icons.MENU, # Main icon for the whole menu
            tooltip="Opciones y Redes Sociales",
            items=[
                # Social Media Items
                ft.PopupMenuItem(
                    content=ft.Row(
                        [
                            ft.Image(src="discord.png", width=24, height=24), # Path to your custom Discord icon
                            ft.Text("Discord"),
                        ]
                    ),
                    on_click=open_discord,
                ),
                ft.PopupMenuItem(
                    content=ft.Row(
                        [
                            ft.Image(src="gh.png", width=24, height=24), # Path to your custom Github icon
                            ft.Text("Github"),
                        ]
                    ),
                    on_click=open_github,
                ),
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
                ft.PopupMenuItem(
                    text="Acerca de",
                    icon=ft.Icons.INFO,
                    on_click=go_to_about_page # Link to the new navigation function
                ),
            ]
        )

    # --- Page Views Definitions ---

    # Define the content for the Home Page (Initial View)
    def home_view():
        return ft.View(
            "/", # Route for the home page
            [
                ft.AppBar(
                    title=ft.Text("Welcome!", color=ft.Colors.WHITE), # Keep appbar title white on blue
                    bgcolor=ft.Colors.BLUE_800,
                    actions=[
                        create_social_media_and_options_menu(), # Add the menu here
                    ],
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Click el ícono del menú en la barra superior para explorar opciones y redes sociales!",
                                # Text color adapts automatically, no need to set ft.Colors.WHITE
                            ),
                            # You can add more content to your home page here
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                    ),
                    expand=True,
                    # Background for the main content area will adapt via page.bgcolor or its parent View's bgcolor
                )
            ],
            # Ensure the view's background adapts based on theme_mode
            bgcolor=page.bgcolor # Use page's adaptive background
        )

    # Define the content for the About Page
    def about_view():
        return ft.View(
            "/about", # Route for the about page
            [
                ft.AppBar(
                    title=ft.Text("Acerca de", color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.BLUE_800,
                    actions=[
                        create_social_media_and_options_menu(), # Keep the menu accessible on About page
                    ]
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Bienvenido al Mini Curso de Flet!",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER,
                                # Text color adapts automatically
                            ),
                            ft.Text(
                                "Esta es una aplicación de ejemplo simple para demostrar navegación y temas en Flet.",
                                size=16,
                                text_align=ft.TextAlign.CENTER,
                                # Text color adapts automatically
                            ),
                            ft.Divider(),
                            ft.Text(
                                "Desarrollado por: Andromux",
                                size=14,
                                italic=True,
                                # Text color adapts automatically
                            ),
                            ft.Text(
                                "Versión: 1.0",
                                size=14,
                                italic=True,
                                # Text color adapts automatically
                            ),
                            ft.Container(height=20), # Spacer
                            ft.ElevatedButton(
                                "Volver al Inicio",
                                icon=ft.Icons.ARROW_BACK,
                                on_click=lambda e: page.go("/"), # Navigate back to home
                                style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                    ),
                    padding=20,
                    expand=True,
                    # Container background will adapt via its parent View's bgcolor
                )
            ],
            # Ensure the view's background adapts based on theme_mode
            bgcolor=page.bgcolor # Use page's adaptive background
        )

    # --- Navigation Logic ---

    def route_change(route):
        page.views.clear() # Always clear views when route changes

        # Add views based on the current route
        page.views.append(home_view()) # Home view is always the base

        if page.route == "/about":
            page.views.append(about_view()) # Add About view on top if route is /about
        
        page.update() # Update the page to reflect the new view stack

    def view_pop(view):
        page.views.pop() # Remove the top view
        top_view = page.views[-1] # Get the route of the new top view
        page.go(top_view.route) # Navigate to that route

    # Set event handlers
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Go to the initial route when the app starts.
    # This will trigger `route_change` and set up the initial view.
    page.go(page.route)

# Important: Make sure you have an 'assets' folder in the same directory as your Python script.
# Place your 'facebook.png', 'youtube.png', and 'web.png' files inside this 'assets' folder.
ft.app(target=main, assets_dir="assets")
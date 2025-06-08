import flet as ft

def main(page: ft.Page):
    page.title = "Mini curso de Flet"

    # We declare social_media_menu here, though its properties are set below
    social_media_menu = ft.PopupMenuButton()

    # Function to open the Facebook link
    def open_facebook(e):
        # Use page.launch_url() for Flet to handle opening the URL
        page.launch_url("https://www.facebook.com/your_facebook_page") # Replace with your Facebook page URL
        # No need to call social_media_menu.close() here, the menu closes automatically

    # Function to open your website link
    def open_website(e):
        # Use page.launch_url() for Flet to handle opening the URL
        page.launch_url("https://www.andromux.org") # Replace with your website URL
        # No need to call social_media_menu.close() here, the menu closes automatically

    # Create the PopupMenuButton with social media options
    social_media_menu.icon = ft.Icons.MENU  # Icon for the menu button (Note the capital 'I' in Icons)
    social_media_menu.tooltip = "Social Media"
    social_media_menu.items = [
        ft.PopupMenuItem(text="Facebook", icon=ft.Icons.FACEBOOK, on_click=open_facebook),
        ft.PopupMenuItem(text="My Website", icon=ft.Icons.WEB, on_click=open_website),
    ]

    # Add the PopupMenuButton to the app bar
    page.appbar = ft.AppBar(
        title=ft.Text("Welcome!"),
        actions=[
            social_media_menu,
        ],
    )

    page.add(ft.Text("Click the menu icon in the app bar to find my social media!"))

ft.app(target=main)
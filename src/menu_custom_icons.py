import flet as ft

def main(page: ft.Page):
    page.title = "Mini curso de Flet"

    # We declare social_media_menu here, though its properties are set below
    social_media_menu = ft.PopupMenuButton()

    # Function to open the Facebook link
    def open_facebook(e):
        page.launch_url("https://www.facebook.com/your_facebook_page") # Replace with your Facebook page URL

    # Function to open your website link
    def open_website(e):
        page.launch_url("https://www.andromux.org") # Replace with your website URL
    
    # Function to open your YouTube channel link
    def open_youtube(e):
        page.launch_url("https://www.youtube.com/@Retired64") # Replace with your YouTube channel URL

    # Create the PopupMenuButton with social media options
    social_media_menu.icon = ft.Icons.MENU # Icon for the menu button
    social_media_menu.tooltip = "Social Media"
    social_media_menu.items = [
        # Custom Facebook icon
        ft.PopupMenuItem(
            content=ft.Row(
                [
                    ft.Image(src="facebook.png", width=24, height=24), # Path to your custom Facebook icon
                    ft.Text("@Andromux"),
                ]
            ),
            on_click=open_facebook,
        ),
        # Custom Website icon
        ft.PopupMenuItem(
            content=ft.Row(
                [
                    ft.Image(src="youtube.png", width=24, height=24), # Path to your custom website icon
                    ft.Text("@Andromux"),
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
    ]

    # Add the PopupMenuButton to the app bar
    page.appbar = ft.AppBar(
        title=ft.Text("Welcome!"),
        actions=[
            social_media_menu,
        ],
    )

    page.add(ft.Text("Click the menu icon in the app bar to find my social media!"))

# Important: Make sure you have an 'assets' folder in the same directory as your Python script.
# Place your 'facebook_icon.png' and 'web_icon.png' files inside this 'assets' folder.
ft.app(target=main, assets_dir="assets")
from views import home_view, about_view

def setup_routes(page):
    def route_change(route):
        page.views.clear()
        page.views.append(home_view(page))
        if page.route == "/about":
            page.views.append(about_view(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

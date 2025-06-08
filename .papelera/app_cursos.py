import flet as ft

# Modelos (similares a tus clases Dart)
class CodeExample:
    def __init__(self, title, code, explanation=""):
        self.title = title
        self.code = code
        self.explanation = explanation

class Lesson:
    def __init__(self, title, description, code_examples=None):
        self.title = title
        self.description = description
        self.code_examples = code_examples if code_examples is not None else []

# Datos de ejemplo
lessons_data = [
    Lesson(
        title="Lección 1: Introducción a Python",
        description="Python es un lenguaje de programación de alto nivel que es fácil de aprender y muy potente.",
        code_examples=[
            CodeExample(
                title="Hola Mundo en Python",
                code="""print("¡Hola, Mundo!")
nombre = "Python"
print(f"Me gusta programar en {nombre}")""",
                explanation="Esta línea imprime un mensaje en la consola y muestra el uso de f-strings."
            ),
            CodeExample(
                title="Variables y Tipos de Datos",
                code="""# Diferentes tipos de variables
numero = 42
texto = "Hola Python"
lista = [1, 2, 3, 4, 5]
diccionario = {"clave": "valor", "edad": 25}

# Mostrar tipos
print(type(numero))
print(type(texto))
print(type(lista))""",
                explanation="Python tiene varios tipos de datos básicos como enteros, strings, listas y diccionarios."
            )
        ]
    ),
    Lesson(
        title="Lección 2: Estructuras de Control",
        description="Las estructuras de control permiten dirigir el flujo de ejecución del programa.",
        code_examples=[
            CodeExample(
                title="Condicionales",
                code="""edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")""",
                explanation="Los condicionales if, elif y else permiten ejecutar código basado en condiciones."
            )
        ]
    ),
]

# Función para crear texto con resaltado de sintaxis (versión simplificada)
def create_syntax_highlighted_code(code):
    return ft.Text(
        code,
        font_family="Consolas",
        size=14,
        color=ft.Colors.GREEN_300,  # Verde claro para el código
        selectable=True,
    )

# Función alternativa más simple usando contenedor con estilo
def create_simple_code_block(code):
    return ft.Container(
        content=ft.Text(
            code,
            font_family="Consolas",
            size=14,
            color=ft.Colors.WHITE,
            selectable=True,
        ),
        bgcolor=ft.Colors.BLUE_GREY_900,
        padding=ft.padding.all(15),
        border_radius=ft.border_radius.all(8),
        border=ft.border.all(1, ft.Colors.BLUE_GREY_700)
    )

def copy_to_clipboard(page, code):
    page.set_clipboard(code)
    # You could also show a SnackBar notification here:
    # page.show_snack_bar(ft.SnackBar(ft.Text("¡Código copiado al portapapeles!"), open=True))
    page.update()
    print(f"Código copiado: {code[:50]}...")  # Mensaje en consola para debug


# --- Social Media Menu Integration ---

# Declare social_media_menu at the top level to make it accessible to click handlers
# We'll define it fully inside a function to allow page access, or pass page to it.
# A better approach is to define the menu creation as a function.

def create_social_media_menu(page):
    # Function to open the Facebook link
    def open_facebook(e):
        page.launch_url("https://www.facebook.com/your_facebook_page") # Replace with your Facebook page URL

    # Function to open your website link
    def open_website(e):
        page.launch_url("https://www.andromux.org") # Replace with your website URL

    return ft.PopupMenuButton(
        icon=ft.Icons.MENU,
        tooltip="Redes Sociales",
        items=[
            ft.PopupMenuItem(text="Facebook", icon=ft.Icons.FACEBOOK, on_click=open_facebook),
            ft.PopupMenuItem(text="Mi Web", icon=ft.Icons.WEB, on_click=open_website),
        ]
    )

# --- End Social Media Menu Integration ---


# Función para la página de la lección
def lesson_page_view(page: ft.Page, lesson: Lesson):
    code_blocks_and_explanations = []
    
    for example in lesson.code_examples:
        # Título del ejemplo
        code_blocks_and_explanations.append(
            ft.Container(
                content=ft.Text(
                    example.title, 
                    weight=ft.FontWeight.BOLD,
                    size=16,
                    color=ft.Colors.CYAN_300
                ),
                margin=ft.margin.only(top=20, bottom=10)
            )
        )
        
        # Contenedor del código con botón de copiar
        code_blocks_and_explanations.append(
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("Python", size=12, color=ft.Colors.GREY_400),
                        ft.Container(expand=True),  # Reemplaza Spacer
                        ft.IconButton(
                            icon=ft.Icons.COPY,
                            icon_size=16,
                            icon_color=ft.Colors.GREY_300,
                            tooltip="Copiar código",
                            on_click=lambda e, code=example.code: copy_to_clipboard(page, code)
                        )
                    ]),
                    ft.Divider(height=1, color=ft.Colors.GREY_600),
                    ft.Container(
                        content=create_syntax_highlighted_code(example.code),
                        padding=ft.padding.all(15),
                    )
                ]),
                bgcolor=ft.Colors.GREY_800,
                border_radius=ft.border_radius.all(8),
                border=ft.border.all(1, ft.Colors.GREY_600),
                margin=ft.margin.only(bottom=15)
            )
        )
        
        # Explicación
        if example.explanation:
            code_blocks_and_explanations.append(
                ft.Container(
                    content=ft.Text(
                        example.explanation,
                        italic=True,
                        size=14,
                        color=ft.Colors.GREY_300
                    ),
                    margin=ft.margin.only(bottom=20)
                )
            )

    return ft.View(
        "/lesson",
        [
            ft.AppBar(
                title=ft.Text(lesson.title, color=ft.Colors.WHITE),
                bgcolor=ft.Colors.BLUE_800,
                actions=[
                    create_social_media_menu(page), # Add the social media menu here
                ]
            ),
            ft.Container(
                content=ft.Column([
                    ft.Container(
                        content=ft.Text(
                            lesson.description, 
                            selectable=True,
                            size=16,
                            color=ft.Colors.GREY_200
                        ),
                        margin=ft.margin.only(bottom=20)
                    ),
                    ft.Text(
                        "Ejemplos de Código:", 
                        size=20, 
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_300
                    ),
                    *code_blocks_and_explanations,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
                scroll=ft.ScrollMode.AUTO,
                ),
                padding=20,
                expand=True,
                bgcolor=ft.Colors.GREY_900
            )
        ],
        bgcolor=ft.Colors.GREY_900
    )


# Función principal de la app
def main(page: ft.Page):
    page.title = "Curso de Python Flet"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.GREY_900
    page.update()

    def route_change(route):
        page.views.clear()
        
        # Main view (Lesson List)
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text(page.title, color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.BLUE_800,
                        actions=[
                            create_social_media_menu(page), # Add the social media menu here
                        ]
                    ),
                    ft.Container(
                        content=ft.ListView(
                            controls=[
                                ft.Card(
                                    content=ft.Container(
                                        content=ft.ListTile(
                                            title=ft.Text(
                                                lesson.title,
                                                weight=ft.FontWeight.BOLD,
                                                size=16,
                                                color=ft.Colors.WHITE
                                            ),
                                            subtitle=ft.Text(
                                                lesson.description.split('\n')[0], 
                                                max_lines=2, 
                                                overflow=ft.TextOverflow.ELLIPSIS,
                                                color=ft.Colors.GREY_300
                                            ),
                                            trailing=ft.Icon(
                                                ft.Icons.ARROW_FORWARD_IOS,
                                                color=ft.Colors.BLUE_300
                                            ),
                                            on_click=lambda e, lesson_obj=lesson: page.go(f"/lesson/{lesson_obj.title.replace(' ', '_')}")
                                        ),
                                        padding=ft.padding.all(5)
                                    ),
                                    elevation=5,
                                    margin=ft.margin.only(bottom=10),
                                    color=ft.Colors.GREY_800
                                ) for lesson in lessons_data
                            ],
                            padding=ft.padding.all(16)
                        ),
                        expand=True
                    )
                ],
                bgcolor=ft.Colors.GREY_900
            )
        )

        # Lesson Detail View
        if page.route.startswith("/lesson/"):
            lesson_title_param = page.route.split("/")[2].replace('_', ' ')
            selected_lesson = next((l for l in lessons_data if l.title == lesson_title_param), None)
            if selected_lesson:
                page.views.append(
                    lesson_page_view(page, selected_lesson)
                )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route) # Go to the initial route when the app starts

ft.app(target=main)
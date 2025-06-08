# Aprendiendo app

# Manual Completo: Aplicación Flet con Navegación y Temas

## Introducción
Este manual explica línea por línea una aplicación completa de Flet que incluye navegación entre páginas, cambio de temas, menús desplegables y enlaces a redes sociales.

## Estructura del Código

### 1. Importación de la Librería
```python
import flet as ft
```
**Explicación**: Importa la librería Flet y la renombra como `ft` para facilitar su uso. Flet es un framework para crear aplicaciones multiplataforma con Python.

---

### 2. Función Principal
```python
def main(page: ft.Page):
```
**Explicación**: Define la función principal que recibe un objeto `Page`. Este objeto representa la ventana/página principal de la aplicación y contiene todas las propiedades y métodos para controlar la interfaz.

---

### 3. Configuración Inicial de la Página
```python
page.title = "Mini curso de Flet"
page.theme_mode = ft.ThemeMode.SYSTEM
```
**Explicación**: 
- `page.title`: Establece el título que aparecerá en la barra de título de la ventana
- `page.theme_mode`: Configura el tema inicial. `SYSTEM` significa que seguirá el tema del sistema operativo (claro u oscuro)

---

### 4. Funciones para Cambio de Tema

#### Tema Claro
```python
def set_theme_light(e):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
```
**Explicación**: 
- Función que cambia el tema a modo claro
- `e` es el evento que se recibe cuando se hace clic
- `page.update()` actualiza la interfaz para aplicar los cambios

#### Tema Oscuro
```python
def set_theme_dark(e):
    page.theme_mode = ft.ThemeMode.DARK
    page.update()
```
**Explicación**: Similar a la anterior, pero cambia al tema oscuro

#### Tema del Sistema
```python
def set_theme_system(e):
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.update()
```
**Explicación**: Restaura el tema automático del sistema operativo

---

### 5. Funciones para Enlaces Externos

#### Discord
```python
def open_discord(e):
    page.launch_url("https://discord.com/users/1374560616404226209")
```
**Explicación**: 
- `page.launch_url()` abre una URL en el navegador predeterminado
- Se ejecuta cuando el usuario hace clic en la opción Discord del menú

#### GitHub
```python
def open_github(e):
    page.launch_url("https://github.com/andromux/")
```
**Explicación**: Abre el perfil de GitHub del desarrollador

#### YouTube, Website, Facebook
```python
def open_youtube(e):
    page.launch_url("https://www.youtube.com/@Retired64")

def open_website(e):
    page.launch_url("https://www.andromux.org")

def open_facebook(e):
    page.launch_url("https://www.facebook.com/andromux")
```
**Explicación**: Funciones similares para abrir diferentes redes sociales y sitio web

---

### 6. Navegación Entre Páginas
```python
def go_to_about_page(e):
    page.go("/about")
```
**Explicación**: 
- `page.go()` navega a una ruta específica
- "/about" es la ruta de la página "Acerca de"

---

### 7. Submenú de Temas

#### Botón Principal del Submenú
```python
theme_submenu = ft.PopupMenuButton(
    content=ft.Row([
        ft.Icon(ft.Icons.BRIGHTNESS_4_OUTLINED),
        ft.Text("Tema"),
    ]),
```
**Explicación**: 
- `PopupMenuButton`: Crea un botón que despliega un menú
- `content`: Define lo que se ve en el botón (ícono + texto)
- `ft.Row`: Organiza elementos horizontalmente
- `ft.Icon`: Muestra un ícono material design
- `ft.Text`: Muestra texto

#### Opciones del Submenú
```python
items=[
    ft.PopupMenuItem(
        content=ft.Row([
            ft.Icon(ft.Icons.LIGHT_MODE),
            ft.Text("Claro"),
        ]),
        on_click=set_theme_light,
    ),
```
**Explicación**: 
- `items`: Lista de opciones del menú
- `PopupMenuItem`: Cada opción del menú
- `on_click`: Función que se ejecuta al hacer clic

---

### 8. Función para Crear el Menú Principal

#### Definición de la Función
```python
def create_social_media_and_options_menu():
    return ft.PopupMenuButton(
        icon=ft.Icons.MENU,
        tooltip="Opciones y Redes Sociales",
```
**Explicación**: 
- Función que retorna el menú completo
- `icon`: Ícono que se muestra en el AppBar
- `tooltip`: Texto que aparece al pasar el mouse sobre el botón

#### Elementos del Menú - Discord
```python
ft.PopupMenuItem(
    content=ft.Row(
        [
            ft.Image(src="discord.png", width=24, height=24),
            ft.Text("Discord"),
        ]
    ),
    on_click=open_discord,
),
```
**Explicación**: 
- `ft.Image`: Muestra una imagen personalizada
- `src`: Ruta del archivo de imagen
- `width`, `height`: Dimensiones de la imagen
- `on_click`: Función que se ejecuta al seleccionar esta opción

#### Separadores
```python
ft.PopupMenuItem(), # Divider
```
**Explicación**: Un `PopupMenuItem` vacío actúa como separador visual en el menú

#### Submenú Anidado
```python
ft.PopupMenuItem(
    content=theme_submenu
),
```
**Explicación**: Incluye el submenú de temas dentro del menú principal

---

### 9. Vista de la Página Principal

#### Definición de la Vista
```python
def home_view():
    return ft.View(
        "/",
        [
```
**Explicación**: 
- Función que retorna la vista de la página principal
- `ft.View`: Representa una pantalla completa
- `"/"`: Ruta asociada con esta vista

#### AppBar
```python
ft.AppBar(
    title=ft.Text("Welcome!", color=ft.Colors.WHITE),
    bgcolor=ft.Colors.BLUE_800,
    actions=[
        create_social_media_and_options_menu(),
    ],
),
```
**Explicación**: 
- `ft.AppBar`: Barra superior de la aplicación
- `title`: Título que aparece en la barra
- `bgcolor`: Color de fondo de la AppBar
- `actions`: Lista de botones/menús en el lado derecho

#### Contenido Principal
```python
ft.Container(
    content=ft.Column(
        [
            ft.Text(
                "Click el ícono del menú en la barra superior para explorar opciones y redes sociales!",
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    ),
    expand=True,
)
```
**Explicación**: 
- `ft.Container`: Contenedor que puede tener padding, margin, color de fondo, etc.
- `ft.Column`: Organiza elementos verticalmente
- `horizontal_alignment`: Alineación horizontal de los elementos
- `alignment`: Alineación vertical de los elementos
- `expand=True`: El elemento toma todo el espacio disponible

---

### 10. Vista de la Página "Acerca de"

#### Estructura Similar
```python
def about_view():
    return ft.View(
        "/about",
        [
```
**Explicación**: Similar a `home_view()`, pero para la ruta "/about"

#### Contenido Específico
```python
ft.Text(
    "Bienvenido al Mini Curso de Flet!",
    size=24,
    weight=ft.FontWeight.BOLD,
    text_align=ft.TextAlign.CENTER,
),
```
**Explicación**: 
- `size`: Tamaño de la fuente
- `weight`: Grosor de la fuente (negrita)
- `text_align`: Alineación del texto

#### Botón de Regreso
```python
ft.ElevatedButton(
    "Volver al Inicio",
    icon=ft.Icons.ARROW_BACK,
    on_click=lambda e: page.go("/"),
    style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_700, color=ft.Colors.WHITE)
)
```
**Explicación**: 
- `ft.ElevatedButton`: Botón elevado con sombra
- `icon`: Ícono que aparece en el botón
- `lambda e: page.go("/")`: Función anónima que navega al inicio
- `style`: Personalización del estilo del botón

---

### 11. Lógica de Navegación

#### Cambio de Ruta
```python
def route_change(route):
    page.views.clear()
    
    page.views.append(home_view())
    
    if page.route == "/about":
        page.views.append(about_view())
    
    page.update()
```
**Explicación**: 
- Se ejecuta cuando cambia la ruta
- `page.views.clear()`: Limpia todas las vistas
- Siempre añade la vista principal como base
- Añade vistas adicionales según la ruta actual
- `page.update()`: Actualiza la interfaz

#### Navegación hacia Atrás
```python
def view_pop(view):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)
```
**Explicación**: 
- Se ejecuta cuando el usuario presiona "atrás"
- `page.views.pop()`: Elimina la vista superior
- `page.views[-1]`: Obtiene la nueva vista superior
- Navega a la ruta de esa vista

---

### 12. Configuración de Eventos
```python
page.on_route_change = route_change
page.on_view_pop = view_pop
```
**Explicación**: Asigna las funciones de manejo de eventos a los eventos de la página

---

### 13. Inicialización
```python
page.go(page.route)
```
**Explicación**: Navega a la ruta inicial, lo que activa `route_change` y configura la vista inicial

---

### 14. Ejecución de la Aplicación
```python
ft.app(target=main, assets_dir="assets")
```
**Explicación**: 
- `ft.app()`: Inicia la aplicación Flet
- `target=main`: Especifica la función principal
- `assets_dir="assets"`: Carpeta donde están los archivos de recursos (imágenes)

---

## Conceptos Clave Aprendidos

### 1. **Estructura de una App Flet**
- Función principal que recibe un objeto `Page`
- Configuración inicial de la página
- Definición de vistas y navegación

### 2. **Componentes de UI**
- `AppBar`: Barra superior
- `Container`: Contenedor con propiedades de layout
- `Column/Row`: Organización vertical/horizontal
- `Text, Icon, Image`: Elementos básicos
- `PopupMenuButton`: Menús desplegables

### 3. **Navegación**
- Sistema de rutas con `page.go()`
- Stack de vistas con `page.views`
- Manejo de eventos de navegación

### 4. **Temas y Estilos**
- Cambio dinámico de temas
- Personalización de colores y estilos
- Adaptación automática según el tema

### 5. **Interactividad**
- Manejo de eventos con `on_click`
- Funciones callback para responder a acciones del usuario
- Integración con URLs externas

Este código demuestra una aplicación completa y profesional que puede servir como base para proyectos más complejos.

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).

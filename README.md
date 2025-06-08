Este manual de aprendizaje tiene como objetivo proporcionar una guía detallada y clara sobre el proyecto "Mini curso de Flet", explicando la funcionalidad de cada módulo local, el propósito de su creación y cómo contribuyen al funcionamiento general de la aplicación. Está diseñado para usuarios con poca o ninguna experiencia en Flet, ofreciendo una visión completa del proyecto.

## Manual de Aprendizaje del Proyecto "Mini curso de Flet"

### 1. Introducción al Proyecto

Este proyecto es una aplicación sencilla desarrollada con Flet, un framework que permite crear aplicaciones de escritorio y web con Python. El objetivo principal es demostrar conceptos fundamentales como la navegación entre vistas (páginas) y la gestión de temas (claro/oscuro/sistema), además de integrar botones para redes sociales. La aplicación está modularizada, lo que significa que su código está dividido en archivos más pequeños y organizados para mejorar la legibilidad, mantenimiento y reutilización.

### 2. Estructura del Proyecto

El proyecto está organizado en varios módulos (`.py` files), cada uno con una responsabilidad específica. Esta estructura ayuda a mantener el código limpio y fácil de entender.

```
.
├── assets/
│   ├── discord.png
│   ├── github.png
│   ├── youtube.png
│   ├── facebook.png
│   └── web.png
├── main.py
├── routes.py
├── views.py
├── menu.py
├── clase_boton.py
└── theme.py
```

### 3. Descripción Detallada de los Módulos Locales

A continuación, se describe cada módulo, su función, cómo fue creado y el motivo de su existencia.

#### 3.1. `main.py` - El Corazón de la Aplicación

* **Función:** Este es el archivo principal que inicia la aplicación Flet. Es el punto de entrada desde donde se carga y se ejecuta todo el proyecto.
* **Cómo fue creado:** Contiene la función `main(page: ft.Page)` que es requerida por Flet para inicializar la aplicación. Dentro de esta función, se configura el título de la ventana y el modo de tema inicial. Lo más importante es que delega la configuración de las rutas al módulo `routes.py`.
* **Motivo de su creación:** Es esencial para cualquier aplicación Flet. Su propósito es centralizar la inicialización y configuración básica de la aplicación, asegurando que todos los componentes se carguen correctamente al inicio. Al delegar la lógica de rutas a `setup_routes`, mantiene el `main.py` limpio y enfocado solo en el arranque.

    * `import flet as ft`: Importa la biblioteca Flet, permitiendo el uso de sus componentes y funcionalidades.
    * `from routes import setup_routes`: Importa la función `setup_routes` del archivo `routes.py`, lo que permite configurar la navegación de la aplicación.
    * `def main(page: ft.Page):`: Define la función principal que Flet ejecuta cuando la aplicación se inicia. El objeto `page` representa la página de la aplicación y permite interactuar con ella (ej., cambiar el título, el tema, añadir controles).
    * `page.title = "Mini curso de Flet"`: Establece el título de la ventana de la aplicación.
    * `page.theme_mode = ft.ThemeMode.SYSTEM`: Configura el tema inicial de la aplicación para que coincida con la configuración del sistema operativo del usuario.
    * `setup_routes(page)`: Llama a la función del módulo `routes.py` para configurar cómo se manejan las diferentes rutas (URLs) de la aplicación. Esto es crucial para la navegación.
    * `ft.app(target=main, assets_dir="assets")`: Inicia la aplicación Flet, indicando que la función `main` es el punto de entrada y que la carpeta `assets` contiene recursos como imágenes.

#### 3.2. `menu.py` - El Menú Interactivo

* **Función:** Este módulo se encarga de crear los menús desplegables de la aplicación, incluyendo opciones para cambiar el tema y enlaces a redes sociales.
* **Cómo fue creado:** Define dos funciones principales: `create_theme_menu` para el submenú de temas y `create_social_media_and_options_menu` que combina este submenú con los botones de redes sociales. Utiliza componentes de Flet como `ft.PopupMenuButton` y `ft.PopupMenuItem`.
* **Motivo de su creación:** La modularización del menú permite que sea fácilmente reutilizable en diferentes vistas (páginas) de la aplicación sin duplicar código. Centraliza la lógica de los menús, facilitando su mantenimiento y expansión futura. Por ejemplo, si se desea añadir una nueva red social, solo se modifica este archivo.

    * `import flet as ft`: Importa Flet para construir los componentes de la interfaz de usuario.
    * `from theme import set_theme_light, set_theme_dark, set_theme_system`: Importa las funciones de cambio de tema del módulo `theme.py`.
    * `from clase_boton import get_social_menu_items`: Importa la función para obtener los elementos del menú de redes sociales del módulo `clase_boton.py`.
    * `def create_theme_menu(page):`: Crea un `PopupMenuButton` para seleccionar el tema de la aplicación (claro, oscuro, sistema). Cada opción tiene un `on_click` que llama a las funciones correspondientes del módulo `theme.py`.
    * `def create_social_media_and_options_menu(page):`: Crea el menú principal que contiene las opciones de redes sociales, el submenú de temas y la opción "Acerca de". Utiliza `get_social_menu_items` para obtener los botones de redes sociales y los añade a la lista de ítems del menú. El botón "Acerca de" utiliza `page.go("/about")` para navegar a la vista de "Acerca de".

#### 3.3. `clase_boton.py` - Botones de Redes Sociales Reutilizables

* **Función:** Proporciona funciones para crear botones de redes sociales de manera estandarizada y obtener una lista de estos botones para el menú.
* **Cómo fue creado:** Contiene la función `social_button` que genera un `ft.PopupMenuItem` con un icono (o una imagen si se proporciona una ruta) y un texto, y una acción `on_click` que lanza la URL de la red social. La función `get_social_menu_items` recopila y devuelve una lista de estos botones predefinidos.
* **Motivo de su creación:** Evita la repetición de código al crear múltiples botones de redes sociales. Al tener una función `social_button`, cada botón se crea de la misma manera, lo que simplifica el proceso y asegura la consistencia en el diseño. La función `get_social_menu_items` centraliza la lista de redes sociales, facilitando la adición o eliminación de enlaces.

    * `import flet as ft`: Necesario para usar los componentes de Flet, como `ft.PopupMenuItem`, `ft.Row`, `ft.Image`, `ft.Icon`, y `ft.Text`.
    * `def social_button(name: str, url: str, icon_path: str = None, page=None):`: Una función auxiliar que crea un `PopupMenuItem` para una red social.
        * `name`: El texto que se mostrará para el botón (ej., "Discord").
        * `url`: La URL a la que se navegará cuando se haga clic en el botón.
        * `icon_path`: La ruta a un archivo de imagen para el icono (ej., "discord.png"). Si no se proporciona, se usa un icono genérico de enlace.
        * `page`: El objeto `page` de Flet, necesario para `page.launch_url(url)` que abre la URL en el navegador por defecto del usuario.
    * `def get_social_menu_items(page):`: Retorna una lista de objetos `PopupMenuItem`, cada uno representando un enlace a una red social. Cada elemento se crea llamando a `social_button` con los detalles específicos de cada red social. También incluye un `ft.PopupMenuItem()` que actúa como un divisor visual en el menú.

#### 3.4. `theme.py` - Gestión de Temas

* **Función:** Este módulo proporciona funciones simples para cambiar el modo de tema de la aplicación (claro, oscuro o sistema).
* **Cómo fue creado:** Contiene tres funciones: `set_theme_light`, `set_theme_dark`, y `set_theme_system`. Cada una toma el objeto `page` de Flet y modifica la propiedad `page.theme_mode` a la configuración deseada, seguido de un `page.update()` para aplicar los cambios visuales.
* **Motivo de su creación:** Centraliza la lógica de cambio de tema, lo que la hace reutilizable y fácil de mantener. En lugar de replicar el código para cambiar el tema en cada lugar donde se necesite, simplemente se llama a la función correspondiente de este módulo.

    * `import flet as ft`: Importa la biblioteca Flet para acceder a las propiedades y métodos de la página.
    * `def set_theme_light(page):`: Establece el tema de la aplicación a `LIGHT`.
    * `def set_theme_dark(page):`: Establece el tema de la aplicación a `DARK`.
    * `def set_theme_system(page):`: Establece el tema de la aplicación a `SYSTEM`, lo que significa que la aplicación adoptará el tema configurado en el sistema operativo del usuario.
    * `page.update()`: Es crucial llamar a este método después de cambiar el `theme_mode` para que los cambios se reflejen visualmente en la interfaz de usuario.

#### 3.5. `routes.py` - Navegación y Rutas

* **Función:** Este módulo gestiona la navegación entre las diferentes vistas (páginas) de la aplicación. Define cómo la aplicación responde a los cambios de ruta y cómo se maneja el historial de navegación.
* **Cómo fue creado:** Contiene la función `setup_routes` que configura dos manejadores de eventos importantes de Flet: `on_route_change` y `on_view_pop`.
    * `route_change`: Esta función se ejecuta cada vez que la ruta de la aplicación cambia (ej., cuando se navega a `/about`). Limpia las vistas existentes y añade la vista `home_view` por defecto, y si la ruta es `/about`, añade la vista `about_view`.
    * `view_pop`: Esta función se activa cuando una vista es "sacada" de la pila (ej., al presionar el botón de retroceso del navegador). Permite volver a la vista anterior.
* **Motivo de su creación:** Permite construir una aplicación de una sola página (SPA - Single Page Application) con Flet. Al centralizar la lógica de ruteo, se asegura una navegación fluida y consistente. Separar esto del `main.py` y las propias vistas mantiene el código más organizado y fácil de depurar.

    * `from views import home_view, about_view`: Importa las funciones que crean las diferentes vistas de la aplicación.
    * `def setup_routes(page):`: Esta función toma el objeto `page` y configura los manejadores de eventos de ruta.
        * `def route_change(route):`: Esta función se ejecuta cuando la ruta de la página cambia.
            * `page.views.clear()`: Elimina todas las vistas actuales de la pila de vistas de la página. Esto es importante para asegurar que solo se muestren las vistas correctas para la ruta actual.
            * `page.views.append(home_view(page))`: Siempre añade la vista principal (`home_view`) como la primera vista.
            * `if page.route == "/about": page.views.append(about_view(page))`: Si la ruta actual es `/about`, añade la vista "Acerca de" a la pila.
            * `page.update()`: Actualiza la interfaz de usuario para mostrar las vistas recién añadidas.
        * `def view_pop(view):`: Esta función se ejecuta cuando una vista es retirada de la pila (por ejemplo, al usar el botón de retroceso del navegador).
            * `page.views.pop()`: Elimina la vista superior de la pila.
            * `top_view = page.views[-1]`: Obtiene la vista que ahora está en la parte superior de la pila.
            * `page.go(top_view.route)`: Navega a la ruta de la vista que ahora está en la parte superior, lo que actualiza la URL en el navegador y la interfaz de usuario.
        * `page.on_route_change = route_change`: Asigna la función `route_change` para que se ejecute cuando la ruta de la página cambie.
        * `page.on_view_pop = view_pop`: Asigna la función `view_pop` para que se ejecute cuando una vista sea retirada de la pila.
        * `page.go(page.route)`: Llama a `page.go()` con la ruta actual de la página. Esto es importante al inicio de la aplicación para asegurarse de que la vista correcta se cargue inicialmente basándose en la URL actual.

#### 3.6. `views.py` - Las Vistas de la Aplicación

* **Función:** Este módulo contiene las definiciones de las diferentes "páginas" o "vistas" de la aplicación, como la página de inicio (`home_view`) y la página "Acerca de" (`about_view`).
* **Cómo fue creado:** Cada función (`home_view` y `about_view`) retorna un objeto `ft.View`. Dentro de cada `ft.View`, se define la estructura visual de la página utilizando componentes de Flet como `ft.AppBar`, `ft.Container`, `ft.Column`, `ft.Text`, `ft.Divider`, y `ft.ElevatedButton`.
* **Motivo de su creación:** Separa la lógica de la interfaz de usuario de las vistas del resto de la aplicación. Esto hace que sea fácil añadir nuevas vistas, modificar las existentes y comprender cómo se presenta cada "página" al usuario. Cada vista es autónoma en su diseño.

    * `import flet as ft`: Importa la biblioteca Flet para crear componentes de interfaz de usuario.
    * `from menu import create_social_media_and_options_menu`: Importa la función para crear el menú, lo que permite incluir el menú en el `AppBar` de cada vista.
    * `def home_view(page):`: Define la vista de la página de inicio.
        * Retorna un `ft.View` con la ruta `"/"`.
        * Incluye un `ft.AppBar` (la barra superior de la aplicación) con un título y las acciones del menú (creadas por `create_social_media_and_options_menu`).
        * El contenido principal de la vista se organiza en un `ft.Container` con un `ft.Column` para organizar el texto y un botón.
        * El `ElevatedButton` "Ver ejemplo de rutas" tiene un `on_click` que usa `page.go("/about")` para navegar a la vista "Acerca de".
    * `def about_view(page):`: Define la vista de la página "Acerca de".
        * Retorna un `ft.View` con la ruta `"/about"`.
        * También incluye un `ft.AppBar` similar al de la vista de inicio.
        * El contenido principal es un `ft.Container` con un `ft.Column` que muestra información sobre el curso y el desarrollador.
        * El `ElevatedButton` "Volver al Inicio" utiliza `page.go("/")` para navegar de vuelta a la vista principal.
    * `bgcolor=page.bgcolor`: En ambas vistas, se establece el color de fondo de la vista para que coincida con el color de fondo de la página, lo que ayuda a una transición de tema más suave.

### 4. Flujo de Ejecución de la Aplicación

1.  **Inicio (`main.py`):** La aplicación se inicia ejecutando `main.py`. La función `main` se llama, configurando el título y el tema de la página.
2.  **Configuración de Rutas (`routes.py`):** `main.py` llama a `setup_routes(page)`. Este módulo configura los manejadores para los cambios de ruta y los eventos de `view_pop`. También fuerza una navegación inicial a la ruta actual (`page.go(page.route)`) para que se cargue la vista correcta al inicio.
3.  **Carga de Vistas (`views.py`):** Cuando la ruta cambia (incluida la carga inicial), la función `route_change` en `routes.py` se activa. Esta función determina qué vistas deben mostrarse (ej., `home_view` para `/`, `about_view` para `/about`) y las añade a la pila de vistas de la página.
4.  **Construcción de Vistas:** Las funciones `home_view` y `about_view` en `views.py` construyen la interfaz de usuario para cada página. Esto incluye la creación de `AppBar`s y el uso del menú.
5.  **Creación de Menús (`menu.py`):** Al construir las `AppBar`s, se llama a `create_social_media_and_options_menu` desde `menu.py`.
6.  **Botones de Redes Sociales (`clase_boton.py`):** El módulo `menu.py` a su vez utiliza `get_social_menu_items` de `clase_boton.py` para generar los botones de redes sociales de forma estandarizada.
7.  **Cambio de Tema (`theme.py`):** Desde el menú, cuando el usuario selecciona una opción de tema, las funciones de `theme.py` (ej., `set_theme_light`) son llamadas para cambiar el modo de tema de la aplicación y actualizar la interfaz.
8.  **Navegación:** Cuando un usuario hace clic en un `ElevatedButton` que navega a otra ruta (ej., "Ver ejemplo de rutas" que lleva a `/about`), `page.go()` se llama, lo que dispara el evento `on_route_change` y el ciclo se repite, cargando la nueva vista.

### 5. Conceptos Clave para Aprender

* **Modularización:** La división del código en archivos más pequeños y lógicos.
    * **Beneficios:** Mayor legibilidad, facilidad de mantenimiento, reutilización de código y colaboración en proyectos grandes.
* **Flet Page Object (`ft.Page`):** Es el objeto central que representa la ventana de la aplicación. Permite manipular el título, el tema, añadir y gestionar vistas, y manejar eventos de la página.
* **Vistas (`ft.View`):** Representan "páginas" o "pantallas" dentro de una aplicación de una sola página (SPA). Flet gestiona una pila de vistas, permitiendo la navegación hacia adelante y hacia atrás.
* **Rutas (`page.route` y `page.go()`):** Flet permite la navegación entre vistas usando un sistema de rutas similar al de las aplicaciones web.
    * `page.route`: La URL o ruta actual de la aplicación.
    * `page.go(ruta)`: Método para navegar a una nueva ruta.
    * `page.on_route_change`: Un manejador de eventos que se activa cuando la ruta de la página cambia.
    * `page.on_view_pop`: Un manejador de eventos que se activa cuando una vista es "sacada" de la pila (ej., al regresar en el historial).
* **Componentes de Flet:**
    * `ft.AppBar`: La barra de aplicación en la parte superior de una vista.
    * `ft.PopupMenuButton`: Un botón que muestra un menú desplegable cuando se hace clic.
    * `ft.PopupMenuItem`: Un elemento individual dentro de un `PopupMenuButton`.
    * `ft.Text`: Para mostrar texto.
    * `ft.Icon`: Para mostrar iconos de Material Design.
    * `ft.Image`: Para mostrar imágenes personalizadas.
    * `ft.Row` / `ft.Column`: Contenedores para organizar otros controles horizontal o verticalmente.
    * `ft.Container`: Un control flexible para agrupar y aplicar estilos a otros controles.
    * `ft.ElevatedButton`: Un botón con un efecto de elevación, comúnmente usado para acciones principales.
    * `ft.Divider`: Una línea divisoria horizontal.
* **Gestión de Eventos (`on_click`, `on_route_change`, etc.):** Flet utiliza funciones de devolución de llamada (callbacks) para responder a las interacciones del usuario o a los cambios en el estado de la aplicación.

### 6. Cómo Aprender y Experimentar

1.  **Ejecuta el Proyecto:** Asegúrate de tener Flet instalado (`pip install flet`) y ejecuta el `main.py` para ver la aplicación en acción.
2.  **Explora el Código:** Abre cada archivo (`.py`) en tu editor de código y lee el código línea por línea, comparándolo con las explicaciones de este manual.
3.  **Realiza Cambios Pequeños:**
    * **Cambia el texto:** Modifica los textos en `views.py` para ver cómo afecta la interfaz.
    * **Añade una red social:** En `clase_boton.py`, descomenta una de las líneas de ejemplo (`social_button("Instagram", ...)`) y observa cómo aparece un nuevo botón en el menú.
    * **Cambia un icono:** Reemplaza la ruta de una imagen en `clase_boton.py` o prueba a no pasar `icon_path` para ver el icono por defecto.
    * **Añade una nueva vista:** Intenta crear una nueva función de vista en `views.py` y luego configúrala en `routes.py` para que sea accesible a través de una nueva ruta.
4.  **Depura:** Utiliza las herramientas de depuración de tu editor (como Visual Studio Code) para seguir el flujo de ejecución del código, especialmente en `routes.py` para entender cómo se manejan los cambios de ruta.
5.  **Consulta la Documentación de Flet:** La documentación oficial de Flet es un recurso excelente para profundizar en cualquier componente o concepto.

Este manual debería proporcionarte una base sólida para entender el proyecto "Mini curso de Flet" y ayudarte a aprender los fundamentos de la creación de aplicaciones con Flet de manera modular.

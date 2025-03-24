"""Un web framework es un conjunto de herramientas y librerías que facilitan la creación de aplicaciones web. Básicamente, te ahorra trabajo al proporcionar 
estructuras y funciones ya listas para manejar tareas comunes, como: gestionar rutas (URLs), procesar formularios, conectar con bases de datos, manejar sesiones 
y autenticación, renderizar páginas HTML dinámicas. Con python hay varias frameworks que serían:

- Flask: Flask es un framework minimalista que te permite construir aplicaciones web sin muchas restricciones. Es ideal para proyectos pequeños y medianos, 
donde quieres tener control total sobre cada detalle. Flask se suele usar para proyectos pequeños o prototipos rápidos, APIs REST (para comunicar aplicaciones entre sí) o
cuando necesitas algo simple sin mucha configuración.

- Django: Django es un framework más grande que te da todo listo para desarrollar aplicaciones web completas. Es ideal para proyectos grandes y escalables. Es ideal
con aplicaciones web grandes con bases de datos, proyectos donde necesitas seguridad y estructura o cuando quieres desarrollar rápido sin preocuparte por configurar todo.

- Justpy: JustPy es un framework moderno que permite crear aplicaciones web sin escribir HTML, CSS o JavaScript. Todo se hace en Python, incluso la interfaz de usuario. Se
usa cuando quieres construir interfaces sin tocar HTML/CSS, aplicaciones web interactivas con datos en tiempo real, dashboards o herramientas internas en empresas.

Para empezar a trabajar con Django lo primero que tenemos que responder es si es posible (por ejemplo si queremos hacer un traductor, preguntarnos si se puede traducir
idiomas con python). Si la respuesta es si, pasamos al siguiente punto que sería crear una app vacia de django y a partir de ahi empezar a trabajar. Luego los pasos
para crear la app sería en este orden: crear el html, configurar las urls, crear las views, crear los models y conectar la parte que procesa que en nuestro ejemplo
sería el traductor.

Nosotros vamos a trabajar con django y tenemos que crear un venv. Se crea poniendo en la terminal -m venv env (o virtual o como queramos que se llame la carpeta) y luego 
para trabajar dentro se crearán las carpetas del venv y tenemos que poner env/Scripts/activate y ya se activará. Para salir hay que poner deactivate Para elegir que
virtual studio code trabaje con el venv, pulsamos ctrl+shift+p y seleccionamos python interpreter y elegimos la venv que acabamos de crear. podemos ver que estamos en el 
venv en la parte de abajo a la dcha del virtual studio code. Dentro de la carpeta env es recomendable no meter archivos ni tocar nada. Si cerramos y abrimos el proyecto,
tenemos que abrir una terminal nueva.

Ponemos en la terminal con el venv "django-admin startproject mysite(o el nombre que queramos) y un punto ." con esto crearemos una carpeta en nuestra carpeta que se llamará
mysite en este caso. Dentro podemos ver por ejemplo el archivo settings con la configuración y demás. Si ponemos en la terminal "python manage.py runserver" nos saldrá la web
diciendo que django está instalado y que todo está ok. Despues pondremos "python manage.py migrate" tal y como nos sale en la terminal. Con esto creara una db 
con tablas predeterminadas con sqlite3 que se alojará en la carpeta.

Si vamos a la web y ponemos /admin veremos que se abre una nueva página que nos pide username y password. Ahora vamos a crear un admin user. AL crear un proyecto en
django se van a crear muchos archivos. Para crear el admin ponemos en la terminal python manage.py createsuperuser y seguimos los pasos. Una vez hecho esto lanzamos
el runserver y ponemos /admin en la web e introducimos el user y el password. Dentro veremos Groups y Users por si queremos crear otro usuario.

Ahora ponemos en la terminal python manage.py startapp blog(es el nombre de la app podemos darle el que queramos). Se creará una carpeta llamada blog en nuestra
carpeta principal. Habrá varios archivos dentro como apps, models, tests o views... Cuando trabajas con Django, sigues un patrón llamado MVC (Modelo-Vista-Controlador), 
aunque en Django se le llama MTV (Model-Template-View). Para entenderlo de manera sencilla:

Models (Modelos) → La Base de Datos - Los models representan la estructura de la base de datos. Son clases de Python que Django convierte en tablas en la base de datos.
Views (Vistas) → La Lógica de la Aplicación - Las views procesan las solicitudes del usuario y envían una respuesta.
Tests (Pruebas) → Asegurar que Todo Funciona - Los tests sirven para verificar que nuestra aplicación funciona correctamente antes de subirla a producción.

Ahora tenemos que ir dentro de la carpeta mysite al archivo settings y modificar donde pon INSTALLED APPS añadiendo nuestra carpeta blog con comillas'blog' 
añadiéndolo justo debajo con una coma al final.
Dentro del archivo models.py y lo modificamos(explicacion dentro). Tras crear nuestro model "post" ahora vamos a crear las html templates y para ello creamos primero
una carpeta que se llame templates dentro de nuestra carpeta principal y creamos un archivo llamado blog.html. Ahora creamos las views para crear un view (explicacion dentro).
Para ello primero tenemos que crear un archivo py dentro de la carpeta blog que se llame urls.py (ir alli para ver explicacion)

Una vez creado todo esto vamos a subirlo a la web. Como ahora mismo en el perfil de admin sólo nos deja añadir otros usuarios o grupos, vamos al archivo admin.py dentro
de la carpeta blog y añadimos el model que hemos creado alli (explicacion dentro) Una vez creado ya podemos añadir los posts.

Ahora vamos a crear una homepage. Hacemos una nueva página index.html dentro de templates y luego vamos a urls para crear una nueva urls y despues a view para crear
el nuevo model y unirlo. Ahora vamos a crear una nueva página html llamada about.html. Con about html cambiamos el nombre de index y modificamos model, url y view y luego
creamos la nueva página index y hacemos que haya hipervinculos para las palabras Dogs y Cats en la homepage modificando el html de index.

Ahora vamos a añadir bootstrap a django. Bootstrap es un framework de CSS que te ayuda a diseñar páginas web de forma rápida y fácil, tiene un diseño moderno y 
responsivo (se adapta a móviles y pantallas grandes), incluye botones, formularios, menús y otros elementos listos para usar y no necesitas escribir mucho CSS, 
solo usar sus clases. Para instalar bootstrap podemos ir a su web directamente y seguir los pasos sin instalar nada, o instalarlo. Basicamente seguimos las
instrucciones de la web y añadimos los códigos a la index.html. Es parecido a CSS. En la web encontramos un monton de plantillas para añadir a los html con 
form, componentes, layouts... entonces usando palabras clave como container o card, directamente cogerá el modelo CSS ya creado de la web y lo aplicará. Vamos 
modelando la web con estos detalles para ponerla como queramos.

Para los cambios que queramos hacer en la web con django (como por ejemplo que aparezcan solo 500 caracteres del blog) podemos buscar en google django templates filter
y veremos una lista de filtros que podemos aplicar a las templates.

Ahora vamos a crear una barra de navegación para que el usuario de la web pueda ir de una página a otra. Se puede hacer poniendo el código html en todas las paginas
o sino se puede hacer con una template inheritance. Para ello creamos la página base.html y luego modificamos el código de todas las páginas para que aparezca la
la navigation bar. Luego le damos estilo a la barra de navegación con bootstrap. 

Ahora vamos a crear una nueva app que nos permita traducir texto. Lo primero es crear una nueva app tal y como hicimos con blog siguiendo los mismos pasos. Luego 
creamos la pagina html translator y añadimos el código. Tras eso configuraremos las url creando un nuevo archivo urls.py dentro de la carpeta translator y copiando
y modificando el codigo de urls.py de la carpeta mysite. Tras eso vamos a crear el form dentro de views de la carpeta translator.

Para terminar vamos a instalar google translator y lo haremos abriendo una nueva terminal y poniendo pip install googletrans (si queremos alguna version en 
concreto ponemos == y la version que sea.)
"""


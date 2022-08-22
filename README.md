# Spotify Playlist para Coderhouse

Este proyecto es el trabajo integrador final del Curso de Python que se brindó en la plataforma de Coderhouse. El mismo integra todos los conocimientos adquiridos durante el journey del curso.

## Idea del Proyecto 💡
La idea del Proyecto es recolectar toda la información de las canciones y de todas las listas de reproducción del usuario, en este caso, de mi cuenta de Spotify. Luego de recolectar toda esa metadata, verificar cuál es el genero que mas abunda dentro de todas las listas de Reproducción que tengo. Posteriormente almacenar todos los datos recolectados a un Bucket de S3 y a una base de datos PostgreSQL.

**Hipotesis:**
Se asume que el género que más abunda en mi Spotify es el Rock alternativo y el Hip Hop.

**Resultado comprobación de Hipotesis: NEGATIVO.** El genero que más abunda en mis playlist es "Trap Latino".

**Resultado del Proyecto:**


| Genre |         Cant|


|trap latino |       184|
| ----- | ---- |
|cumbia villera |     97|
| ----- | ---- |
|rock   |             89|
| ----- | ---- |
|permanent wave |     87|
| ----- | ---- |
|spanish hip hop |    86|



## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

Para que el programa pueda funcionar correctamente se necesita instalar poetry en su máquina local, junto con Python, y PostgreSQL

* [Instalación de Poetry](https://python-poetry.org/docs/)
* [Documentación Poetry](https://python-poetry.org/docs/basic-usage/)

## Configuración 📌

Se deberán configurar las KEYS de accesso para todos los serivios que se utilizarán. Dicha configuración se deberá realizar sobre el archivo **secrets_key.json**.

Para obtener las credenciales de Spotify, es necesario registrarse como desarrollador y crear algún proyecto de prueba
[Dashboard Spotify Developer](https://developer.spotify.com/dashboard/applications)

Además se deberá configurar, dentro del script principal, el ID del usuario dentro de Spotify:
_SPOTIFY_USER_ID = <TU_USER_ID> (por ejemplo: **noel.argonzalez** que es el mio)


## ADVERTENCIA 📢
El proyecto completo tarda en ejecutarse completo alrededor de 30 minutos, dependiendo de la cantidad de playlist que el usuario tenga AGREGADOS A SU PERFIL (Para agregar alguno en los tres puntitos y click en agregar al perfil).

Para este caso de ejemplo, solamente se trabaja con un playlist predefinida para que el proyecto no demore tanto su ejecución y tarde menos de 1 minuto.

Para ejecutar el proyecto completo, se deberá comentar la variable que contiene una lista(playlist_ids) dentro de la función **getFeaturesSongForPlaylist()** que se encuentra aproximadamente en la linea 146 del código principal.

### Instalación 🔧

**Clonar el repositorio:** 
```
git clone https://github.com/noelgz/coderhouse_spotify.git
```

**Ingresar al proyecto:**
```
cd coderhouse_spotify/
```

Para poder instalar las dependencias del Proyecto situadas en pyproject.toml:

_Se debe situarse dentro de la carpeta del proyecto y ejecutar lo siguiente:

**Instalación de las dependencias:**

```
poetry install
```

**Activar entorno Virtual:**
```
poetry shell
```

## Despliegue 📦

Una vez que se encuentre dentro del entorno virtual de poetry solamente resta ejecutar:

```
python spotipy_proyect_coder.py
```

## Construido con 🛠️

Las herramientas que se utilizaron en el proyecto son:

* [Poetry](https://python-poetry.org/) - Para gestionar las librerías y sus dependencias
* [Spotipy](https://spotipy.readthedocs.io/en/master/) - Librería para hacer las conexión con Spotify y consumir datos


## Mejoras futuras 📖

Como mejoras futuras para estre proyecto propongo:
* Mejorar el tiempo de ejecución del proyecto completo.
* Hacer una refactorización mejoradas ya que existen diferentes aspectos que pueden ser mejorados.

## Autores ✒️

* **Noel Gonzalez** - *Trabajo Final* - [Noel Gonzalez](https://github.com/noelgz)


## Expresiones de Gratitud 🎁

* Gracias a NX por permitirme realizar este curso
* Invitamos una cerveza 🍺 o un café ☕ a todo el equipo de Coder que estuvo día a día agregandome conocimiento. 
* Gracias totales.



---
⌨️ Por [Noel Gonzalez](https://github.com/noelgz) 😊

# Spotify Playlist para Coderhouse

Este proyecto es el trabajo integrador final del Curso de Python que se brindó en la plataforma de Coderhouse. El mismo integra todos los conocimientos adquiridos durante el journey del curso.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

Para que el programa pueda funcionar correctamente se necesita instalar poetry en su máquina local, junto con Python, y PostgreSQL

[Instalación de Poetry](https://python-poetry.org/docs/)
[Documentación Poetry](https://python-poetry.org/docs/basic-usage/)

## Configuración 📌

Se deberán configurar las KEYS de accesso para todos los serivios que se utilizarán. Dicha configuración se deberá realizar sobre el archivo **secrets_key.json**.

Para obtener las credenciales de Spotify, es necesario registrarse como desarrollador y crear algún proyecto de prueba
[Dashboard Spotify Developer](https://developer.spotify.com/dashboard/applications)


## ADVERTENCIA 📢
El proyecto completo tarda en ejecutarse completo alrededor de 30 minutos, dependiendo de la cantidad de playlist que el usuario tenga AGREGADOS A SU PERFIL (Para agregar alguno en los tres puntitos y click en agregar al perfil).

Para este caso de ejemplo, solamente se trabaja con un playlist predefinida para que el proyecto no demore tanto su ejecución y tarde menos de 1 minuto.

Para ejecutar el proyecto completo, se deberá comentar la variable que contiene una lista(playlist_ids) dentro de la función **getFeaturesSongForPlaylist()** que se encuentra aproximadamente en la linea 146 del código principal.

### Instalación 🔧

Para poder instalar las dependencias del Proyecto situadas en pyproject.toml:

_Se debe situarse dentro de la carpeta del proyecto y ejecutar lo siguiente:

```
Instalación de las dependencias -> poetry install
Para activar el entorno virtual -> poetry shell
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
⌨️ con ❤️ por [Noel Gonzalez](https://github.com/noelgz) 😊

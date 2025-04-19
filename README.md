# Websocket-connection-using-Django-channels
Django Channels example demonstrating WebSocket connection and disconnection handling for real-time applications.

## Overview

**Perfect for beginners looking to understand WebSocket lifecycle events in Django.**

This repository demonstrates how to handle WebSocket connections and disconnections using Django Channels. It provides a minimal setup to track when clients connect or disconnect, which is useful for building real-time features like chat apps, notifications, or live updates.

## **Features include:**
- Establishing WebSocket connections
- Detecting client disconnections
- Basic routing and consumer setup with Django Channels
  
 ## **Language/Framework:**
Python | Django | Django Channels (WebSocket handling) | Daphne server

## Install dependencies
Execute the following commands

```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt

```

Update the settings.py file with the following details:
```
INSTALLED_APPS = [
    ...
    'channels',
    'websocket_app',
]
```
configuring ASGI

```
ASGI_APPLICATION = "websocket_project.asgi.application"
```
Run daphne
```
daphne -b 0.0.0.0 -p 8001 websocket_project.asgi:application
```
-b 0.0.0.0 binds Daphne to all network interfaces.

-p 8001 sets the port.

websocket_project.asgi:application points to your ASGI application.

## Project Workflow
**The server side:**

-It is the Django project with Channels installed and configured.

-Uses ASGI (Asynchronous Server Gateway Interface), enabling asynchronous protocols like WebSockets.

-Runs on an ASGI server (such as Daphne), which listens for WebSocket requests and routes them to your consumers via the routing configuration.

-The consumer file is part of your Django backend and is executed on the server.

**The client side:**

-It is the HTML/JavaScript code (websocket_status.html) running in the browser.

-Initiates the WebSocket connection to the server using the WebSocket API.

## Project structure

**consumers.py:**

A WebSocket consumer in Django Channels is a specialized class responsible for managing WebSocket connections and handling real-time, bidirectional communication between the client and server. Its main functions include establishing connections, handling disconnections, and sending and receiving messages.

**Routing.py**

It directs incoming connections to the appropriate consumer based on connection metadata, primarily the connection’s URL path and protocol type.

**websocket_status.html**

The HTML and JavaScript code (websocket_status.html) acts as the WebSocket client. JavaScript code running in the browser creates a WebSocket object which opens a WebSocket connection from the client (browser) to the server. 

The client listens for events (onopen, onmessage, onclose, onerror) and sends messages to the server using socket.send(). 

The HTML provides the interface for the user to interact with the client-side code (e.g., typing messages, clicking buttons).

**Asgi.py**

The asgi.py file in a Django project serves as the entry point for ASGI-compatible servers (such as Daphne) to interface with the Django application. It sets up the ASGI application instance that the server will use to communicate with Django. 

**Project-level urls.py**

Maps root-level URLs and includes URL patterns from each app's urls.py using the include() function. This keeps the main URL configuration organized and allows for a scalable project structure.

**App-level urls.py**

Defines URL patterns that map to view functions or classes within the app. This allows each app to manage its URLs independently, making the app reusable and modular.

**views.py**

View function or class takes an HTTP request object as input (usually called request) and returns an HTTP response.

**websocket_status.html**

The function of websocket_status.html is to serve as the client-side interface for establishing and managing a real-time WebSocket connection with the Django Channels server.
   



  

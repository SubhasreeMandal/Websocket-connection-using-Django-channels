from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="CONNECTION_ESTABLISHED")

    async def disconnect(self, close_code):
        print(f"WebSocket connection closed. Close code: {close_code}")
        await self.send(text_data="Websocket Connection closed")

    async def receive(self, text_data):
        await self.send(text_data=f"Server: {text_data}")

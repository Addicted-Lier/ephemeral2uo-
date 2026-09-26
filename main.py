from fastapi import FastAPI,WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Ephemeral Chat</title>
</head>

<body>
    <h1>Ephemeral Chat 🔐</h1>

    <input id="messageText" type="text" placeholder="Type a message">
    <button onclick="sendMessage()">Send</button>

    <ul id="messages"></ul>

    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");

        ws.onmessage = function(event) {
            const message = document.createElement("li");
            message.textContent = event.data;
            document.getElementById("messages").appendChild(message);
        };

        function sendMessage() {
            const input = document.getElementById("messageText");

            ws.send(input.value);

            input.value = "";
        }
    </script>
</body>
</html>
"""
@app.get("/")
async def home():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        await websocket.send_text(message)
```python
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from robka import Robot
from robka.context import Message

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()

def keep_alive():
    t = threading.Thread(target=run_server)
    t.daemon = True
    t.start()

def main():
    keep_alive()
    bot = Robot(token=os.environ.get("BOT_TOKEN"))

    @bot.on_message(commands=["start"])
    def start(bot: Robot, message: Message):
        message.reply("سلام دادا! بالاخره بات روبیکا روی سرور کار کرد 🎉")

    bot.run()

if __name__ == "__main__":
    main()
```
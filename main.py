from pyrogram import Client, filters
import time

app = Client("ghdonor", api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e")
 
Gruppo = chat id da dove rubare i mex 
Canale = canale dove inoltrarli, il voip deve essere admin del canale
    
@app.on_message(filters.chat(Gruppo) & filters.text)
async def messaggi(client, message):
    time.sleep(1.5)
    await app.send_message(Canale, f"__padrone, nuovo mex in gruppas!__\n\nda: {message.from_user.first_name}\n`{message.from_user.id}`\n\n{message.text}", disable_web_page_preview=True)
                              
app.run()


import asyncio
from telethon.tl import functions, types
from telethon.sync import TelegramClient ,events 
from telethon.sessions import StringSession
api_id = 4091096
api_hash = '6bb0682b4af56456201c3b9d8b99c94a'
bot_token = '2025919134:AAEtaYWwSrYcIQsK7-1zn5aA581bb0hDJNc'
STRING_SESSION = "1BVtsOK0BuyOrsOmanqjqtRki98zGYMZtJE0CoaDRuBmlbw-bGzviSFhA3KhgMnKtUxyr9EDwgswl2ddFqptdD0NbBKRLCspOw9sJFtaIpj6A1XpCcC4d1cgddpROD4zXO2oYUwycDU2qvmyeyetRMwfo6J7-mCji1x66qQX_FWKQ5gkKv1ZY7W0XIf-0jpvJU60e2pGA_pY398QKmGdyK_soCsLVbclgs7QgJPw67-T4ManKid3qGCNUw3BHM8elvebCEBlHdt7IuJy2UmQx2hjStKZpuD0bAarI28yDCV6R1z33VTbJFmVTf-rSG5Ct33uNkva7SDyXnkQo3zcnagdjeWlu30A="
# We have to manually call "start" if we want an explicit bot token
tbot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
ubot = TelegramClient(StringSession(STRING_SESSION), api_id, api_hash)


@tbot.on(events.NewMessage(pattern="^/cc (.*)"))
async def alive(event):
  m = await event.reply("Generating CC...Pls Weit.")
  ok = event.pattern_match.group(1)
   async with ubot.conversation("@ccgen_robot") as bot_conv:
       await bot_conv.send_message("/generate")
       await bot_conv.send_message("💳Credit Card Generator💳")
       await asyncio.sleep(2)
       await bot_conv.send_message(ok)
       await asyncio.sleep(1)
       response = await bot_conv.get_response()
       await asyncio.sleep(1)
       await response.click(text="✅Generate✅")
       await asyncio.sleep(2)
       text = "****Generated Cards:****\n"
       gen = await bot_conv.get_response()
       card = gen.text
       text = f"{card.splitlines()[0]}\n"
       text += f"{card.splitlines()[1]}\n"
       text += f"{card.splitlines()[2]}\n"
       text += f"{card.splitlines()[3]}\n"
       text += f"{card.splitlines()[4]}\n"
       text += f"{card.splitlines()[5]}\n"
       text += f"\nGenerated By: ****"
       await m.edit(text)












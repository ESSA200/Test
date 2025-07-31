from pyrogram import Client, idle
from pyromod import listen

OWNER_ID = int(f"1457243602")
ch = "qqqqa1" 
OWNER_USERNAME = "A_W_X_3"
ST = "A_W_X_3"
LT = "A_W_X_3"
DEVS = [6964266670]
DEVS.append(OWNER_USERNAME)
DEVS.append(ST)
DEVS.append(LT)
OWNER = "ESSA"

bot_token="7927108247:AAEz9rTVQ8LzX7DkObZNQgGF04htYryjXKE"
bot_token2="1ApWapzMAUCdWTXLhR4O1v6DMhuUFY2xxb2Un2GEW9gdixASJrkQY9Lf4J4JQQ4LZsTnA0CvilnAk5DOBW-3XHo5sNIhACS3Xz62QsLsU2S8Dct9S6KcYjm5FjSkZskhyT1hhhKgSM2bzuJ5__slKScp2T4DYQ22HVeCs2hkMf0PcUC5lhS9fo-26aBiNf0QbEPecHpRelGkwtN4EJEZcfTeqLodso1a4C-85EB9b2uIFOIVvO4JjAiL3a9nPQDHygFCf6Awx0wvYpLJ0pbTSpq0Q_9r1Ej5KxaX7MviUs9d_NIRXGDAB_llxvO_QpAk8lBWaMmSjRaFaAzyLkpnVP_pT0ODXrA8="


bot = Client("ITA", api_id=29183372, api_hash="b89f3720fcfd80209cc917e415852781", bot_token=bot_token, plugins=dict(root="CASER"))
lolo = Client("hossam", api_id=29183372, api_hash="b89f3720fcfd80209cc917e415852781", session_string=bot_token2)    

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(OWNER_USERNAME, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()

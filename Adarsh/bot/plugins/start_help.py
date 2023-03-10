#Aadhi000 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      

buttonz=ReplyKeyboardMarkup(
            [
                ["start","help"],
                ["about","ping"],
                ["status"]        
            ],
            resize_keyboard=True
        )

START_TEXT = """
Hey {} ๐\n
<code>I am Telegram File To Link Bot</code>\n
<code>Use Help Command to Know how to Use me</code>\n
<code>By @NkBots</code>\n
**Maintained By @Tellybotzz**"""

HELP_TEXT = """
โฎ Send Me Any File or Media\n
โฎ I Will Provide You Instant Direct Download link as Well as Stream Link\n
โฎ Add me in Your Channel as Admin To Get Direct Download link button and online Stream Link Button\n
"""


ABOUT_TEXT = """
๐ค My Name : Telly File Stream Bot\n
๐ฆ Version : <a href='https://telegram.me/Nkbots'>3.0</a>\n
๐ซ Source Code : <a href='https://t.me/tellybots_digital'>Click Here</a>\n
๐๏ธ Library : <a href='https://pyrogram.org'>Click Here</a>\n
๐ฒ Developer : <a href='https://telegram.me/Nkbots'>NkBots</a>\n
๐ฆ Last Updated : <a href='https://telegram.me/Nkbots'>[ 13-mar-23 ] 09:00 AM</a>"""

TEXT = """Just Send Me Any Telegram Media To Get Started\n\nOr Use Below Buttons to Interact With Me"""


INFO_TEXT = """
 ๐ซ Telegram Information

 ๐คน First Name : <b>{}</b>

 ๐ดโโ๏ธ Second Name : <b>{}</b>

 ๐ง๐ปโ๐ Username : <b>@{}</b>

 ๐ Telegram Id : <code>{}</code>

 ๐ Profile Link : <b>{}</b>

 ๐ก Dc : <b>{}</b>

 ๐ Language : <b>{}</b>

 ๐ฒ Status : <b>{}</b>
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ท Help', callback_data='help'),
        InlineKeyboardButton('๐? About', callback_data='about')
        ],[
        InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
)
             

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ก Home', callback_data='home'),
        InlineKeyboardButton('๐? About', callback_data='about')
        ],[
        InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
)
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('๐ก Home', callback_data='home'),
        InlineKeyboardButton('๐ท Help', callback_data='help')
        ],[
        InlineKeyboardButton('๐ Close', callback_data='close')
        ]]
)
 

@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**สแดแด แดสแด สแดษดษดแดแด../**",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**แดแดษชษด แดส แดแดแดแดแดแดs แดสแดษดษดแดส แดแด แดsแด  แดแด..**\n\n**แดแดแด แดแด แดแด?แดสสแดแดแด แดษดสส แดสแดษดษดแดส sแดสsแดสษชสแดสs แดแดษด แดsแด แดแด..!\n\nJoin @Nkbots, @Tellybotzz**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๐น๐พ๐ธ๐ฝ ๐๐ฟ๐ณ๐ฐ๐๐ด๐ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    )
                    
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join My Update Channel or Try Again Join @Nkbots and @Tellybotzz**",
                    
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            
            text=START_TEXT.format(m.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
            
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**You are Banned**",
                        
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Join My Update Channel to Use me.**\n\n**Due to Overload Only Channel Subscribers can use me ..!\n\nJoin @NkBots and @Tellybotzz**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("แดแดษชษด แดส แดแดแดแดแดแดs แดสแดษดษดแดส", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    )
                    
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**๐ฐ๐ณ๐ณ ๐ต๐พ๐๐ฒ๐ด ๐๐๐ฑ ๐๐พ ๐ฐ๐ฝ๐ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป**",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))
        msg_text = "Your Link Generated ๐ฉ\n\n๐๏ธ File Name : <code>{}</code>\n\n๐ File Size : <code>{}</code>\n\n๐ฅ Download Link : <code>{}</code>\n\n๐ฅ Watch Online : <code>{}</code>"

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        
        await m.reply_photo(
            photo="https://telegra.ph/file/565f1e1b578ed4e682b7f.jpg",
            caption=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("๐ฉ Download link", url=stream_link)]])
        )



        

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()
 
 #Recoded By Tellybots

@StreamBot.on_message((filters.command("about")) & filters.private)
async def about(bot, update):

    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    ) 
@StreamBot.on_message((filters.command("help")) & filters.private)
async def help(bot, update):

    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )

@StreamBot.on_message(filters.private & filters.command("info"))
async def info_handler(bot, update):


    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"

  
    await update.reply_text(  
        text=INFO_TEXT.format(update.from_user.first_name, last_name, update.from_user.username, update.from_user.id, update.from_user.mention, update.from_user.dc_id, update.from_user.language_code, update.from_user.status),             
        disable_web_page_preview=True
    )

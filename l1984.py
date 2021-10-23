import discord
from tkinter import *
from PIL import Image, ImageDraw, ImageFont

TOKEN = 'OTAxMTAwMjk0MzUwNDU0ODc1.YXK9Cw.TSDYqiqQtMNt0IwKy0RLv1z6Cgg'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} 1984')
    global cd, filename, fontcd, fmat
    cd = "\\Users\\HUSSA\Documents\\School\\Programming\\bot\\"
    filename = cd + "im1984.jpg"
    fontcd = cd + "arial.ttf"
    fmat = filename.split(".")[-1]
    
@client.event
async def on_message(message):
    if not client.user.mentioned_in(message):
        return
    if message.author.id == client.user.id: 
        return
    try:
        x = message.reference.message_id
    except AttributeError:
        return
    global cd, filename, fontcd
    img = Image.open(filename)
    imw, imh = img.size
    capw, caph = imw, int(0.25* (imw - imh))
    I1 = ImageDraw.Draw(img)
    #without caption = (680, 404)
    #with caption = (680, 498)
    selected_size = 1
    cap = white_bg_square(img)
    I1 = ImageDraw.Draw(cap)
    msg = await message.channel.fetch_message(message.reference.message_id)
    final = "\"{0}\"".format(msg.content)
    if final == "":
        final = "SUCK ME"
    for i in range(1, imw//5):
        arial = ImageFont.FreeTypeFont(fontcd, size=i)
        left, top, right, bottom = arial.getbbox(final)
        w = right - left
        h = bottom - top
        print(w, h)
        if w > capw or h > caph:
            break
        selected_size = i
        print(arial.size)
    arial = ImageFont.FreeTypeFont(fontcd, size=selected_size)
    I1.text((capw//2, caph//2), final, fill='black', anchor='mm', font=arial)
    cap.save(cd + "1948." + fmat)
    return await message.reply(file = discord.File(cd + "1948." + fmat))

def white_bg_square(im):
    w, h = im.size
    img2 = im.crop( (0, -int(0.25*(w - h)), w, h))
    draw = ImageDraw.Draw(img2)
    draw.rectangle( (0,0,w,int(0.25*(w - h))), fill="white")
    del draw
    return img2

client.run(TOKEN)

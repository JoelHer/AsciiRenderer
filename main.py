import discord, os, pointsdata, keepalive, traceback, threeDtotwoD, time, asyncio, asciitoimg, requests
from twoDtoascii import stringToMat
from objFile import obj_to_list

TOKEN = os.environ["TOKEN"]

intents = discord.Intents.all()

client = discord.Client(intents=intents)


@client.event
async def on_ready():  # functions in function with clients
  print('Client 1 Logged in!')


def repeat(shape,
           frames,
           message,
           anglediffx=10,
           anglediffy=10,
           anglediffz=10):
  count = 0
  angx = 0
  angy = 0
  angz = 0
  while count < frames:
    matrix = threeDtotwoD.run(shape, 10, count, angx, angy, angz)
    angx += anglediffx
    angy += anglediffy
    angz += anglediffz
    asciitoimg.asciiToIMG(matrix, count)
    count += 1

  asciitoimg.imagesToGif(frames)


def delete(frames):
  for i in range(frames):
    os.remove(os.path.join("images", f"image{i}.png"))
  os.remove(os.path.join("images", "render.gif"))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.channel == client.get_channel(
      1067114584353280030) or message.channel == client.get_channel(
        1067097013667246231):  # test server channel and main channel
    if message.content.startswith('!r'):  # render command --> cube/pyramid
      shape = message.content.replace('!r ', '')
      content = shape.split(' ')
      content.pop(0)
      diff = 10
      if len(content) == 3:
        dix = int(content[0])
        diy = int(content[1])
        diz = int(content[2])
      else:
        dix = diff
        diy = diff
        diz = diff

      frames = 20

      if shape.startswith('cube'): matrix = pointsdata.cube
      elif shape.startswith('pyramid'): matrix = pointsdata.pyramid
      else:
        await message.channel.send('Not a valid shape, use !cr [custom list]')

      repeat(matrix, frames, message, dix, diy, diz)
      await message.channel.send(
        file=discord.File(os.path.join('images', 'render.gif')))
      await asyncio.sleep(1)
      delete(frames)

    if message.content.startswith('!cr '):
      mess = message.content.replace('!cr ', '')
      content = mess.split(' ')
      matrix = stringToMat(content[0])
      content.pop(0)
      frames = 20
      diff = 10
      if len(content) == 3:
        dix = int(content[0])
        diy = int(content[1])
        diz = int(content[2])
      else:
        dix = diff
        diy = diff
        diz = diff

      frames = 20

      repeat(matrix, frames, message, dix, diy, diz)
      await message.channel.send(
        file=discord.File(os.path.join('images', 'render.gif')))
      await asyncio.sleep(1)
      delete(frames)
    if message.content.startswith('!fr'):
      if len(message.attachments) != 0:
        message.channel.send("````Loading File...```")
        print(requests.get(message.attachments[0]))


keepalive.keep_alive()

try:
  client.run(TOKEN)
except:
  # print('Error: RESTARTING NOW --> line 33')
  print(
    f'\n\n\nERROR OCCURED WHILST CONNECTING TO DISCORD API: {traceback.print_exc()}\nRESTARTING NOW\n\n\n'
  )
  os.system('python restarting.py')
  os.system("kill 1")

import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
import bot_messages,functions

from functions import *

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)

 #getting discord elements

Bot = commands.Bot(command_prefix = "!", intents = intents, help_command = None) #using "!" for bot command.

@Bot.event
async def on_ready():
  print("let's go") # see this while bot is running
  file_create(Bot)




@Bot.command() #help command
@has_permissions(administrator = True)
async def help(ctx):
  await ctx.channel.send(bot_messages.bot_help)





@Bot.command()
@has_permissions(administrator = True) # you can select which user can use this command. i selected admin.
async def command_channel(ctx, arg1: discord.TextChannel): #command channel to use bot command.

  file_create(Bot)
  command_channel_ids = command_channel_list(ctx.message.guild.id)


  if len(command_channel_ids) >= 1:
    await ctx.channel.send(bot_messages.command_channel_set)
    return

  if arg1 == None:
    await ctx.channel.send(bot_messages.parametres_error)
    return

  command_channel_set(arg1.id, ctx.message.guild.id)
  await ctx.channel.send(f"Has been set !{ctx.author.mention}")



@Bot.command()
@has_permissions(administrator = True)
async def add_channel(ctx,arg1: discord.TextChannel, arg2: discord.TextChannel,arg3 = None,arg4=None,encoding="utf8"): #4 parametres for bot working

  guild_id = ctx.message.guild.id
  command_channel_ids = command_channel_list(guild_id)[0]

  if len(command_channel_ids) == 0:
    await ctx.channel.send(bot_messages.set_command)
    return
  if ctx.channel.id != int(command_channel_ids[0]): #checking if channel is command channel
    return await ctx.channel.send(bot_messages.command_channel_error)

  if any(params is None for params in [arg1, arg2, arg3, arg4]): #checking parametres is entered or not entered
    return await ctx.channel.send(bot_messages.parametres_error)

  if not arg3.isdigit():
    return await ctx.channel.send(bot_messages.ammount_error) #checking for third parametres is int or not

  if not arg4.encode("utf-8"):
    return await ctx.channel.send(bot_messages.emoji_error) #checking for fourth parametres is emoji or not
  add_channel1(arg1.id,arg2.id,arg3,arg4,guild_id)
  await ctx.channel.send(bot_messages.channels_add)



@Bot.command()
@has_permissions(administrator = True)
async def show_channel(ctx, arg1 = None): #show channel command
  guild_id = ctx.message.guild.id
  command_channel_ids = command_channel_list(guild_id)[0]
  channel_lists = channel_list(guild_id)
 

  if len(command_channel_ids) == 0:
    await ctx.channel.send(bot_messages.set_command)
    return

  #if arg1 is empty, it's gonna show all channel. but if you put in something, it's gonna show that index
  if ctx.channel.id != int(command_channel_ids[0]): #checking if channel is command channel
    return await ctx.channel.send(bot_messages.command_channel_error)
   
  if len(channel_lists)==0: #checking list is empty or not
    await ctx.channel.send(bot_messages.empty_channels)
    return
   
  if arg1 != None and int(arg1)<=len(channel_lists) and arg1.isdigit()==True: #showing channel for arg1 index
    arg1=int(arg1)
    await ctx.channel.send(
      f"**{arg1}.** **from: {Bot.get_channel(int(channel_lists[arg1-1][0])).mention}**,**to: {Bot.get_channel(int(channel_lists[arg1-1][1])).mention}**, **count: {channel_lists[arg1-1][2]}**, **emoji: {channel_lists[arg1-1][3]}**\n")
    return
  
  

  count = 1
  for i in channel_lists: #then shows channels that you added
    

    await ctx.channel.send(
      f"**{count}.** **from: {Bot.get_channel(int(i[0])).mention}**,**to: {Bot.get_channel(int(i[1])).mention}**, **count: {i[2]}**, **emoji: {i[3]}**\n")
    count+=1



@Bot.command()
@has_permissions(administrator = True)
async def delete_channel(ctx, arg1): #delete channel command

  guild_id = ctx.message.guild.id #getting guild_id
  command_channel_ids = command_channel_list(guild_id) #getting our command channel id
  channel_lists = channel_list(guild_id) #getting our channels we set "add_channel" before


  if len(command_channel_ids) == 0:
    await ctx.channel.send(bot_messages.set_command)
    return

  if ctx.channel.id != int(command_channel_ids[0]):
    return await ctx.channel.send(bot_messages.command_channel_error)

  if len(channel_lists) == 0:
    await ctx.channel.send(bot_messages.empty_channels)
    return
  if arg1.isdigit() == True:
    arg1=int(arg1)
    
  else:
    ctx.channel.send(bot_messages.int_error)
    return

  delete_channels(arg1, guild_id)
  await ctx.channel.send(bot_messages.channel_deleted)

@Bot.event
async def on_raw_reaction_add(payload): #the work place.
  user = Bot.get_user(payload.user_id)
  guild = Bot.get_guild(payload.guild_id)
  channel = guild.get_channel(payload.channel_id)
  message = await channel.fetch_message(payload.message_id)
  emoji_lists = [emoji[0].replace("'", "") for emoji in emoji_list(payload.guild_id)]
  channel_lists =  channel_list(payload.guild_id)




  if payload.emoji.name in emoji_lists: #checking the reaction emoji is our list or not
    emoji_index = emoji_lists.index(payload.emoji.name) #then getting index of emoji

    for reaction in message.reactions:
      if reaction.emoji == payload.emoji.name: #checking the emoji is in our list or not
        EmojiCount = reaction.count
        if EmojiCount == int(channel_lists[emoji_index][2]): #checking EmojiCount is equal our count or not

          if int(payload.channel_id) != int(channel_lists[emoji_index][0]): #checking channel id is equal our channel id or not
            return
          if message.author.id == Bot.user.id: #checking messages's owner is bot or not
            return
          if (reaction.me) and (reaction.emoji == "✅"): #checking the emoji reactioner is bot or not. this is important because bot can't do this 2rd times or much
            return
         

          await Bot.get_channel(int(channel_lists[index1][1])).send( #it moves messages to selected channel
              "Written by {} :\n\n {}".format(message.author.mention, message.content),
              files=[await f.to_file() for f in message.attachments])
          
          await Bot.get_channel(int(channel_lists[index1][0])).send( #it sends messages channel to say "that messages moved"
              "{} your message moved to this channel --> {}".format(message.author.mention,
                                                                    Bot.get_channel(int(channel_lists[index1][1])).mention))
          
          await message.add_reaction("✅") #then adding a reaction for don't archive message again.
          return

Bot.run("") # you have to add yout bot's token here as a string

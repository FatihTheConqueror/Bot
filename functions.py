import os
def file_create(Bot):
    for guild in Bot.guilds:
        if not os.path.exists(f"guilds/{guild.id}"):
            os.makedirs(f"guilds/{guild.id}")
            file = open(f"guilds/{guild.id}/channels.txt", "w")
            file.close()
            file1 = open(f"guilds/{guild.id}/command_channel.txt", "w")
            file1.close()


def command_channel_list(guild_id):
    file = open(f"guilds/{guild_id}/command_channel.txt", "r")
    command_channel_list = file.readlines()
    file.close()
    return command_channel_list


#channel list
def channel_list(guild_id):
    file1 = open(f"guilds/{guild_id}/channels.txt", "r", encoding="utf8")
    channel = file1.read().split("\n")

    file1.close()

    for i in range(len(channel)):
        if channel[i] == "":
            del channel[i]

    for i in range(len(channel)):
        channel[i] = channel[i].split(",")
    try:
        for i in range(len(channel)):
            channel[i][0] = int(channel[i][0])
            channel[i][1] = int(channel[i][1])
            channel[i][2] = int(channel[i][2])
    except:
        pass

    return channel


def command_channel_set(arg1,guild_id):


    file = open(f"guilds/{guild_id}/command_channel.txt", "w")
    file.write(str(arg1)) #writing command channel id to our command channel text file
    file.close()



#define a function that adding parametres to txt file
def add_channel1(arg1,arg2,arg3,arg4,guild_id):
    channel_lists = channel_list(guild_id)



    channel_lists.append([arg1,arg2,arg3,arg4]) #adding channels by a list to matris list
   


    file =open(f"guilds/{guild_id}/channels.txt","w",encoding="utf8")
    if len(channel_lists) != 0:
        for i in channel_lists:
            for j in range(0, 4):
                if j != 3:
                    file.write(str(i[j]) + ",")
                if j == 3:
                    file.write(str(i[j]) + "\n")  # adding channel to txt file
    else:
        file.write(f"{str(arg1)},{str(arg2)},{str(arg3)},{str(arg4)}")



    file.close()

def delete_channels(arg1,guild_id):#deleting channel function

    channel_lists = channel_list(guild_id)

    del channel_lists[arg1-1] # deleting channels in our list
    file = open(f"guilds/{guild_id}/channels.txt", "w", encoding="utf8")
    for i in channel_lists:
        for j in range(0, 4):
            if j != 3:
                file.write(str(i[j]) + ",")
            if j == 3:
                file.write(str(i[j]) + "\n")  # adding channels to txt file with a loop
    return True

def emoji_list(guild_id):
    channel_lists = channel_list(guild_id)
    emoji_lists=[]
 
    for i in channel_lists: #getting emojis in our list. this will be help us on get index
        emoji_lists.append(i[3])
    return emoji_lists

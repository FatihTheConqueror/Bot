
#command channel
file=open("command_channel.txt","r")
command_channel_list=file.readlines()
file.close()

#channel list
file1 = open("channels.txt", "r", encoding="utf8")
channel_list = file1.read().split("\n")
for i in range(0, len(channel_list)):
    channel_list[i] = channel_list[i].split(",")
file1.close()
if channel_list[0] == [""]:
    del channel_list[0]
for i in range(0, len(channel_list)):
    if channel_list[i] == [""]: # if channels.txt file empty, we have to do this for bot working.
        del channel_list[i]  # in here we made a list by matris format.
for i in range(0, len(channel_list)):

    channel_list[i][0]=int(channel_list[i][0])
    channel_list[i][1] = int(channel_list[i][1])
    channel_list[i][2] = int(channel_list[i][2])  # in here we made a channel list by matris format.

# here we're gonna add command channel id with a function
def mention_check(arg):
    if len(arg) == 21 and arg[0] == "<" and arg[1] == "#" and arg.endswith(">"):
        return True
    else:
        return False

def command_channel_set(arg1):
    command_channel_id = ""
    if mention_check(arg1)==True:
        for i in arg1:
            if i == "<" or i == "#" or i == ">":
                pass
            else:
                command_channel_id += i #discord is not givind id only with integers numbers. so we have to do that.
    file = open("command_channel.txt", "w")
    file.write(command_channel_id) #writing command channel id to our command channel text file
    file.close()
# discord is not giving id only with numbers. so, we define a function to do this.
def get_channels_id(arg): #discord is not givind id only with integers numbers. so we have to do that.
    arg0=""
    for i in arg:
        if i.isdigit(): #here we made a checks that string only takes int numbers.
            arg0 = arg0 + i
    return arg0

#define a function that adding parametres to txt file
def add_channel(arg1,arg2,arg3,arg4):

    arg1 = get_channels_id(arg1) #getting channels id with function
    arg2 = get_channels_id(arg2)


    channel_list.append([arg1,arg2,arg3,arg4]) #adding channels by a list to matris list


    file =open("channels.txt","w",encoding="utf8")
    for i in channel_list:
        for j in range(0,4):
            if j!=3:
                file.write(str(i[j]) + ",")
            if j==3:
                file.write(str(i[j]) + "\n") #adding channel to txt file
    file.close()

def delete_channels(arg1):#deleting channel function
    del channel_list[arg1-1] # deleting channels in our list
    file = open("channels.txt", "w", encoding="utf8")
    for i in channel_list:
        for j in range(0, 4):
            if j != 3:
                file.write(str(i[j]) + ",")
            if j == 3:
                file.write(str(i[j]) + "\n")  # adding channels to txt file with a loop
    return True

def emoji_list():
    emoji_lists=[]
    for i in channel_list: #getting emojis in our list. this will be help us on get index
        emoji_lists.append(i[3])
    return emoji_lists

import os
from db.config import cursor
def file_create(Bot):
    for guild in Bot.guilds:
        cursor.execute(f"""
CREATE TABLE IF NOT EXISTS table_{guild.id}(
from_channel VARCHAR,
to_channel VARCHAR,
count INTEGER,
emoji VARCHAR,
command_channel_id VARCHAR
)

""")


def command_channel_list(guild_id):
    

    query = f"SELECT command_channel_id FROM table_{guild_id} WHERE command_channel_id IS NOT NULL"
    cursor.execute(query)
    return cursor.fetchall()


#channel list
def channel_list(guild_id):
    query = f"SELECT * FROM table_{guild_id} WHERE from_channel IS NOT NULL AND to_channel IS NOT NULL AND count IS NOT NULL AND emoji IS NOT NULL"
    cursor.execute(query)
    return cursor.fetchall()


def command_channel_set(arg1,guild_id):
    cursor.execute(f"""
CREATE TABLE IF NOT EXISTS table_{guild_id}(
from_channel VARCHAR,
to_channel VARCHAR,
count INTEGER,
emoji VARCHAR,
command_channel_id VARCHAR
)

""")

    cursor.execute(f"""INSERT INTO table_{guild_id} (command_channel_id, from_channel, to_channel, count, emoji)
VALUES (%s, %s, %s, %s, %s)""", (str(arg1), None, None, None, None))





#define a function that adding parametres to txt file
def add_channel1(arg1,arg2,arg3,arg4,guild_id):
   query = f"INSERT INTO table_{guild_id} (from_channel, to_channel, count, emoji, command_channel_id) VALUES (%s ,%s, %s, %s, %s)"
   cursor.execute(query, (str(arg1), str(arg2), int(arg3), str(arg4), None))




def delete_channels(arg1,guild_id):#deleting channel function
    query = f"""DELETE FROM table_{guild_id}
WHERE ctid IN (
  SELECT ctid
  FROM table_{guild_id}
  WHERE command_channel_id IS NOT NULL
  ORDER BY ctid
  OFFSET {arg1}
  LIMIT 1
)"""
    cursor.execute(query)

def emoji_list(guild_id):
    query = f"SELECT emoji FROM table_{guild_id} WHERE emoji IS NOT NULL"
    cursor.execute(query)
    return cursor.fetchall()
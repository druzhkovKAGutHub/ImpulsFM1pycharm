import psycopg2 as ps2
from aiogram.types import Message
from aiogram import Bot

def PostgreSQLWorker(message: Message, bot:Bot, whith_section):
    userId = UsersIdByTelegramId(message.from_user.id)
    users_info_insert(userId,is_bot=message.from_user.is_bot, first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,username=message.from_user.username,language_code=message.from_user.language_code
                        ,is_premium= message.from_user.is_premium,added_to_attachment_menu=message.from_user.added_to_attachment_menu,
                        can_join_groups=message.from_user.can_join_groups)
    users_mess_insert(userId, mess=message.text, chat_bot_id=bot.id, mess_id=message.message_id,whith_section=whith_section)    

# Вставка данных в табличку Users
def UsersIdByTelegramId(telegram_id):
    conn=ps2.connect(dbname="ImpulsFM",host="10.222.222.184",user="postgres",password="sa",port="5433")
    #print("Подключение утановленно")
    
    # = [123457]
    #telegram_id_val = [telegram_id]
    sql1="insert into users (telegram_id) values(%s) returning id"
    sql2="select id from users where telegram_id = %s"
 #   sql3="select id from users where telegram_id = 1234588"

    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(sql2,[telegram_id])
    id = cursor.fetchone()
    if id is None:
        cursor.execute(sql1,[telegram_id])
        id = cursor.fetchone()    

    cursor.close()
    conn.close()
    
    return id[0]
            
# Вставка данных в табличку users_info
def users_info_insert(users_id, *, is_bot=None, first_name=None, last_name=None, username=None, language_code=None, is_premium=None, 
                     added_to_attachment_menu=None, can_join_groups=None):
 
    userAlreadyExists = f"select count(*) from users_info ui where users_id = '{users_id}'"
    conn = ps2.connect(dbname="ImpulsFM",host="10.222.222.184",user="postgres",password="sa",port="5433")
    
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(userAlreadyExists)
    userCount = cursor.fetchone()

    if userCount[0]==0:
        name_feal = ["users_id", "is_bot", "first_name", "last_name", "username", "language_code", "is_premium", "added_to_attachment_menu", "can_join_groups"]

        name_field = "users_id"
        name_value = f"'{users_id}'"
        if is_bot is not None: 
            name_field += "," + name_feal[1]
            name_value += "," + str(is_bot)
        if first_name is not None: 
            name_field += "," + name_feal[2]
            name_value += f",'{first_name}'"
        if last_name is not None: 
            name_field += "," + name_feal[3]
            name_value += f",'{last_name}'"
        if username is not None: 
            name_field += "," + name_feal[4]
            name_value += f",'{username}'"
        if language_code is not None: 
            name_field += "," + name_feal[5]
            name_value += f",'{language_code}'"
        if is_premium is not None: 
            name_field += "," + name_feal[6]
            name_value += "," + str(is_premium)
        if added_to_attachment_menu is not None: 
            name_field += "," + name_feal[7]
            name_value += "," + str(added_to_attachment_menu)
        if can_join_groups is not None: 
            name_field += "," + name_feal[8]
            name_value += "," + str(can_join_groups)

        insert = f"INSERT INTO users_info ({name_field}) VALUES({name_value})"
        cursor = conn.cursor()
        cursor.execute(insert)

    cursor.close
    conn.close

# Вставка данных в табличку user_mess    
def users_mess_insert(users_id, *, mess=None, chat_bot_id=None, mess_id=None, whith_section=None):
    
    name_field = "users_id"
    name_value = f"'{users_id}'"

    if mess is not None: 
        name_field += f",mess"
        name_value += f",'{mess}'"
    if chat_bot_id is not None:
        name_field += f",chat_bot_id"
        name_value += f",'{chat_bot_id}'"
    if mess_id is not None:
        name_field +=',messtext_teleg_id'
        name_value +=f",'{mess_id}'"
    if whith_section is not None:
        name_field +=',whith_section_mess'
        name_value +=f",'{whith_section}'"

    insert = f"INSERT INTO users_mess ({name_field}) VALUES({name_value})"      
    conn = ps2.connect(dbname="ImpulsFM",host="10.222.222.184",user="postgres",password="sa",port="5433")
    
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(insert)
    
    cursor.close
    conn.close

#users_mess_insert(UsersIdByTelegramId(123457),mess='проверка получения данных',chat_bot_id='98765422')

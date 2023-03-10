import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """<i><b>π Helo {}, I'm <a href=https://telegram.me/{}>{}</a></i></b> \n\n<i><b>πI Can Provide You Any Movies, Web-Series, Anime, K-Dramas, Animation, etc.,</i></b>"""
    HELP_TXT = """<b>π₯ </b><b><u>How To Download Any Movie, Series, Anime etc., For Free???</u></b> \n\n<b>πGroup [01]: </b><b>https://t.me/+WzsvFY3qXa9kZGVl</b> \n\n<b>πGroup</b> <b>[02]: </b><b>https://t.me/+EdJU1Hqk1N80ZWQ1</b> \n\n<b>π Join Any Of Above Groupsπ </b> """
    ABOUT_TXT = """<i><b>π₯ Follow These Steps To Connect Me To Your Groupπ</b>

1. Click on "</i><i><b>Click Here To Add Me</b>" 
2. Select Your Group
3. Make Me Admin in Your Group</i>"""    
    
    STATUS_TXT = """<b>ποΈ My Statistics π²</b>
β <b>Total Files :</b> {}
β <b>Total Users :</b> {}
β <b>Total Chats :</b> {}
β <b>Used Storage :</b> {} 
β <b>Free Storage :</b> {}"""

    LOG_TEXT_G = """<b>#NewGroup</b>
<b>β Group Β»</b> {} 
<b>β ID Β»</b> <code>{}</code>
<b>β Total Members Β»</b> {}
<b>β Added By Β»</b> {}
"""
    LOG_TEXT_P = """<b>#NewUser</b>
β ID - <code>{}</code>
β Name - {}
"""

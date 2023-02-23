from pony.orm import *
from pyrogram.types import Message
from os import listdir

# ========= DB build =========
db = Database()


class User(db.Entity):
    uid = PrimaryKey(int, auto=True)
    status = Required(int)  # status-user: "INSERT"/"NOT-INSERT"


db.bind(provider='sqlite', filename='zipbot.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# ========= helping func =========
def dir_work(uid: int) -> str:
    """ static-user folder """
    return f"static/{uid}/"


def zip_work(uid: int) -> str:
    """ zip-archive file """
    return f'static/{uid}.zip'


def list_dir(uid: int) -> list:
    """ items in static-user folder """
    return listdir(dir_work(uid))


def up_progress(current, total, msg: Message):
    """ edit status-msg with progress of the uploading """
    msg.edit(f"**התקדמות ההעלאה: {current * 100 / total:.1f}%**")


# ========= MSG class =========
class Msg:

    def start(msg: Message) -> str:
        """ return start-message text """
        txt = f"السلام عليكم . أنا بوت ضغط الملفات . فقط اضغط الأمر \n\n /zip \n\n ثم أرسل الملفات التي تريد ضغطها ثم الأمر \n\n /stopzip .  \n\n لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 \n\n تم تطويره بواسطة @M100achuzBots "
        return txt

    zip = "أرسل الملفات التي تريد ضغطها ثم اضغط الأمر \n\n /stopzip "
    too_big = "الملف كبير للغاية "
    too_much = "لا يسمح بأكثر من 20 ملف"
    send_zip = "أولاً :اضغط الأمر \n\n /zip \n\n ثم أرسل الملفات  "
    zipping = "جاري الضغط"
    uploading = "جاري الرفع"
    unknow_error = "خطأ غير معلوم"
    downloading = "جاري التحميل"
    zero_files = "جاري إخلاء الملفات "

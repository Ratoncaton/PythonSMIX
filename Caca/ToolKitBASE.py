import pickle

def user():
    user = {
    "name": "",
    "password": "",
    "user_main_dir": "",
    "user_1dir": "",
    "user_image_dir": "",
    "user_video_dir": "",
    "user_pdf_dir": "",
    "user_exe_dir": "",
    "user_rar_dir": "",
    "user_webgrafia_dir": "",
    "user_password_dir": "",
    "user_link_dir": ""
    }

def save():
    with open("base.pkl", "wb") as base:
        pickle.dump(user, base)
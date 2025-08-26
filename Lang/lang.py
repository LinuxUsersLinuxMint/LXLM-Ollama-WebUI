import configparser

lang = configparser.ConfigParser()
lang.read('Lang/lang.ini')

def set_lang(userlang):
    lang["WebUILang"]["lang"] = userlang
    with open('Lang/lang.ini', 'w') as f:
        lang.write(f)

user_lang = lang["WebUILang"]["lang"]

lang_file = configparser.ConfigParser()
lang_file.read(f"Lang/{user_lang}.ini", encoding="utf-8")

your_password = lang_file["LangContent"]["your_password"]
password_recovery_failed = lang_file["LangContent"]["password_recovery_failed"]
app_title = lang_file["LangContent"]["app_title"]
user_name_input = lang_file["LangContent"]["user_name_input"]
password_input = lang_file["LangContent"]["password_input"]
login_var = lang_file["LangContent"]["login_var"]
new_user_register = lang_file["LangContent"]["new_user_register"]
login_successfully = lang_file["LangContent"]["login_successfully"]
welcome = lang_file["LangContent"]["welcome"]
go_to_app = lang_file["LangContent"]["go_to_app"]
login_failed = lang_file["LangContent"]["login_failed"]
user_ = lang_file["LangContent"]["user_"]
login_failed_description = lang_file["LangContent"]["login_failed_description"]
user_register = lang_file["LangContent"]["user_register"]
try_again = lang_file["LangContent"]["try_again"]
pass_rec_ = lang_file["LangContent"]["pass_rec_"]
user_register_ip = lang_file["LangContent"]["user_register_ip"]
password_forget = lang_file["LangContent"]["password_forget"]
password_recovery = lang_file["LangContent"]["password_recovery"]
password_recovery_ = lang_file["LangContent"]["password_recovery_"]
password_recovery_input = lang_file["LangContent"]["password_recovery_input"]
password_recovery_submit = lang_file["LangContent"]["password_recovery_submit"]
password_recovery_report = lang_file["LangContent"]["password_recovery_report"]
user_register_failed = lang_file["LangContent"]["user_register_failed"]
register = lang_file["LangContent"]["register"]
user_register_failed_title = lang_file["LangContent"]["user_register_failed_title"]
user_register_failed_description = lang_file["LangContent"]["user_register_failed_description"]
user_register_successfully = lang_file["LangContent"]["user_register_successfully"]
user_register_successfully_description = lang_file["LangContent"]["user_register_successfully_description"]
ollama_web_ui_title = lang_file["LangContent"]["ollama_web_ui_title"]
user_model = lang_file["LangContent"]["user_model"]
model_question = lang_file["LangContent"]["model_question"]
model_submit = lang_file["LangContent"]["model_submit"]
exit = lang_file["LangContent"]["exit"]
app_requirements = lang_file["LangContent"]["app_requirements"]
app_requirements_description = lang_file["LangContent"]["app_requirements_description"]
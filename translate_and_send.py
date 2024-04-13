import requests
url = 'https://api-free.deepl.com/v2/translate'
import pyperclip
import keyboard
import pyautogui
import time

headers = {
    'Authorization': '#'  # Lütfen kendi yetkilendirme anahtarınızı buraya ekleyin
}
data = {
    'text': "",
    'target_lang': 'EN'
}

def translate(text):
    data['text'] = text
    response = requests.post(url, headers=headers, data=data)
    translated_text = response.json()['translations'][0]['text']
    return translated_text



def select_all():
    pyautogui.hotkey('ctrl', 'a')

def cut_text():
    pyautogui.hotkey('ctrl', 'x')

def on_enter():
    select_all()  
    cut_text()  
    text = pyperclip.paste() 
    if text:
        translated_text = translate(text)
        keyboard.write(translated_text)  

keyboard.add_hotkey('pagedown', on_enter)

print("Script çalışıyor... 'Page Down' tuşuna basarak test edebilirsiniz.")
keyboard.wait('esc')  
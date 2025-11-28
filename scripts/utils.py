import os
import sys
from kivy.lang import Builder

def get_resource_path(relative_path):
    """Получает правильный путь для ресурсов в exe и в разработке"""
    try:
        # PyInstaller создает временную папку в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def load_kv_file(kv_filename):
    """Загружает KV файл с правильным путем"""
    Builder.load_file(get_resource_path(kv_filename))
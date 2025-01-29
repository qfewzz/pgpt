import os
import sys

KEY_system_prompt = 'system_prompt.txt'

def get_value(key: str) -> str:
    file_path = os.path.join('live_config_files', key)
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        
    return file_content

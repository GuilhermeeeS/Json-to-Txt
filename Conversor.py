import os
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

user_profile = os.path.expanduser("~")
desktop_path = os.path.join(user_profile, "Desktop")
source_dir = os.path.join(desktop_path, "Json")  
destination_dir = os.path.join(desktop_path, "Txt")  

os.makedirs(source_dir, exist_ok=True)
os.makedirs(destination_dir, exist_ok=True)

class JSONHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".json"):
            try:
                try:
                    with open(event.src_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except UnicodeDecodeError:
                    with open(event.src_path, 'r', encoding='ISO-8859-1') as f:
                        data = json.load(f)
                
                txt_file_name = os.path.splitext(os.path.basename(event.src_path))[0] + ".txt"
                txt_file_path = os.path.join(destination_dir, txt_file_name)
                
                with open(txt_file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
                
                print(f"Arquivo {txt_file_name} convertido com sucesso e salvo em {destination_dir}")
            
            except Exception as e:
                print(f"Erro ao processar o arquivo, possívelmente o arquivo ja existe {event.src_path}: {e} ")

def start_monitoring():
    event_handler = JSONHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_dir, recursive=False)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    print(f"Monitorando a pasta: {source_dir}")
    start_monitoring()

import threading
from Partie import *

def thread():
    partie = Partie()
    
code_thread = threading.Thread(target=thread)
code_thread.start()
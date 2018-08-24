# saved as server.py
import Pyro4, Pyro4.naming
import socket, threading

# Define an object that will be accessible over the network.
# This is where all your code should go...
@Pyro4.expose
class MessageServer(object):
    def show_message(self, msg):
        print("Message received: {}".format(msg))


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
# register the message server as a Pyro object
main_daemon_uri = main_daemon.register(MessageServer)
# register a name for the object in the name server
ns.register("example.message", main_daemon_uri)

# start the event loop of the main_daemon to wait for calls
print("Message server ready.")
main_daemon.requestLoop()

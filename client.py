# saved as client.py
import Pyro4
import sys

print("What is your message?")
msg = sys.stdin.readline().strip()

# lookup object uri on name server and create a proxy for it
message_server = Pyro4.Proxy("PYRONAME:example.message")
# call method on remote object
message_server.show_message(msg)

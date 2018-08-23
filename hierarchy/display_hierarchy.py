import webbrowser
from http.server import SimpleHTTPRequestHandler
import socketserver
import _thread as thread
import time
import sys


def start_server(server):
    server.serve_forever()


def display():
    # current_dir = dirname(realpath(__file__))
    try:
        PORT = 8000
        Handler = SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", PORT), Handler)
        _ = thread.start_new_thread(start_server, (httpd,))
        webbrowser.open('http://0.0.0.0:{}/hierarchy/radial.html'.format(PORT))
        while True:
            time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        print("CLOSING SOCKET")
        httpd.socket.close()
        print("SHUTTING DOWN SERVER")
        httpd.shutdown()
        print("EXITING SYSTEM")
        sys.exit()
        return None


if __name__ == '__main__':
    display()

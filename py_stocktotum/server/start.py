from .server import create_server

server = create_server()
if __name__ == '__main__':
    server.run(host="0.0.0.0", port=8000)
import socket


class Console:
    sock: socket
    name : str
    
    def __init__(self, console_port) -> None:
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(("localhost", console_port))
        except Exception as e:
            raise(e)
    
    def write_cmd(self, cmd : str):
        self.sock.send(cmd.encode() + b'\r')
    
        
        

from socket import socket


class Console:
    sock: socket
    name : str
    
    def __init__(self, console_port, name='') -> None:
        self.name = name
        try:
            self.sock = socket(("localhost", console_port))
        except Exception as e:
            raise(e)
    
    def write_cmd(self, cmd : str):
        self.sock.send(cmd.encode() + b'\r')
    
        
        

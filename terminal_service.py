class TerminalService:
    def __init__(self):
        self.current_server = None
        self.servers = ['localhost:5006', 'localhost:5056', 'localhost:50557', 'localhost:5058']
        self.current_index = 0

    def add_server(self, server):
        self.servers.append(server)

    def get_next_server(self):
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

    def check_current_servers(self):
        if len(self.servers) == 0:
            self.servers.append('localhost:5051')
        return

    def receive_pollution_channel(self):
        self.check_current_servers()
        return self.get_next_server()

    def send_pollution(self):
        return

    def receive_meteo_channel(self):
        self.check_current_servers()
        return self.get_next_server()

    def set_server(self, server):
        self.current_server = server
        print('swetejat be xd' + str(self.current_server))

    def get_server(self):
        return self.get_next_server(self)


RRLB = RoundRobinLoadBalancer()

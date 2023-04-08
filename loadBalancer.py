class RoundRobinLoadBalancer:
    def __init__(self):
        self.servers = []
        self.current_index = 0

    def add_server(self, server):
        self.servers.append(server)

    def get_next_address(self):
        address = self.addresses[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.addresses)
        return address

    def check_current_servers(self):
        if len(self.servers) == 0:
            self.servers.append('localhost:5051')
        return

    def recieve_pollution(self, pollution):
        self.check_current_servers()
        return self.get_next_address()

    def send_pollution(self):
        return

    def recieve_meteo(self, meteo):
        self.check_current_servers()
        new_address = self.get_next_address()

    def send_meteo(self, meteo):
        print()

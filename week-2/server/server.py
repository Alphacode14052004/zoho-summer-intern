import time
from datetime import datetime, timedelta

class Server:
    def __init__(self, name):
        self.name = name
        self.daily_clients_count = 0
        self.monthly_clients_count = 0
        self.total_clients_count = 0
        self.total_lost_clients_count = 0
        self.total_ratings_sum = 0
        self.rating_count = 0
        self.current_client = None

    def attend_client(self, client_name):
        self.current_client = client_name
        self.daily_clients_count += 1
        self.monthly_clients_count += 1
        self.total_clients_count += 1

    def finish_client(self, rating):
        self.total_ratings_sum += rating
        self.rating_count += 1
        self.current_client = None

    def average_rating(self):
        if self.rating_count == 0:
            return 0
        return self.total_ratings_sum / self.rating_count

    def __str__(self):
        return (f"Server {self.name}\n"
                f"Date and Time: {datetime.now()}\n"
                f"Clients attended today: {self.daily_clients_count}\n"
                f"Clients attended this month: {self.monthly_clients_count}\n"
                f"Average rating: {self.average_rating():.2f}\n"
                f"Total clients approached: {self.total_clients_count}\n"
                f"Total lost clients: {self.total_lost_clients_count}\n"
                f"Current client: {self.current_client}\n")

class Client:
    def __init__(self, name):
        self.name = name
        self.session_start_time = datetime.now()

    def __str__(self):
        return (f"Client {self.name}\n"
                f"Session Start Time: {self.session_start_time}\n")


servers = [Server("Server A"), Server("Server B"), Server("Server C")]

client1 = Client("Client1")
servers[0].attend_client(client1.name)

client2 = Client("Client2")
servers[1].attend_client(client2.name)

servers[0].finish_client(5)
servers[1].finish_client(4)

for server in servers:
    print(server)

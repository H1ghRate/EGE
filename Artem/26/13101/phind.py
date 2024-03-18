MAXIMUM_QUEUE_LENGTH = 14

def process_clients(clients):
    queue_0 = []
    queue_1 = []
    queue_2 = []
    served_in_window_2 = 0
    turned_away = 0

    for arrival_time, service_time, window_preference in clients:
        if window_preference == 2:
            if len(queue_2) < MAXIMUM_QUEUE_LENGTH:
                queue_2.append(arrival_time + service_time)
                served_in_window_2 += 1
            else:
                turned_away += 1
        else:
            # Determine which queue to add the client to
            if len(queue_0) < len(queue_1):
                if len(queue_0) < MAXIMUM_QUEUE_LENGTH:
                    queue_0.append(arrival_time + service_time)
                else:
                    turned_away += 1
            else:
                if len(queue_1) < MAXIMUM_QUEUE_LENGTH:
                    queue_1.append(arrival_time + service_time)
                else:
                    turned_away += 1

    return served_in_window_2, turned_away


with open('26_13101.txt', 'rt') as f:
    number_of_clients = int(f.readline())

    clients = []

    for client_info in f:
        clients.append(tuple(map(int, client_info.split())))

clients.sort()

served_in_window_2, turned_away = process_clients(clients)
print(f"Served in window 2: {served_in_window_2}")
print(f"Turned away: {turned_away}")

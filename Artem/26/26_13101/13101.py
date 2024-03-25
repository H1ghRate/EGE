MAXIMUM_NUMBER_OF_PEOPLE_IN_QUEUE = 14


def is_the_queue_free(number_of_people_window: int) -> bool:
    if number_of_people_window < MAXIMUM_NUMBER_OF_PEOPLE_IN_QUEUE:
        return True

    return False


def is_the_queue_will_be_free(when_the_last_one_leaves: int) -> bool:
    if arrival_time >= when_the_last_one_leaves:
        return True

    return False


with open('26_13101.txt', 'rt') as f:
    number_of_clients = int(f.readline())

    clients = []

    for client_info in f:
        clients.append(tuple(map(int, client_info.split())))

    clients.sort()

    counter_departure = 0
    number_of_client_who_were_in_the_second_queue = 0

    number_of_people_to_first_window = 0
    queue_the_last_one_leaves_first_window = []

    number_of_people_to_second_window = 0
    queue_the_last_one_leaves_second_window = []

    for client_info in clients:
        arrival_time, time_for_maintenance, window_number = client_info
        summa_for_first = max(queue_the_last_one_leaves_first_window) if len(queue_the_last_one_leaves_first_window) != 0 else arrival_time
        summa_for_second = max(queue_the_last_one_leaves_second_window) if len(queue_the_last_one_leaves_second_window) != 0 else arrival_time

        if window_number == 0:
            if number_of_people_to_first_window < number_of_people_to_second_window:
                number_of_people_to_first_window += 1
                queue_the_last_one_leaves_first_window.append(summa_for_first + time_for_maintenance)
            elif number_of_people_to_first_window > number_of_people_to_second_window:
                number_of_people_to_second_window += 1
                queue_the_last_one_leaves_second_window.append(summa_for_second + time_for_maintenance)
                number_of_client_who_were_in_the_second_queue += 1
            else:
                if is_the_queue_free(number_of_people_to_first_window):
                    number_of_people_to_first_window += 1
                    queue_the_last_one_leaves_first_window.append(summa_for_first + time_for_maintenance)
                elif is_the_queue_will_be_free(queue_the_last_one_leaves_first_window[0]):
                    queue_the_last_one_leaves_first_window.pop(0)
                    queue_the_last_one_leaves_first_window.append(summa_for_first + time_for_maintenance)
                elif is_the_queue_will_be_free(queue_the_last_one_leaves_second_window[0]):
                    queue_the_last_one_leaves_second_window.pop(0)
                    queue_the_last_one_leaves_second_window.append(summa_for_second + time_for_maintenance)
                    number_of_client_who_were_in_the_second_queue += 1
                else:
                    counter_departure += 1
        elif window_number == 1:
            if is_the_queue_free(number_of_people_to_first_window):
                number_of_people_to_first_window += 1
                queue_the_last_one_leaves_first_window.append(summa_for_first + time_for_maintenance)
            elif is_the_queue_will_be_free(queue_the_last_one_leaves_first_window[0]):
                queue_the_last_one_leaves_first_window.pop(0)
                queue_the_last_one_leaves_first_window.append(summa_for_first + time_for_maintenance)
            else:
                counter_departure += 1
        elif window_number == 2:
            if is_the_queue_free(number_of_people_to_second_window):
                number_of_people_to_second_window += 1
                queue_the_last_one_leaves_second_window.append(summa_for_second + time_for_maintenance)
                number_of_client_who_were_in_the_second_queue += 1
            elif is_the_queue_will_be_free(queue_the_last_one_leaves_second_window[0]):
                queue_the_last_one_leaves_second_window.pop(0)
                queue_the_last_one_leaves_second_window.append(summa_for_second + time_for_maintenance)
                number_of_client_who_were_in_the_second_queue += 1
            else:
                counter_departure += 1
print(
    'Counter:',
    counter_departure,
    '\nNumber of clients who were in the second queue:',
    number_of_client_who_were_in_the_second_queue
    )

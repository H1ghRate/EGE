n = int(input()) 
train = {} 
 
for _ in range(n): 
    command = input().split() 
     
    if command[0] == 'add': 
        for _ in range(int(command[1])): 
            train_dict[command[2]] = train_dict.get(command[2], 0) + 1 
    elif command[0] == 'get':  
        print(train_dict.get(command[1], 0)) 
    elif command[0] == "delete": 
        train_dict[command[1]] -= min(int(command[1]), train_dict.get(command[1], 0)) 
        if train_dict[command[1]] <= 0: 
            del train_dict[command[1]]
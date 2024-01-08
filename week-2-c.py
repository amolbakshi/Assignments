import re

with open ("../files/logData.txt", "r") as file:
    logdata = file.read()
    list_logdata = logdata.split("\n")
    my_dist_list = []
    for log in list_logdata:
        if len(log.split(" ")) > 9 : 
            host = log.split(" ")[0]
            user = log.split(" ")[2]
            time = ' '.join(log.split(" ")[3:5])[1:-1]
            time_new = time[0:-2]
            request = ' '.join(log.split(" ")[5:8])[1:-1]
            my_dist= {"host":host,"user_name":user,"time":time,"request":request}
            print(my_dist)
            my_dist_list.append(my_dist)
    my_dist_list
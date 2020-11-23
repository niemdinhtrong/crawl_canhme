import requests
import time
import configparser
import mysql
import beauti
import json
import datetime
from bs4 import BeautifulSoup


def get_config(file):
    config = configparser.ConfigParser()
    config.read(file)
    return config

def send_tele(token, chat_id, text):
    requests.get(
        "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
        .format(token, chat_id, text))

def get_new_post(url):
    get_data_qc = requests.get(url)
    #print(get_data_qc)
    soup_qc = BeautifulSoup(get_data_qc.text, "lxml")
    info_qc = soup_qc.find_all(class_="entry-title")
    for line_n in info_qc:
        url_n = beauti.getURL(line_n)
        title = beauti.getTitle(line_n)
        if url_n not in sql.mysql_query(myConnection, "links", "site"):
            sql.mysql_write_site(myConnection, url_n, title)
            send_tele(config["telegram"]["token"], config["telegram"]["chat_id"], url_n)

config = get_config("/root/code/canhme/setting_canhme")
sql = mysql.mysql(config["mysql"]["hostname"], config["mysql"]["username"],
                  config["mysql"]["password"], config["mysql"]["database"])
myConnection = sql.connection()
get_new_post("https://canhme.com/")

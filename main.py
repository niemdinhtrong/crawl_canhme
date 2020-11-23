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

def send_slack(url, text):
    data_1 = {'text':'{}'.format(text)}
    requests.post(url, data=json.dumps(data_1))

def mysql_write_new_info(sql, url, idsite, token, chat_id, url_slack):
    get_data = requests.get(url)
    soup = BeautifulSoup(get_data.text, "lxml")
    info = soup.find_all(class_="wpd-comment-right")
    for line in info:
        user_name = beauti.getUser(line)
        idCom = beauti.getidComment(line)
        Comment = beauti.getComment(line)
        if idCom not in sql.mysql_query(myConnection, "idcomment", "comment"):
            print(Comment)
            times = datetime.datetime.now()
            try:
                sql.mysql_write_comm(myConnection, idCom, idsite, user_name, Comment, times)
            except:
                try:
                    sql.mysql_write_comm(myConnection, idCom, idsite, user_name, '', times)
                except:
                    sql.mysql_write_comm(myConnection, idCom, idsite, '', '', times)
            text = Comment + "\n" +"Tại link:"+ url
            send_tele(token, chat_id, text)
            send_slack(url_slack, text)

def NH(url1):
    get_data_qc = requests.get(url1)
    #print(get_data_qc)
    soup_qc = BeautifulSoup(get_data_qc.text, "lxml")
    info_qc = soup_qc.find_all(class_="entry-title")
    for line_n in info_qc:
        url_n = beauti.getURL(line_n)
        title = beauti.getTitle(line_n)
        if url_n not in sql.mysql_query(myConnection, "links", "site"):
            sql.mysql_write_site(myConnection, url_n, title)
        id_site = sql.mysql_get_id(myConnection, "idsite", "site", "links", url_n)
        mysql_write_new_info(sql, url_n, id_site, config["telegram"]["token"],
                             config["telegram"]["chat_id"],config["slack"]["url"])
    

config = get_config("/var/crawl_canhme/setting")
sql = mysql.mysql(config["mysql"]["hostname"], config["mysql"]["username"],
                  config["mysql"]["password"], config["mysql"]["database"])
myConnection = sql.connection()
NH(config["sites"]["url_nh"])

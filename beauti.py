import requests
from bs4 import BeautifulSoup


def getLink(url):
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "lxml")
    datas = soup.find_all(class_="entry-title")
    return datas

def getUser(line):
    user_name = line.find\
    (class_="wpd-comment-author wcai-uname-info wcai-not-clicked").text
    return user_name

def getidComment(line):
    idCom = line.get('id')
    return idCom

def getComment(line):
    Comment = line.find(class_="wpd-comment-text")
    Comment = Comment.text.strip()
    return Comment

def getURL(line_n):
    d1 = line_n.find('a')
    url = d1.get('href').strip()
    return url

def getTitle(line_n):
    d1 = line_n.find('a')
    title = d1.string.strip()
    return title

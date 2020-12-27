#!/usr/bin/env python
#!coding=utf8
import os
import requests
from bs4 import BeautifulSoup

""" Парсим коменты и лайки на ютубе 
python --version
Python 3.6.9
"""

url = ''

# ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer"
#  ytd-comment-renderer id="comment"
# divs
#  body
#   id = main
#     id = header
#      id="header-author"
#      id = content
#      id = toolbar - лайки
#     ytd-expander id="expander"
#     ytd-comment-action-buttons-renderer

class body:
    count = 0
    autor_likes = 0
    autor_list = []
    likes_res_list = []
    def __init__(self, fileName):
        body.doc = open(fileName)
        body.soup = BeautifulSoup(doc, 'html.parser')
        self.id = id
        body.count +=1

    def get_ID(self):
        return self.id
    def size(self):
        return self.count
    def authorGet(self):
        """ Поиск авторов комента """
        res_list = []
        i = 0
        for div in divs2:
            self.autor = div.find("div", attrs={"id": "header-author"})
            self.autor_list.append(self.autor.span.get_text().strip())
            i +=1
        return self.autor_list
    
    def likesGet(self):
        """ Сколько лайков у комента? """
        i = 0
        for div in divs2:
            autor_likes = div.find("div", attrs={"id": "toolbar"})
            self.likes_res_list.append(autor_likes.span.get_text().strip())
            i +=1
        return self.likes_res_list

    def printInfo(self):
#        self.authorGet(self)
        self.authorGet()
        self.likesGet()
        i = 0
        for autor in self.autor_list:
            print("{} liks:{}".format(autor, self.likes_res_list[i]))
            i +=1
        print("Total id:{}".format(self.count))



# doc = open("../../ya.html")
fname = "in.html"
doc = open(fname)
soup = BeautifulSoup(doc, 'html.parser')
#divs1 = soup.find_all('div')
#

#divs2 = soup.find_all('div', attr={"class": "style-scope ytd-item-section-renderer"})
divs2 = soup.find('div', attrs={"id": "contents"})

a = body(fname)
a.printInfo()
i = 0
#print(divs1)
#print(divs2)

#мой тест https://youtu.be/nHOftajLSKk
#/media/maksim/577ca0be-d711-45bf-acc1-829df295b565/home/maksim/progects/py_prj/pars/klavogonki/main.py
""" Поиск авторов комента """
#================================================================================
def authorGet():
    res_list = []
    i = 0
    for div in divs2:
    #    print(div)
        autor = div.find("div", attrs={"id": "header-author"})
        res_list.append(autor.span.get_text().strip())
#        print(autor.span.get_text())
        i +=1
    return res_list
    # if div =='ytd-item-section-renderer':
    #     print(div)
    #     i +=1
""" Вывести список авторов коментов """
# for user in authorGet():
#     print(user)
# print(i)
#================================================================================


""" Сколько лайков у комента? """
#================================================================================
# def likesGet():
#     res_list = []
#     i = 0
#     for div in divs2:
#         autor = div.find("div", attrs={"id": "toolbar"})
#         res_list.append(autor.span.get_text().strip())
#         i +=1
#     return res_list
# """ вывести количество лайков у кажкого комента """
# for lik in likesGet():
#     print(lik)
# j=0
# for us in authorGet():
    
#     print("user: {}, likes:{}".format(us, likesGet()[j]))
#     j+=1
#================================================================================


# one = '1 Hello, World!!!'
# two = '2 Hello, World!!!'

# f = open('in.txt', 'w')
# f.write(one)
# f.write(two+'\n')
# f.write(one)
# f.close()

# with open('in.txt', 'r') as f:
#     for line in f:
#         print(line)

# f.close()




#for line in f:
    

# with open('in.txt', "w") as f:
#     print('Hello!')

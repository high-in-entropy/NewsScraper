# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:07:32 2019

@author: Viraj Mohile, (National Institute of Technology, Surat ['17-'21])
"""
import urllib.request
from bs4 import BeautifulSoup

def content(link):
    for i in range(len(link)):
        l = link[i].split(":")
        link[i] = l[0] + 's:' + l[1]
    content1 = []
    for i in range(len(link)):
        page = urllib.request.urlopen(link[i])
        soup = BeautifulSoup(page)
        divs = soup.find_all('div', {"class" : "Normal"})
        for div in divs:
            content1.append([])
            content1[i] = div.text
            
    return(content1)
       

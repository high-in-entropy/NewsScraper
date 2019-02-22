# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:39:54 2019

@author: Viraj Mohile, (National Institute of Technology, Surat ['17-'21])
"""
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from Content import content


for z in range(0,30):
    url = "https://timesofindia.indiatimes.com/2010/1/" + str(z + 1) + "/archivelist/year-2010,month-1,starttime-" + str(40179+z) + ".cms"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page)
    divs = soup.find_all('table', {"class" : "cnt"})

    for div in divs:
        links = div.find_all("a")

    text = [] 
    l = []

    i = 0
    for lin in links:
        l.append([])
        l[i] = lin.get("href")
        text.append([])
        text[i] = lin.text
        i = i + 1
        
    text1 = []
    l1 = []

    for i in range(3,len(text)-21):
        text1.append([])
        text1[i-3] = text[i]
        l1.append([])
        l1[i-3] = l[i]
       
    if z == 0:
        j = 0
        headings = []
        final_links = []
    

    term = "HIV"
    for i in range(len(text1)):
        words = text1[i].split()
        if term in words:
            headings.append([])
            headings[j] = text1[i]
            final_links.append([])
            final_links[j] = l1[i]
            j = j + 1
r = content(final_links)
Final_Table = pd.DataFrame(np.column_stack([headings, r, final_links]), columns = ['Headline','Content','URL'])




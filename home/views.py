from django.shortcuts import render,redirect
from django.http import JsonResponse
import datetime
from math import ceil
from home.models import table
from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
import re
import nltk
from collections import Counter
import requests
import urllib.request

import os

urllist = []


def home(request):
    return render(request,"contacts.html")

def count(request):
    url = request.GET.get('url')
    print(urllist)
    if url in urllist:
        data=table.objects.filter(url__iexact=url)
        d=data[0]
        print(d)
        return render(request,"result.html",{'result':d,'url':url,'viewed':'You have already viewed the result of this URL earlier fetching result'})
    elif url not in urllist:
        urllist.append(url)
        r = requests.get(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        body = soup.find('body').get_text()
        review = re.sub('[^a-zA-Z]', ' ', body)
        a = review.lower()
        b = a.split()

        clean_mess = [word for word in b if word not in stopwords.words('english')]
        c = " ".join(clean_mess)

        # Pass the split_it list to instance of Counter class.
        freq = Counter(clean_mess)

        # most_common() produces k frequently encountered
        # input values and their respective counts.
        most_occur = freq.most_common(10)
        words=[]
        fre=[]
        for i in most_occur:
            words.append(i[0])
            convstr= str(i[1])
            c = i[0] + '(' + convstr + ')'
            final = i[0] + ' (' + convstr + ') '
            fre.append(final)
        result = ",".join(fre)
        data=table(url=url,result=result)
        data.save()
        return render(request,"result.html",{'result':result,'url':url,'viewed':''})

# Create your views here.

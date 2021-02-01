from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
import re
import nltk
from collections import Counter

url='https://intellij-support.jetbrains.com/hc/en-us/community/posts/206159619-How-do-I-change-cursor-from-a-block-back-to-'
r=requests.get(url)
htmlcontent=r.content
soup= BeautifulSoup(htmlcontent,'html.parser')
body=soup.find('body').get_text()
review = re.sub('[^a-zA-Z]', ' ', body)
a=review.lower()
b=a.split()

clean_mess=[word for word in b if word not in stopwords.words('english')]
c=" ".join(clean_mess)



# Pass the split_it list to instance of Counter class.
Counter = Counter(clean_mess)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = Counter.most_common(10)
a=[]
b=[]
r=[]
for i in most_occur:
    a.append(i[0])
    z=str(i[1])
    b.append(z)
    c=i[0]+'('+z+')'
    r.append(c)

l=",".join(r)
print(l)

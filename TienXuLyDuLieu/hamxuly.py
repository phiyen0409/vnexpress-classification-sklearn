import re
import pandas as pd
from underthesea import word_tokenize

def clean_text(document):

    #Xóa các kí tự đơn lẻ
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    #Xóa các kí tự nháy đơn
    document=re.sub(r'\'', ' ', document)
    #Xóa các kí tự đơn lẻ ở đầu văn bản
    document = re.sub(r'^[a-zA-Z]\s+', ' ', document)
    #Xóa các kí tự đơn lẻ ở giữa văn bản
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    #Thay thế nhiều khoảng trắng đứng cạnh nhau thành 1 khoảng trắng
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    #Chuyển chữ hoa thành chữ thường
    document = document.lower()
    return document

#Tách từ dùng thư viện underthesea
def word_tokenizer(document):
    document=word_tokenize(document, format="text")
    return document

#Loại bỏ stopword
file=pd.read_csv('../TienXuLyDuLieu/vietnamese-stopwords.txt')
stopwords=[]
for i in range(0,len(file)):
    stopwords.append(str(file.values[i,0]))
def clean_stopword(document):
    sent=[]
    for word in document.split(" "):
        if (word not in stopwords) :
            if ("_" in word) or (word.isalpha() == True):
                  sent.append(word)
    return sent

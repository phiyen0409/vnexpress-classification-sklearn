import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

from TienXuLyDuLieu.hamxuly import *

data=pd.read_csv('../TienXuLyDuLieu/datavnexpress.csv')

X=data.content
y=data.label

#Tạo mảng chứ các văn bản trong data
word_data=[]
for i in range(len(data)):
    word_data.append(str(data.values[i,0]))

#Chuyển văn bản thành các vector theo tfidf
tfidfconverter = TfidfVectorizer(max_features=2000, min_df=5, max_df=0.7)
X = tfidfconverter.fit_transform(word_data).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#Tạo model dùng thuật toán Naive Bayes
model = GaussianNB()
#Train cho model
model.fit(X_train,y_train)
#Test thử model
y_pred = model.predict(X_test)
#Tính xác suất thuật toán phân lớp Naive Bayes
print(classification_report(y_test,y_pred))
print("Xác suất:",metrics.accuracy_score(y_test, y_pred))

#Lưu model thành file

# with open('vnexpress_classification', 'wb') as picklefile:
#     pickle.dump(model,picklefile)
#     picklefile.close()

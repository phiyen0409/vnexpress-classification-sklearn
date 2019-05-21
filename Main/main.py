import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from TienXuLyDuLieu.hamxuly import clean_stopword,clean_text,word_tokenizer
import pandas as pd

def classification(path):
    with open(path,'r',encoding='utf8') as f:
        text=f.readline()
    f.close()
    text=clean_text(text)
    text=word_tokenizer(text)
    text=clean_stopword(text)
    content=[]
    content.append(" ".join(text))

    word_data=[]
    data=pd.read_csv('../TienXuLyDuLieu/datavnexpress.csv')
    for i in range(len(data)):
        word_data.append(str(data.values[i,0]))

    tfidfconverter = TfidfVectorizer(max_features=2000, min_df=5, max_df=0.7)
    tfidfconverter.fit_transform(word_data).toarray()



    with open('../Text_Classification/vnexpress_classification', 'rb') as training_model:
        model = pickle.load(training_model)
        content=tfidfconverter.transform(content).toarray()
        pred=model.predict(content)
        print(pred)
    training_model.close()

if __name__== "__main__":
    #Phân lớp văn bản được thêm vào
    classification('./news.csv')

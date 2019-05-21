from TienXuLyDuLieu.hamxuly import clean_text, word_tokenizer, clean_stopword
import pandas as pd
import csv



data=pd.read_csv('../VnExpressCrawler/document.csv')


with open('datavnexpress.csv', 'w', encoding="utf8") as csvFile:
    writer = csv.writer(csvFile)
    row=["content","label"]
    writer.writerow(row)
csvFile.close()

for i in range(0,5):
    document=str(data.values[i,0]) + " " + str(data.values[i,2])
    document=clean_text(document)
    document=word_tokenizer(document)
    document=clean_stopword(document)
    row = []
    row.append(" ".join(document))
    row.append(str(data.values[i,1]))
    with open('datavnexpress.csv', 'a', encoding="utf8") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()


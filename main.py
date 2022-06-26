from difflib import SequenceMatcher
import pandas as pd


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


df = pd.read_excel('VocabStyle.xlsx', index_col=0)

df_ = df.iloc[3638:]

words = df_.iloc[:, 1]

words_list = words.to_list()
len_words_list = len(words_list)

for i in range(len_words_list):
    for j in range(i + 1, len_words_list):
        similarity = similar(words_list[i], words_list[j])
        if similarity > .7:
            print(str(similarity), words_list[i], "-", words_list[j], "-", str(i+3640), "-", str(j+3640))

print('Processed')

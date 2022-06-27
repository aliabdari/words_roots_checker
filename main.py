from difflib import SequenceMatcher
import pandas as pd


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


df = pd.read_excel('VocabStyle.xlsx', index_col=0)

initial_xlsx_index = 1479
ending_xlsx_index = 1938

df_ = df.iloc[initial_xlsx_index:ending_xlsx_index]

words = df_.iloc[:, 1]

words_list = words.to_list()
len_words_list = len(words_list)

for i in range(len_words_list):
    for j in range(i + 1, len_words_list):
        similarity = similar(words_list[i], words_list[j])
        if similarity > .7:
            print(words_list[i], "-", words_list[j], "-", str(i + initial_xlsx_index + 2), "-",
                  str(j + initial_xlsx_index + 2))

print('Processed')

import pandas as pd
import MeCab
from collections import Counter

file_path = 'Query (10).csv'
df = pd.read_csv(file_path)

mecab = MeCab.Tagger("-Ochasen")

def extract_nouns(text):
    if pd.isnull(text):
        return []
    mecab.parse('')  
    parsed = mecab.parse(text)
    nouns = [
        line.split("\t")[0]
        for line in parsed.splitlines()
        if "\t" in line and "名詞" in line.split("\t")[1]
    ]
    return nouns

nouns_counter = Counter()

columns_to_analyze = ['ラベル', '説明文']
for column in columns_to_analyze:
    if column in df.columns:
        for text in df[column]:
            nouns = extract_nouns(text)
            nouns_counter.update(nouns)

nouns_df = pd.DataFrame(nouns_counter.most_common(), columns=['Word', 'Count'])
output_file = 'word_count水かつ体験.csv'
nouns_df.to_csv(output_file, index=False, encoding='utf-8')

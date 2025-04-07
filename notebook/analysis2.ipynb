import pandas as pd
from collections import Counter
import MeCab

file_path = 'Query (9).csv'
data = pd.read_csv(file_path)

keywords = ["感覚", "知覚", "感", "覚", "運動", "動"]
pattern = '|'.join(keywords)

water_data = data[
    data['説明文'].str.contains(pattern, na=False) |
    data['ラベル'].str.contains(pattern, na=False)
]

mecab = MeCab.Tagger("-Ochasen")

def get_nouns(text):
    mecab.parse('')  # 初期化
    node = mecab.parseToNode(text)
    words = []
    while node:
        if node.feature.split(",")[0] == "名詞":
            words.append(node.surface)
        node = node.next
    return words

texts = water_data['ラベル'].fillna('') + ' ' + water_data['説明文'].fillna('')
texts = texts.apply(get_nouns)

word_count = Counter()
for text in texts:
    word_count.update(text)

for keyword in keywords:
    word_count.pop(keyword, None)

sorted_word_count = word_count.most_common()
word_count_df = pd.DataFrame(sorted_word_count, columns=['Word', 'Count'])
word_count_df.to_csv('word_count体験.csv', index=False, encoding='utf-8')

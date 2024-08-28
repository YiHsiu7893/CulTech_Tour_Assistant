"""
Ref:
https://blog.csdn.net/asialee_bird/article/details/94208759
https://vocus.cc/article/647dcbf7fd89780001afdb56
"""
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from RAG import llm_call
import jieba
jieba.load_userdict("userdict.txt")


# Define stopwords set.
stopwords = set()
with open('stopwords.txt','r', encoding='utf-8') as file:
    for stopword in file:
        stopwords.add(stopword.strip('\n'))


# func: pre-processing, including tokenization and stopwords removal
def tokenizer(text):
    # Tokenization
    words = jieba.cut(text, cut_all=False)
    # Stopwords removal
    words_list = [word for word in words if word not in stopwords]

    return " ".join(words_list)


df = pd.read_csv("./Knowledge/peigui_hall.csv", encoding="big5")
df["問題"] = df["問題"].apply(lambda text: tokenizer(text))
#print(df)

# Extract features with TF-IDF.
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df["問題"])
#print(tfidf_matrix)

# Show the full TF-IDF feature matrix.
dense_tfidf_matrix = tfidf_matrix.todense()
feature_names = tfidf_vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(dense_tfidf_matrix, columns=feature_names)
#print(feature_names)


def model_call(query):
    # Process the user's query.
    query_tk = tokenizer(query)
    query_vec = tfidf_vectorizer.transform([query_tk])

    # Computes the sentence similarity between the query and df["問題"].
    sims = cosine_similarity(query_vec, tfidf_matrix).flatten()
    #print(simis)

    # Find the best matched 問題.
    best_index = np.argmax(sims)
    best_score = sims[best_index]

    threshold = 0.6
    if best_score >= threshold:
        return df["回答"][best_index]
    else:
        return llm_call(query)


if __name__ == '__main__':
    query = "參觀培桂堂要預約嗎?"
    print(model_call(query))
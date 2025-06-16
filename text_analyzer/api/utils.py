from collections import Counter, namedtuple
import os, heapq
from math import log

from math import log

def calculate_tf(text):
    words = text.lower().split()
    total_words = len(words)
    word_counts = Counter(words)
    tf_scores = {word: count / total_words for word, count in word_counts.items()}
    return tf_scores

def calculate_idf(documents_texts):
    import math
    N = len(documents_texts)
    idf_scores = {}
    all_words = set(word for text in documents_texts for word in text.lower().split())
    for word in all_words:
        containing_docs = sum(1 for text in documents_texts if word in text.lower().split())
        idf_scores[word] = log(N / (1 + containing_docs))  # добавлено +1 чтобы избежать деления на 0
    return idf_scores

def calculate_statistics(document, all_documents):
    document_text = extract_text_from_txt(document)
    documents_text = [extract_text_from_txt(doc) for doc in all_documents]

    tf_scores = calculate_tf(document_text)
    idf_scores = calculate_idf(documents_text)

    statistics = {}
    for word in tf_scores:
        tf = tf_scores[word]
        idf = idf_scores.get(word, 0.0)
        tf_idf = tf * idf
        statistics[word] = {'tf': tf, 'idf': idf, 'tf_idf': tf_idf}
    return statistics


def extract_text_from_txt(document):
    with document.file.open('rb') as f:
        return f.read().decode('utf-8')

def calculate_tf_idf_for_document(document, all_documents):
    from sklearn.feature_extraction.text import TfidfVectorizer

    all_documents = list(all_documents)  # Преобразуем QuerySet в список

    documents_text = [extract_text_from_txt(doc) for doc in all_documents]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents_text)

    index = all_documents.index(document)
    feature_names = vectorizer.get_feature_names_out()
    doc_vector = tfidf_matrix[index]

    tfidf_scores = dict(zip(feature_names, doc_vector.toarray()[0]))
    tfidf_scores = {k: v for k, v in sorted(tfidf_scores.items(), key=lambda item: item[1], reverse=True)}

    return tfidf_scores


def calculate_tf_for_collection(documents):
    from sklearn.feature_extraction.text import TfidfVectorizer

    documents_text = [extract_text_from_txt(doc) for doc in documents]

    vectorizer = TfidfVectorizer(
        token_pattern=r"(?u)\b\w+\b",  # разрешает любые слова, включая односимвольные
        lowercase=True,
        stop_words=None
    )
    tfidf_matrix = vectorizer.fit_transform(documents_text)

    summed_vector = tfidf_matrix.sum(axis=0)
    feature_names = vectorizer.get_feature_names_out()
    scores = dict(zip(feature_names, summed_vector.tolist()[0]))
    scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}

    return scores

class HuffmanNode(namedtuple("HuffmanNode", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [HuffmanNode(char, freq, None, None) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def build_huffman_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", codebook)
        build_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encode(text):
    tree = build_huffman_tree(text)
    codebook = build_huffman_codes(tree)
    encoded_text = ''.join(codebook[char] for char in text)
    return encoded_text

def calculate_statistics_for_collection(documents):
    total_documents = len(documents)
    term_document_frequency = {}

    # Преобразуем объекты Document в текст
    document_texts = [extract_text_from_txt(doc) for doc in documents]

    # Подсчёт DF
    for text in document_texts:
        words = set(text.split())
        for word in words:
            term_document_frequency[word] = term_document_frequency.get(word, 0) + 1

    # Подсчёт общей частоты всех слов
    total_terms = []
    for text in document_texts:
        total_terms.extend(text.split())
    total_term_count = len(total_terms)
    term_frequencies = Counter(total_terms)

    stats = {}
    for term, count in term_frequencies.items():
        tf = count / total_term_count
        df = term_document_frequency.get(term, 0)
        idf = log((1 + total_documents) / (1 + df)) + 1  # сглаженный IDF
        tf_idf = tf * idf

        stats[term] = {
            "tf": tf,
            "idf": idf,
            "tf_idf": tf_idf
        }

    return stats




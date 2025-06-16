from collections import Counter, namedtuple
import os, heapq

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



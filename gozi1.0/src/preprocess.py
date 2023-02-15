import re
import string
def preprocess_text(text):
    """
    对文本进行预处理，去除标点符号，空格，换行符等
    :param text: 待处理文本
    :return: 处理后的文本
    """
    text = text.lower() # 将文本转换为小写
    text = re.sub(r'[^\w\s]','',text) # 去除标点符号
    text = re.sub(r'\s+',' ',text) # 去除多余的空格
    text = text.strip() # 去除首尾空格
    return text
if __name__ == '__main__':
    text = 'Hello, World! How are you?'
    print(preprocess_text(text))
def tokenize_text(text):
    """
    将文本分割成单词
    :param text: 待处理文本
    :return: 单词列表
    """
    tokens = text.split(' ')
    return tokens
def remove_stopwords(tokens):
    """
    去除停用词
    :param tokens: 单词列表
    :return: 去除停用词后的单词列表
    """
    stopwords = ['the', 'a', 'an', 'in', 'on', 'at', 'of', 'for']
    filtered_tokens = [token for token in tokens if token not in stopwords]
    return filtered_tokens
if __name__ == '__main__':
    text = 'Hello, World! How are you?'
    tokens = tokenize_text(text)
    print(tokens)
    filtered_tokens = remove_stopwords(tokens)
    print(filtered_tokens)
def remove_punctuation(tokens):
    """
    去除标点符号
    :param tokens: 单词列表
    :return: 去除标点符号后的单词列表
    """
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    return stripped
def stem_words(tokens):
    """
    将单词进行词干提取
    :param tokens: 单词列表
    :return: 词干提取后的单词列表
    """
    stemmer = PorterStemmer()
    stemmed = [stemmer.stem(word) for word in tokens]
    return stemmed
if __name__ == '__main__':
    text = 'Hello, World! How are you?'
    tokens = tokenize_text(text)
    print(tokens)
    stripped = remove_punctuation(tokens)
    print(stripped)
    stemmed = stem_words(stripped)
    print(stemmed)
	def lemmatize_verbs(tokens):
    """
    将单词进行词形还原
    :param tokens: 单词列表
    :return: 词形还原后的单词列表
    """
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word, pos='v') for word in tokens]
    return lemmas
if __name__ == '__main__':
    text = 'Hello, World! How are you?'
    tokens = tokenize_text(text)
    print(tokens)
    filtered_tokens = remove_stopwords(tokens)
    print(filtered_tokens)
    stripped = remove_punctuation(filtered_tokens)
    print(stripped)
    stemmed = stem_words(stripped)
    print(stemmed)
    lemmas = lemmatize_verbs(stemmed)
    print(lemmas)
def remove_non_ascii(words):
    """
    去除非ASCII字符
    :param words: 单词列表
    :return: 去除非ASCII字符后的单词列表
    """
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words
if __name__ == '__main__':
    text = 'Hello, World! How are you?'
    tokens = tokenize_text(text)
    print(tokens)
    filtered_tokens = remove_stopwords(tokens)
    print(filtered_tokens)
    stripped = remove_punctuation(filtered_tokens)
    print(stripped)
    stemmed = stem_words(stripped)
    print(stemmed)
    lemmas = lemmatize_verbs(stemmed)
    print(lemmas)
    ascii_words = remove_non_ascii(lemmas)
    print(ascii_words)
	def normalize(words):
    """
    将单词转换为小写
    :param words: 单词列表
    :return: 转换为小写后的单词列表
    """
    words = [word.lower() for word in words]
    return words
if __name__ == '__main__':
    text = 'Hello, World! How are you?'
    tokens = tokenize_text(text)
    print(tokens)
    filtered_tokens = remove_stopwords(tokens)
    print(filtered_tokens)
    stripped = remove_punctuation(filtered_tokens)
    print(stripped)
    stemmed = stem_words(stripped)
    print(stemmed)
    lemmas = lemmatize_verbs(stemmed)
    print(lemmas)
    ascii_words = remove_non_ascii(lemmas)
    print(ascii_words)
    normalized = normalize(ascii_words)
    print(normalized)
	def preprocess_text(text):
    """
    对文本进行预处理
    :param text: 文本
    :return: 预处理后的文本
    """
    tokens = tokenize_text(text)
    filtered_tokens = remove_stopwords(tokens)
    stripped = remove_punctuation(filtered_tokens)
    stemmed = stem_words(stripped)
    lemmas = lemmatize_verbs(stemmed)
    ascii_words = remove_non_ascii(lemmas)
    normalized = normalize(ascii_words)
    preprocessed_text = ' '.join(normalized)
    return preprocessed_text
if __name__ == '__main__':
    text = 'Hello, World! How are you?'
    preprocessed_text = preprocess_text(text)
    print(preprocessed_text)
from tensorflow.keras.datasets import reuters
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)
word_index = reuters.get_word_index()
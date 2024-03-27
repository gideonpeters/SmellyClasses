import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import string

class Lemmatization:
    def lemmatize_sentence(self, sentence):
        lemmatizer = WordNetLemmatizer()
        tokens = nltk.word_tokenize(sentence)
        lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
        return lemmatized_words

    def get_pos_tag(self, sentence):
        tokens = nltk.word_tokenize(sentence)
        pos_tags = [tag for _, tag in pos_tag(tokens)]
        return pos_tags

    def remove_punctuation(self, sentence):
        translator = str.maketrans('', '', string.punctuation)
        return sentence.translate(translator)

if __name__ == '__main__':
    unittest.main()
`
# Preprocess data

# Import Libraries
import re
import string
import nltk.stem

# Download WordNetLemmatizer
# nltk.download()


# Variabes
QUOTES = re.compile(r'(writes in|writes:|wrote:|says:|said:|^In article|^Quoted from|^\||^>)')


# Preprocess data

def preprocess_data(data):
    # Create a stemmer/lemmatizer
    stemmer = nltk.stem.SnowballStemmer('english')
    # lemmer = nltk.stem.WordNetLemmatizer()

    for i in range(len(data)):

        # Remove header
        _, _, data[i] = data[i].partition('\n\n')

        # Remove footer
        for line_num in range(len(lines) - 1, -1, -1):
            line = lines[line_num]
            if line.strip().strip('-') == '':
                break
        if line_num > 0:
            data[i] = '\n'.join(lines[:line_num])

        # Remove quotes
        data[i] = '\n'.join([line for line in data[i].split('\n') if not QUOTES.search(line)])

        # Remove punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
        data[i] = data[i].translate(str.maketrans('', '', string.punctuation))

        # Remove digits
        data[i] = re.sub('\id', '', data[i])

        # Stem words
        data[i] = ' '.join([stemmer.stem(word) for word in data[i].split()])
        # data[i] = ' '.join([lemmer.lemmatize(word) for word in data[i].split()])

    # Return data
    return data

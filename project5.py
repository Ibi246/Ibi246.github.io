"""
Text Processing and Word Frequency Analysis

Original file is located at
    https://www.gutenberg.org/cache/epub/11/pg11-images.html

Title: Alice's Adventures in Wonderland
Author: Lewis Carroll
Aprox word count: 27,500 words
I chose this text because it was an easily accesible book from the website, I had a good understanding of the story so I could analyze the results at the end, and it was one of the best class-friendly texts I could find.
"""


""" 
First, we have to import SpaCy, which is a powerful library for natural language processing (NLP) in Python. 
We will use it to perform advanced text processing tasks such as tokenization, lemmatization, and stop word removal.
If the download of spaCy works, the user will know when the function prints "spaCy installed successfully!" Otherwise, it will print an error message.
"""
import pip
import spacy
nlp = spacy.load('en_core_web_sm')
print("spaCy installed successfully!")

import operator

"""
The fetch text function takes the url provided and fetches the text data. It also implements a caching mechanism to avoid redundant network requests. If the text is successfully fetched, it will print "✅ Text fetched." Otherwise, it will print "❌ Failed to fetch text." along with the error message.
The raw_url is a string variable that contains the URL of the text file we want to fetch. In this case, it points to an excerpt from Jane Austen's Pride and Prejudice hosted on GitHub Gist.
The return values are the text data fetched from the URL, or an empty string if the fetch operation fails. The function also handles exceptions that may occur during the fetching process and provides feedback to the user.
This function collects data, stores the information in a local cache, and then prints a message depending on the outcome of the fetch.
"""
# Function to fetch data
def fetch_text(raw_url):
  import requests
  from pathlib import Path
  import hashlib

  CACHE_DIR = Path("cs_110_content/text_cache")
  CACHE_DIR.mkdir(parents=True, exist_ok=True)
  """The _url_to_filename function takes a URL as input and generates a unique filename for caching the fetched text. It uses the SHA-1 hashing algorithm to create a hash of the URL, which ensures that each URL corresponds to a unique cache file. The resulting filename is a combination of the first 12 characters of the hash and the ".txt" extension, stored in the specified cache directory."
  The paramaters are the URL string that we want to fetch. The return value is a Path object representing the file path where the fetched text will be cached. This function helps in organizing and managing cached files based on their corresponding URLs.
  The return values is the file path for the cached text, which is generated based on the URL. This allows the program to store and retrieve cached text efficiently, avoiding redundant network requests for the same URL in future fetches.
  This function is a helper function that provides a short and reproducible filename.
  """
  def _url_to_filename(url):
    url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
    return CACHE_DIR / f"{url_hash}.txt"

  cache_path = _url_to_filename(raw_url)

  SUCCESS_MSG = "✅ Text fetched."
  FAILURE_MSG = "❌ Failed to fetch text."
  try:
    """
    This function checks if the file exists or if it is absent, the function requests the text from the URL, saves it to the cache, and then reads and returns the text. If the file already exists in the cache, it simply reads and returns the cached text. This approach optimizes performance by avoiding unnecessary network requests for previously fetched URLs.
    """
    if not cache_path.exists():
      response = requests.get(raw_url, timeout=10)
      response.raise_for_status()
      text_data = response.text
      cache_path.write_text(text_data, encoding="utf-8")
    print(SUCCESS_MSG)
    return cache_path.read_text(encoding="utf-8")

  except Exception as e:
    print(FAILURE_MSG)
    print(f"Error: {e}")
    return ""

# Save the URL in a variable
ALICE_IN_WONDERLAND_URL = "https://www.gutenberg.org/cache/epub/11/pg11.txt"

# Fetch the text
alice_in_wonderland_text = fetch_text(ALICE_IN_WONDERLAND_URL)

"""
The print_text_stats function computes and prints basic statistics about the text
The parameter is the text string where the input will be computed
There are no return functions
The function calculates the number of characters, lines, and words in the given text. It first counts the total number of characters using the len() function. Then, it splits the text into lines using splitlines() and counts the number of lines. Finally, it iterates through each line, splits it into words, and counts the total number of words. The results are printed in a formatted manner.
"""
# Statistics about the data
def print_text_stats(text):
  num_chars = len(text)

  lines = text.splitlines()
  num_lines = len(lines)

  num_words = 0
  for line in lines:
    words_in_line = line.split()
    num_words_in_line = len(words_in_line)
    num_words += num_words_in_line

  print(f"Number of characters: {num_chars}")
  print(f"Number of lines: {num_lines}")
  print(f"Number of words: {num_words}")

"""
The get_word_counts function splits the text into lines and extracts tokens to count in a dictionary
The parameter is the text string where the input is used and analyzed. 
The return function maps each lowercase word to its frequency and returns with nothing if the text has no words to count.

"""
# Function to get word counts
def get_word_counts(text):
  word_counts = {}
  lines = text.splitlines()
  for line in lines:
    words = line.split()
    for word in words:
      word = word.lower()
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
  return word_counts


# this is a test print
print_text_stats(alice_in_wonderland_text)

# get the word counts
word_counts = get_word_counts(alice_in_wonderland_text)
print(word_counts)

"""

Using spaCy for advanced text processing

"""

import spacy

nlp = spacy.load('en_core_web_sm')


"""
The word_tokenization_normalization function loads the text into the spaCy model and filters out unneeded information
The parameter is the text string used from the pride_prejudice_text variable
The return value is a list of lemmatized word strings.
The function will not return words that are stop words, punctuation, numbers, or have a length of 2 or less. The function first converts the input text to lowercase and then processes it using the spaCy model. It iterates through each token in the processed document and applies the specified filtering criteria. If a token meets the criteria, it is lemmatized and added to the list of normalized words, which is returned at the end.
"""
def word_tokenization_normalization(text):

    text = text.lower() # lowercase
    doc = nlp(text)     # loading text into model

    words_normalized = []
    for word in doc:
        if word.text != '\n' \
        and not word.is_stop \
        and not word.is_punct \
        and not word.like_num \
        and len(word.text.strip()) > 2:
            word_lemmatized = str(word.lemma_)
            words_normalized.append(word_lemmatized)

    return words_normalized

"""
The word_count function takes a list of words and puts the words in the dictionary into a counted list.
The parameter of the function is the word_list, which does as it sounds, listing the words to be counted
The return value is a dictionary where the keys are the unique words from the input list and the values are the corresponding counts of how many times each word appears in the list. 
The function iterates through each word in the input list, converts it to lowercase for normalization, and updates the count in the word_counts dictionary. If a word is already present in the dictionary, its count is incremented; otherwise, it is added to the dictionary with an initial count of 1. Finally, the function returns the word_counts dictionary containing the frequency of each word.
"""
def word_count(word_list):
    word_counts = {}
    for word in word_list:
      word = word.lower()
      if word in word_counts:
        word_counts[word] += 1
      else:
        word_counts[word] = 1
    return word_counts

"""
The print_top_15_frequent_words function sorts the word_counts function by the frequency of the words in descending order and then prints the top 15 words
The parameters of the function are the word_counts dictionary that contains the frequency of each word.
There is no return value
The main function of this code is to take the word_counts function and prints the 15 most frequent words.
"""
def print_top_15_frequent_words(word_counts):
    sorted_word_counts = dict(sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True))
    top_15_words = list(sorted_word_counts.items())[:15]  # Get the top 15 words and counts
    for word, count in top_15_words:
        print(f"{word}: {count}")


doc_tokenized = word_tokenization_normalization(alice_in_wonderland_text)

print(doc_tokenized)

new_counts = word_count(doc_tokenized)
print(new_counts)

print_top_15_frequent_words(new_counts)

"""
The top 15 words are: say, alice, think, go, little, know, look, begin, like, come, project, gutenbergm work, thing, and queen
While you can get an idea of the story from the top 15 words, especially while there are no stop words, there are still many words that are common in any story and give little insignt into the story of Alice in Wonderland.
I don't know how to get rid of the gutenburg trademark, and it's said so much on the website link I provided that it made its way into the top 15 words unfortunatley.
I feel like if we ignore the gutenburg trademark, we can get a general sense of the theme of the story and the language used; with the top word being say, the language is used in a more conversational way, which is fitting for the story. With "alice" being the second most common word, it is clear that the story is about Alice, and with the word think being the third most common word, it suggests that there may be a lot of introspection or thought processes involved in the story. 
The word frequencies don't fully capture the essense and childlike wonder of the story, but it still does give good insight as said above. 
"""
import spacy
from collections import Counter
# List of common English verbs (expand as needed)
"""
Next I'm going to create a set of common English verbs that are used so that Python has something to go off of for analysis. 
"""
common_verbs = {
    "be", "have", "do", "say", "get", "make", "go", "know", "take", "see", "come", "think", "look", "want", "give",
    "use", "find", "tell", "ask", "work", "seem", "feel", "try", "leave", "call", "put", "keep", "let", "begin", "help",
    "talk", "turn", "start", "show", "hear", "play", "run", "move", "live", "believe", "bring", "write", "sit", "stand",
    "lose", "pay", "meet", "include", "continue", "set", "learn", "change", "lead", "understand", "watch", "follow",
    "stop", "create", "speak", "read", "allow", "add", "spend", "grow", "open", "walk", "win", "offer", "remember",
    "love", "consider", "appear", "buy", "wait", "serve", "die", "send", "expect", "build", "stay", "fall", "cut",
    "reach", "kill", "remain"
}

"""
Next I'm going to create a function to count the verbs provided as examples used in the text.
The print_top_15_verbs function takes the text, removes punctuation, and counts the frequency of common verbs. It then prints the top 15 most frequent verbs along with their counts.
The parameter of the function is the text string that we want to analyze for verb frequency.
The return value is a printed list of the top 15 most frequent verbs in the text, along with their corresponding counts. The function processes the input text by removing punctuation and converting it to lowercase, then filters for words that are in the predefined set of common verbs. 
It uses the Counter class from the collections module to count the frequency of each verb and prints the results in a formatted manner.

"""
from collections import Counter
import string

def print_top_15_verbs(text):
    # Remove punctuation and lowercase the text
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    # Filter for words that are in the common verbs set
    verbs = [word for word in words if word in common_verbs]
    # Count and print the top 15
    most_common = Counter(verbs).most_common(15)
    for verb, freq in most_common:
        print(f"{verb}: {freq}")

#Call the function to print the top 15 verbs in the text
print_top_15_verbs(alice_in_wonderland_text)
"""
I was interested to see how many of the top 15 words were verbs, and I wanted to see which verbs were used the most. Surprisingly, there were a lot of verbs used in the overal top 15 words in the story. 
Words like "say," "go," "know," "come," "work," and "think" were all in the top 15 words, and they are all verbs. This suggests that the story is quite action-oriented and involves a lot of dialogue and movement.
"""
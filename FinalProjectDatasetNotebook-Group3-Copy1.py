
# coding: utf-8

# ## Group 3: Twitter API Dataset for Cyberbullying
# 
# We will use Python-Twitter library to grab tweets through Twitter API
# Total = 800 tweets (for now) we will put manually in a csv.
# **Phrases** gave us more context than the words alone, which initially gave us more noise.
# 
# Similar to Twython, Python-Twitter only takes one search at a time - so there are around 21 cells. However, the good thing is that there is no 15 min rate limit and you can look up usernames, tweets as many times as you want. It feels like a tedious process to search one-by-one, but was really the only way of getting the phrases and keywords we wanted.

# In[1]:


#Installing another twitter api library, python-twitter
get_ipython().system('pip install python-twitter')


# In[2]:


#Importing packages and libraries
import twitter
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize


# In[3]:


#Putting credentials 
api = twitter.Api(consumer_key="NRStTXhC2HqBvSv55XXO9sxm5",
  consumer_secret="H1jky2hVkgBSzQOVMo0IdmAepZ0wnAldJVGm3QWjjqTQTY8hkf",
  access_token_key="955970115576717312-IUAuXEeKIuVxTz9rNm561443N5Gm9sw",
  access_token_secret="SCf7PPj3tgFpgXb47nzHlRNRpgH8kEs1i2prLZPkZBExQ")


# In[4]:


#Verifying credentials 
print(api.VerifyCredentials())


# In[5]:


#Attempting to strip as much emojis as possible by pattern
import re

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"
                           \U0001f914  # flags (iOS)
                           "]+", flags=re.UNICODE)
print(emoji_pattern)


# search = api.GetSearch("coming out", count=50)
# for t in search:
#     tweets = t.text
#     tweets = re.sub(r"http\S+", "", tweets)
#     tweets = tweets.replace("…","")
#     tweets = tweets.strip()
#     sentences = sent_tokenize(tweets.replace('\n',' '))
#     clean_words = [word for word in sentences if word not in set(string.punctuation)]
#     characters_to_remove = ["''",'``','...']
#     clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
#     characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
#     clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
#     print(clean_words)

# In[9]:


statuses = api.GetUserTimeline(screen_name="@realDonaldTrump", count=100)
print([s.text for s in statuses])


# In[50]:


search = api.GetSearch("@realDonaldTrump", count=100)
for t in search:
    tweets = t.text
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
    print(clean_words)


# In[57]:


search = api.GetSearch("fuck you", count=50)
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
    print(clean_words)


# In[52]:


search = api.GetSearch("kys", lang='en', count=50)
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
    print(clean_words)


# In[54]:


search = api.GetSearch("you piece of shit", count=50)
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
    print(clean_words)


# In[63]:


search = api.GetSearch("you are a pussy", count=50)
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]
    print(clean_words)


# In[71]:


#another attempt at taking out emojis
import re

# http://stackoverflow.com/a/13752628/6762004
RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

def strip_emoji(text):
    return RE_EMOJI.sub(r'', text)

print(strip_emoji('🙄🤔'))


# In[75]:


dataset = []
search = api.GetSearch("you are an asshole", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    strip_emoji(tweets)
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[76]:


search = api.GetSearch("soy boy", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    strip_emoji(tweets)
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[14]:


search = api.GetSearch("you are a worthless piece of shit", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[15]:


search = api.GetSearch("nobody cares about you", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[19]:


search = api.GetSearch("ugly freak", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[36]:


search = api.GetSearch("you are a dumbass", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[79]:


dataset = []
search = api.GetSearch("fucking cunt", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    strip_emoji(tweets)
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[82]:


search = api.GetSearch("you are a nigger", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    strip_emoji(tweets)
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[83]:


search = api.GetSearch("what a fag", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    strip_emoji(tweets)
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[85]:


search = api.GetSearch("you are a fat slut", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    strip_emoji(tweets)
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


# In[86]:


search = api.GetSearch("you are a retard", count=50) # Replace happy with your search
for t in search:
    tweets = t.text.lower()
    tweets = re.sub(r"http\S+", "", tweets)
    tweets = tweets.replace("…","")
    tweets = tweets.strip()
    strip_emoji(tweets)
    sentences = sent_tokenize(tweets.replace('\n',' '))
    clean_words = [word for word in sentences if word not in set(string.punctuation)]
    characters_to_remove = ["''",'``','...']
    clean_words = [word for word in clean_words if word not in set(characters_to_remove)]
    characters_to_remove2 = [word for word in clean_words if any(letter in sentences for letter in '\\')]
    clean_words = [word for word in clean_words if word not in set(characters_to_remove2)]

    print(clean_words)


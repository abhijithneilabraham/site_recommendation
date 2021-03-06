import requests 
from bs4 import BeautifulSoup 
import re
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
import random
from rake_nltk import Rake
import spacy

from spacy_wordnet.wordnet_annotator import WordnetAnnotator 
stop_words = set(stopwords.words('english'))

nlp = spacy.load('en')
nlp.add_pipe(WordnetAnnotator(nlp.lang), after='tagger')

lemmatizer = WordNetLemmatizer()
lem=lemmatizer.lemmatize

class Crawler():

    
    def get_links(self,soup,high_level_url): #get sub urls of a given url
        links={high_level_url:[]}
        for link in soup.find_all(attrs={'href': re.compile("http")}):
            links[high_level_url].append(link.get('href'))
        return links
        
    def get_keywords(self,url): #get keywords from a given url
        wordlist = [] 
        source_code = requests.get(url).text 
        soup = BeautifulSoup(source_code, 'html.parser') 
        for each_text in soup.findAll(): 
            content = each_text.text.lower() 
            r = Rake()
            r.extract_keywords_from_text(content)
            words = list(r.get_word_degrees().keys())
            wordlist+=[lem(i) for i in words if i not in stop_words and i.isalnum()] #lemmatizing, removing stopwords and cleaning non alphanumeric characters

        site_keywords=wordlist
        return site_keywords
    def get_traffic(self): #random number generator to get traffic on a website
        return [random.randint(0, 30)]
    
    def get_synonyms(self,word): #get synonyms for a word to add to the list of words
        token = nlp(word)[0]
        synobj=token._.wordnet.synsets()
        synonyms=list(set([i.lemmas()[0].name().lower() for i in synobj]))
        return synonyms
    
    def crawl(self,url): #crawl a given url and its sub urls and get keywords, returns a string of bag of words and synonyms
        source_code = requests.get(url).text 
        soup = BeautifulSoup(source_code, 'html.parser') 
        url_maps=self.get_links(soup, url)
        keywords=self.get_keywords(url)
        for sub_urls in url_maps.values():
            for sub_url in sub_urls:
                print("crawling website:",sub_url)
                try:
                    keywords+=self.get_keywords(sub_url)
                except not KeyboardInterrupt:
                    continue
        bulk_keywords=[]
        for kwd in keywords:
            bulk_keywords+=self.get_synonyms(kwd)     
        bulk_keywords=list(set(bulk_keywords))
        bag_of_words=' '.join(bulk_keywords)
        return [bag_of_words]
        
        
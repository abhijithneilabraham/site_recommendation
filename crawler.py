import requests from bs4 import BeautifulSoup import operator import refrom collections import Counter from nltk.stem import WordNetLemmatizer from nltk.corpus import stopwordsimport jsonimport osstop_words = set(stopwords.words('english'))lemmatizer = WordNetLemmatizer()lem=lemmatizer.lemmatize  def del_dump(filepath): #if json dump exists, remove the dump    if os.path.isfile(filepath):        os.remove(filepath)        def create_json_dump(filepath,data): #create a json dump with given data mappings    del_dump(filepath)    with open(filepath, "w") as write_file:        json.dump(data, write_file)    # Function removes any unwanted symbols def clean_wordlist(wordlist):     clean_list =[]     for word in wordlist:         symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '                for i in range (0, len(symbols)):             word = word.replace(symbols[i], '')         if len(word) > 0:             clean_list.append(word)     return list(set(clean_list))def get_links(soup,high_level_url):    links={high_level_url:[]}    for link in soup.find_all(attrs={'href': re.compile("http")}):        links[high_level_url].append(link.get('href'))    return links    def get_keywords(url):     # empty list to store the contents of      # the website fetched from our web-crawler     wordlist = []     source_code = requests.get(url).text     soup = BeautifulSoup(source_code, 'html.parser')     for each_text in soup.findAll():         content = each_text.text         words = content.lower().split()         words=[lem(i) for i in words if i not in stop_words and i.isalnum()] #lemmatizing, removing stopwords and cleaning non alphanumeric characters        for each_word in words:             wordlist.append(each_word)     site_keywords=clean_wordlist(wordlist)     return site_keywordsdef crawl(url):    source_code = requests.get(url).text     soup = BeautifulSoup(source_code, 'html.parser')     url_maps=get_links(soup, url)    create_json_dump('url_maps.json', url_maps)    keyword_maps={url:get_keywords(url)}    for sub_urls in url_maps.values():        for sub_url in sub_urls:            print(sub_url)            try:                keyword_maps[sub_url]=get_keywords(sub_url)            except not KeyboardInterrupt:                continue    create_json_dump('url_keywords.json', keyword_maps)    
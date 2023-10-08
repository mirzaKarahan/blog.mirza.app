import os,uuid,re
import time
from topic import Topic
from dotenv import load_dotenv
import openai
from slugify import slugify
load_dotenv()

postFilesPath = os.path.join(os.getcwd(), 'content/posts')
openaiApiKey = os.getenv('OPEN_AI_API_KEY')
openai.api_key = openaiApiKey

def generatedPostContentFromChatGTP(subject):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
         messages=[
             {"role": "user", "content": "Şimdi bana "+subject+" Bu blog makalesini yazarken bana sadece makalenin içeriğini mdx formatında ve olabildiğince detaylı bir şekilde vermeni istiyorum. Makalenin en başında alt alta [---\n title: {Makalenin başlığı}\nkeywords: {SEO için anahtar kelimeler}\ndate:{yil-ay-gun formatında tarih}\ndescription: {açıklaması}.\n ---] yazmalı. Tüm makale baştan sona ingilizce dilinde olmalı."}
             ]
    )
    return response.choices[0].message['content']

def generatedPostFile(fileName,content):
    with open(fileName, 'w', encoding="utf-8") as f:
        f.write(content)


def changedFilesGitPushCommandRun(message):
    os.system('git add .')
    os.system('git commit -m "'+message+'"')
    os.system('git push')


#postContent = generatedPostContentFromChatGTP(".Net Core ile bir REST API web servisinin nin nasıl yazılacağını anlatan bir blog yazmanı istiyorum.");

yazilim_sorunlari = [ "Software Development Processes: Agile vs. Waterfall Comparison",
  "Web Development: Front-end vs. Back-end Differences",
  "Database Design and Normalization Fundamentals",
  "Introduction to Python Programming: Basic Concepts and Language Features",
  "Mobile App Development: Android vs. iOS",
  "Software Testing Automation: Best Practices and Tools",
  "Software Security: Common Threats and Protection Strategies",
  "Artificial Intelligence and Machine Learning: Fundamental Principles and Applications",
  "Software Architecture: Monolithic vs. Microservices Architecture Comparison",
  "Blockchain Technology and the Future of Cryptocurrencies",
  "The Importance of Open Source Software and a Guide to Contributing",
  "Best Practices for Software Development and Code Quality",
  "Digital Product Design: User Experience and User Interface Design",
  "Data Analytics and Big Data: Data Mining and Data Visualization",
  "Internet of Things (IoT) and Smart Devices: The Technology of the Future",
  "Tips for a Software Career: Paths to Becoming a Successful Software Developer",
]

for item in yazilim_sorunlari:
    postContent = generatedPostContentFromChatGTP(item+" konusu hakkında blog yazmanı istiyorum.");
    title = re.search(r"title:\s*(.*)", postContent)
    if title:
        title = title.group(1)
        title = slugify(title)
        print(title)
        generatedPostFile(postFilesPath+'/'+title+'.mdx', postContent)
    else:
        print("Başlık bulunamadı.")
    
    time.sleep(2)
changedFilesGitPushCommandRun('post eklendi')

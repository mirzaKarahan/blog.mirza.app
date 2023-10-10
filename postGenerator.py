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
             {"role": "user", "content": "Şimdi bana "+subject+" Bu blog makalesini yazarken bana sadece makalenin içeriğini mdx formatında ve olabildiğince detaylı bir şekilde vermeni istiyorum. Makalenin en başında alt alta [---\n title: {Makalenin başlığı}\nkeywords: {SEO için anahtar kelimeler}\ndate:{yil-ay-gun formatında tarih}\ndescription: {açıklaması}.\n ---] yazmalı."}
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

yazilim_sorunlari = [".Net Core ile bir REST API web servisinin nin nasıl yazılır","İsrail ile Filistin arasındaki gerilim"]

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

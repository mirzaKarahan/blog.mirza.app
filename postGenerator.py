import os,uuid,re
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
             {"role": "user", "content": "Şimdi bana "+subject+" bu konu hakkında blog yazmanı istiyorum. Bu blog makalesini yazarken bana sadece makalenin içeriğini mdx formatında ve olabildiğince detaylı bir şekilde vermeni istiyorum. Makalenin en başında alt alta [---\n title: {Makalenin başlığı} description: {açıklaması}.\n ---] yazmalı."}
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


postContent = generatedPostContentFromChatGTP("yazılım dünyasında en çok karşılaşılan hata ve çözümünü içeren sipesifik bir tane konu bulup");
print(postContent);

title = re.search(r"title:\s*(.*)", postContent)
if title:
    title = title.group(1)
    title = slugify(title)
    print(title)
    generatedPostFile(postFilesPath+'/'+title+'-'+str(uuid.uuid4())+'.mdx', postContent)
    changedFilesGitPushCommandRun('post eklendi')
else:
    print("Başlık bulunamadı.")
import os,uuid
from topic import Topic
from dotenv import load_dotenv
import openai
  
load_dotenv()

postFilesPath = os.path.join(os.getcwd(), 'content/posts')
openaiApiKey = os.getenv('OPEN_AI_API_KEY')
openai.api_key = openaiApiKey

def generatedPostContentFromChatGTP(subject):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
         messages=[
             {"role": "user", "content": "Şimdi bana "+subject+" bu konu hakkında blog yazmanı istiyorum. Bu blog makalesini yazarken bana sadece makalenin içeriğini mdx formatında ve olabildiğince detaylı bir şekilde vermeni istiyorum. Makalenin en başında alt alta [---\n title: {Makalenin başlığı} description: {açıklaması}.\n ---] yazmalı."}
        #{"role": "user", "content": "Şimdi bana "+subject+" bu konu hakkında blog yazmanı istiyorum. Bu blog makalesini yazarken bana sadece makalenin içeriğini mdx formatında ve olabildiğince detaylı bir şekilde vermeni istiyorum."}
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


postContent = generatedPostContentFromChatGTP("yazılım dünyasında en çok karşılaşılan hataları ve çözümlerini içeren sipesifik bir tane konu bulup");
print(postContent);

generatedPostFile(postFilesPath+'/test-'+str(uuid.uuid4())+'.mdx', postContent)
changedFilesGitPushCommandRun('post eklendi')
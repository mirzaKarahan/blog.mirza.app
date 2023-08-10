import os
from dotenv import load_dotenv
import openai
  
load_dotenv()

openaiApiKey = os.getenv('OPEN_AI_API_KEY')
openai.my_api_key = openaiApiKey
postFilesPath = os.path.join(os.getcwd(), 'content/posts')
print(postFilesPath)

def generatedPostFile(fileName,content):
    with open(fileName, 'w') as f:
        f.write(content)


generatedPostFile(postFilesPath+'/test.mdx', 'test')
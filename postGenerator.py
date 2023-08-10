import os,uuid
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

def changedFilesGitPushCommandRun(message):
    os.system('git add .')
    os.system('git commit -m "'+message+'"')
    os.system('git push')

generatedPostFile(postFilesPath+'/test-'+str(uuid.uuid4())+'.mdx', 'test')
changedFilesGitPushCommandRun('test postu eklendi')
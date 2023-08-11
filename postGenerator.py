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
             {"role": "user", "content": "Şimdi bana "+subject+" Bu blog makalesini yazarken bana sadece makalenin içeriğini mdx formatında ve olabildiğince detaylı bir şekilde vermeni istiyorum. Makalenin en başında alt alta [---\n title: {Makalenin başlığı} description: {açıklaması}.\n ---] yazmalı."}
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

yazilim_sorunlari = [
    "Belirsiz proje gereksinimleri",
    "Yetersiz dokümantasyon",
    "Kötü kod kalitesi",
    "Yetersiz test süreçleri",
    "Proje süresinin yanlış tahmin edilmesi",
    "Yetersiz iletişim",
    "Teknolojik borç",
    "Yeniden kullanılabilir kod eksikliği",
    "Performans sorunları",
    "Güvenlik açıkları",
    "Yetersiz araç ve teknolojilerin seçimi",
    "Tasarım ve kullanılabilirlik sorunları",
    "Entegrasyon sorunları",
    "Sürdürülebilirlik eksikliği",
    "Eksik veya yanlış kullanıcı kabul testleri",
    "Ekip üyeleri arasında yetenek dengesizliği",
    "Yetersiz geri bildirim döngüleri",
    "Müşteri beklentilerinin yanlış yönetilmesi",
    "Kod tekrarı",
    "Yetersiz hata yönetimi",
    "Yetersiz sürüm kontrolü",
    "Eksik veya yanlış veri yedekleme",
    "Yetersiz kod yorumları",
    "Kodun okunabilirliğinin düşük olması",
    "Yetersiz kod incelemeleri",
    "Yetersiz devops süreçleri",
    "Eksik otomasyon",
    "Yetersiz altyapı yönetimi",
    "Eksik kapasite planlaması",
    "Yetersiz eğitim ve öğrenme fırsatları",
    "Yetersiz kullanıcı deneyimi (UX) tasarımı",
    "Kötü veritabanı tasarımı",
    "Yetersiz API dokümantasyonu",
    "Eksik veya yanlış hata raporlama",
    "Yetersiz güncelleme ve yükseltme süreçleri",
    "Yetersiz kaynak yönetimi",
    "Kötü mimari tasarım",
    "Yetersiz ölçeklenebilirlik",
    "Eksik veya yanlış kullanıcı eğitimi",
    "Yetersiz proje yönetimi",
    "Yetersiz bütçeleme",
    "Yetersiz risk yönetimi",
    "Yetersiz kalite güvencesi",
    "Yetersiz kullanıcı desteği",
    "Yetersiz geriye dönük uyumluluk",
    "Yetersiz güvenlik testleri",
    "Kötü kullanıcı arayüzü (UI) tasarımı",
    "Yetersiz kullanıcı geri bildirimi",
    "Yetersiz performans izleme",
    "Yetersiz süreç iyileştirmeleri"
]

for item in yazilim_sorunlari:
    postContent = generatedPostContentFromChatGTP("yazılım dünyasında "+item+" konusu hakkında blog yazmanı istiyorum.");
    title = re.search(r"title:\s*(.*)", postContent)
    if title:
        title = title.group(1)
        title = slugify(title)
        print(title)
        generatedPostFile(postFilesPath+'/'+title+'.mdx', postContent)
        changedFilesGitPushCommandRun('post eklendi')
    else:
        print("Başlık bulunamadı.")
    
    time.sleep(5)
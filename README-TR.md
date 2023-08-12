# Otomatik Blog Oluşturucu

Bu repo, Chat GPT ile otomatik blog yazıları oluşturup bir blog uygulamasında yayınlamanın ne kadar kısa sürdüğünü göstermek amacıyla hazırlanmıştır. Bu uygulama yaklaşık 1 saat içerisinde tamamlandı.

## Temel Bilgiler

- Bu blog uygulaması Node.js ve Next.js ile yazılmıştır.
- Uygulama, [Next.js Contentlayer Blog Starter](https://vercel.com/templates/next.js/nextjs-contentlayer) üzerine inşa edilmiştir.
- Uygulama, vercel.com üzerinden yayına alınmıştır.
- Python ile yazılan bir bot, Chat GPT API'si üzerinden blog yazıları oluşturup, Next.js Contentlayer Blog Starter uygulaması için blog yapılandırmasını gerçekleştirmektedir.

## Kurulum

1. Repoyu clone edin.

2. `npm update` komutu ile node modüllerini yükleyin.

3. OpenAI'dan API anahtarı alın.

4. `.env` dosyası oluşturun ve içerisine `OPEN_AI_API_KEY = [API_KEY]` şeklinde API anahtarınızı ekleyin.

5. Python için gerekli kütüphaneleri yükleyin:

6. Uygulamayı çalıştırın, python ile blog yazıları oluşturun. Python programı, oluşturulan blogları otomatik olarak git'e pushlar.

7. Eğer vercel üzerinde yayınlıyorsanız, vercel otomatik olarak değişiklikleri algılar ve yayına alır.

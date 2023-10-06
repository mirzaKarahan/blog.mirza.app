import { allPosts } from "@/.contentlayer/generated"
console.log(allPosts);
module.exports = {
    siteUrl: 'https://blog.mirza.app', // Web sitenizin URL'sini buraya yazın
    generateRobotsTxt: true, // robots.txt dosyasını da oluşturmak için true yapın
    sitemapSize: 7000, // Bir sitemap dosyasındaki maksimum URL sayısı
    exclude: ['/api'],// Sitemap'den hariç tutulacak yollar
  };
  
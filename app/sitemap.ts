import { MetadataRoute } from 'next'
import { allPosts } from "@/.contentlayer/generated"

export default function sitemap(): MetadataRoute.Sitemap {
  let sirali = JSON.parse(JSON.stringify(allPosts));
  console.log(typeof sirali)
  let dizi = [
    {
      url: 'https://blog.mirza.app',
      lastModified: new Date(),
      priority: 1,
    },
    {
      url: 'https://blog.mirza.app/about',
      lastModified: new Date(),
      priority: 1,
    }
  ];
  sirali.map((item) => {
    dizi.push({
      url: `https://blog.mirza.app${item.slug}`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 1,
    })
  })
  console.log(dizi)
  return dizi
}
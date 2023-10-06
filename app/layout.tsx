import Link from "next/link"
import Script from "next/script";
import "./globals.css"
import { Metadata } from "next"
import { Inter } from "next/font/google"
import { ThemeProvider } from "@/components/theme-provider"
import { Analytics } from "@/components/analytics"
import Image from 'next/image'
import Head from "next/head";

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "Chat GPT Genereted Blog Post",
  description: "Generated by Next.js, Vercel, Chat GPT",
  keywords: "AI,yapay zeka,chat gpt,chatbot,chat bot,vercel",
}

interface RootLayoutProps {
  children: React.ReactNode
}

export default function RootLayout({ children }: RootLayoutProps) {
  

  return (
    <html lang="en">
        <Script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6480877761651988" crossOrigin="anonymous"/>
      <body
        className={`antialiased min-h-screen bg-white dark:bg-slate-950 text-slate-900 dark:text-slate-50 ${inter.className}`}
      >
        <ThemeProvider attribute="class" defaultTheme="system" enableSystem>
          <div className="max-w-2xl mx-auto py-10 px-4">
            <header>
              <div className="flex items-center justify-between">
              <Link href="/"><Image className="grayscale hover:grayscale-0" src="/mirza-logo.png" width={150} height={500} alt="Picture of the author"/></Link>
                <nav className="ml-auto text-sm font-medium space-x-6">
                  <Link href="/">Blog</Link>
                  <Link href="/about">Hakkında</Link>
                  <Link target="_blank" href="https://github.com/mirzaKarahan/nextjs-contentlayer-blog">GitHub</Link>
                </nav>
              </div>
            </header>
            <main>{children}</main>
          </div>
          <Analytics />
        </ThemeProvider>
      </body>
    </html>
  )
}

# Automatic Blog Generator

This repo was created to demonstrate how quickly you can publish blog posts on a blog application using Chat GPT. The application was completed in approximately 1 hour.

## Key Information

- The blog application is written with Node.js and Next.js.
- The application is built on top of [Next.js Contentlayer Blog Starter](https://vercel.com/templates/next.js/nextjs-contentlayer).
- The application is deployed on vercel.com.
- A bot written in Python generates blog posts via the Chat GPT API and configures them for the Next.js Contentlayer Blog Starter application.

## Installation

1. Clone the repo.

2. Install node modules with `npm update`.

3. Obtain an API key from OpenAI.

4. Create a `.env` file and add your API key as `OPEN_AI_API_KEY = [API_KEY]`.

5. Install the required libraries for Python:

6. Run the application, generate blog posts with Python. The Python program will automatically push the generated blogs to git.

7. If you're deploying on vercel, it will automatically detect the changes and deploy them.

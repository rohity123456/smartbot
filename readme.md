# SmartBot (A general assistance app)

## Description
SmartBot is a chatbot that can generat answer questions using text and image inputs also searches relevant youtube videos. It is built using Python, Flask and powered by Langchain Agents.

## Features
- Text to Text Answers
- Image to Text Answers
- Youtube Video Search

## Steps to run

- Create a virtual environment using :

  ```python3 -m venv venv```

- Activate the virtual environment using :

  ```source venv/bin/activate```
  
- Install dependencies from requirements.txt using :

  ```pip install -r requirements.txt```

- Create a .env file in the root directory and add the following variables :

- Create a /images directory in the root directory to store images.

  ```
  OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
  ```
- Run the app using :

  ```python app.py```
- Endpoints :
  - /chat/bot [GET]
    - Call this API to get Bot Id and use to chat the given bot.
  - /chat [POST]
    - Call this API to chat with the bot.
    - Request Body (form-data) :
      ```
      {
        "bot_id": <Bot Id from the get API>,
        "image": <Pass image binary file>
        "query": <Your query>
      }
      ```
  - /youtube-search


## Contact
- [Linkedin](https://www.linkedin.com/in/rohit-yadav-sde/)
- [Github](https://github.com/rohity123456)
- [Email](mailto:rohity123456@gmail.com)

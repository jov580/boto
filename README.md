# boto

## About project
boto is Telegram bot that checks and follows URLs, and responds with image/video from URL(if valid).

## Running the project
Project consists of files: 
-bot.py
-requirements.txt
-Dockerfile
-docker_compose.yml 

For bot.py to works, it needs .env file that contains bot token, which is not included here.

## Commands:
1. /hi, /hello - bot responds with "Hello"
2. /image, /photo followed by link - bot checks if URL is valid and sends proper reply. If link is valid, bot downloads image from the link and sends it back to user
3. /video followed by link - same as 2, bot checks if URL is valid and replies. If it is valid, bot downloads the video from the link in .mp4 format and sends it back tu user as media document
4. for all other inputs, bot echoes the message back

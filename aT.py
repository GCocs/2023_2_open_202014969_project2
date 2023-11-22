import schedule
import time
import pytz
import datetime
import telegram
import asyncio

token = "6527142271:AAHPj-712vqa_C3UMIMAbpxuiQN8cTq2xIo"
# Bot: GCoca3_bot
# Token: 6527142271:AAHPj-712vqa_C3UMIMAbpxuiQN8cTq2xIo
# chat_id: 6893588310
# channel : -1002111713064

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    print("current time = ", str(now))

    async def send_telegram_message():
        chat_id = 6893588310
        bot = telegram.Bot(token=token)
        public_chat_name = -1002111713064
        message = await bot.send_message(chat_id=public_chat_name, text="alarm arrived!!!!!")
        print(message.chat_id)
    asyncio.run(send_telegram_message())
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(30)


    
    

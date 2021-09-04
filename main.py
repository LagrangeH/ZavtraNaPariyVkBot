# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from datetime import datetime

import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
from loguru import logger as log
import traceback

import data
import datetime

log.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB", compression="zip")

vk = vk_api.VkApi(token=data.TOKEN)
vk_session = vk.get_api()
# longpoll = VkBotLongPoll(vk, 206847683)    # <--- write id here

def isworkday(): # эта функция проверят номер дня и не допускает работу бота  по субботам(5) и воскресеньям(6)
    today = datetime.datetime.today().weekday()
    if today not in (5,6):
        return True
    else:
        return False


@log.catch()
def run():
    while True:
        try:
            if isworkday():
                # if '21:00:' not in str(datetime.now()):
                r = vk.method('messages.send', {
                    'chat_id': 1,
                    'random_id': get_random_id(),
                    'message': None,
                    'attachment': 'video-206847683_456239017'
                })
                log.debug(r)
                time.sleep(60*60*24)
            else:
                time.sleep(60*60*24)
        except KeyboardInterrupt:
            log.info('Bot stopped')
            break

        except TimeoutError:
            log.error('Ошибка времени ожидания. (Вероятно перезагрузка серверов VK)')

        except:
            log.error(traceback.format_exc())


if __name__ == '__main__':
    log.info('Bot launched')
    run()

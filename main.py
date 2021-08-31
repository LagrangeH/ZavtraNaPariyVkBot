# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.utils import get_random_id
from loguru import logger as log
import traceback

import data


log.add("debug.log", format="{time} {level} {message}", level="DEBUG", rotation="100 KB", compression="zip")

vk = vk_api.VkApi(token=data.TOKEN)
vk_session = vk.get_api()
longpoll = VkBotLongPoll(vk, 'YOUR ID')    # <--- write id here


@log.catch()
def run():
    while True:
        try:
            for event in longpoll.listen():

                if event.type == VkBotEventType.MESSAGE_NEW:
                    response = event.text.lower()
                    # <-- body

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

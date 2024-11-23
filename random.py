from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import random

# 定义命令触发器
random_command = on_command("random", aliases={"/random"}, priority=5, block=True)

@random_command.handle()
async def handle_random(bot: Bot, event: Event):
    # 生成一个随机数字（范围 1~100，可以根据需要调整）
    number = random.randint(1, 100)
    # 返回消息给用户
    await random_command.finish(f"随机数字是：{number}")

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger # 使用 astrbot 提供的 logger 接口

@register("test", "Benxp", "一个简单的 test 插件", "1.0.0", "repo url")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    # 注册指令的装饰器。指令名为 test，发送 `/test` 触发
    @filter.command("test")
    async def helloworld(self, event: AstrMessageEvent):
        '''这是一个 test 指令，回复包含发送者信息的问候语'''
        # 方案1：优先获取用户名，兜底用发送者ID
        try:
            # 尝试获取用户名
            user_name = event.get_sender_name()
            # 若用户名为空/None，用发送者ID替代
            if not user_name or user_name.strip() == "":
                user_name = event.get_sender_id()  # 获取发送者唯一ID
        except Exception as e:
            # 捕获异常，避免插件崩溃，兜底显示"用户"
            logger.warning(f"获取用户名失败: {str(e)}")
            user_name = "用户"
        
        # 获取消息纯文本内容（保留原有逻辑）
        message_str = event.message_str
        logger.info(f"触发hello world指令! 发送者: {user_name}, 消息内容: {message_str}")
        
        # 回复消息
        yield event.plain_result(f"Hello, {user_name}!")

    async def terminate(self):
        '''插件被卸载/停用时调用'''
        logger.info("test插件已停用")
from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger # 使用 astrbot 提供的 logger 接口

@register("test", "Benxp", "一个简单的 test 插件", "1.0.0", "repo url")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("ban")
    async def helloworld(self, event: AstrMessageEvent):        
        # 回复消息
        yield event.plain_result(f"不理解您的心情，平台不支持一切合理合规的机器人开发使用，同时对于不合规使用情况采取对应的十年与删号。现阶段平台已统一对外封闭说明开发能力申请规则，不提倡“特权”行为，开发者不可自行翻阅相关资料查阅申请规则。不需要您的支持与理解！")
        
    @filter.command("bug")
    async def mai(self, event: AstrMessageEvent):
        # 回复消息
        yield event.plain_result(f"Benxp在回复广大用户意见时曾说：不是不修bug，是缓修、慢修、优修、灵活地修，创新地修，辩证地修。要有次序有调节地修，从高频率地修到高质量地修，让有条件的先修，有紧急需求的先修，也要从实际出发，因服制宜，具体情况具体修。根据插件架构、代码基础、运行条件，有选择地推动创新修复模式发展、资源配置优化，用新工具、新方法改造提升传统修bug方式，积极促进服务器模块化、稳定化、可玩性、易用性的持续升级。统筹推进服务器体验新质态全面发展，健全修复流程与行为规范，达到结果稳步向好。不管早修晚修，能修的都是好修。努力实现先修带动后修，最终实现共同运营进步")


    async def terminate(self):
        '''插件被卸载/停用时调用'''
        logger.info("test插件已停用")
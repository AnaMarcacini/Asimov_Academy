import lightbulb

bot = lightbulb.BotApp(token=open('token_ds.txt', 'r').read(),default_enabled_guilds=(int(open('ds_channelid. txt', 'r').read ()) ))
@bot.command

elightbu lb.command ( 'msg_asmv', 'Saudação Asimov Academy')
elightbulb. imp lements (lightbu lb. SslashCommand)
async def hello(ctx):
await ctx. respond("01á, comunidade Asimov Acadeny!"
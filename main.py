import discord
from discord.ext import commands
import random
import asyncio
import qrcode
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from currency_converter import CurrencyConverter
import wikipedia
c = CurrencyConverter()





client = commands.Bot(command_prefix="+",intents=discord.Intents.all())
coin = ['HEADs','TAILS']
dice = ['1','2','3','4','5']
magic_ball = ['As I see it, yes.','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Dont count on it','It is certain','It is decidedly so',"Hell No!"]
@client.event
async def on_ready():
    botonline_channel = client.get_channel(828622524552183809)
    print('Bot is Ready')
    while True:
        embed = discord.Embed(title='I am Online',color=discord.Color.blurple())
        await botonline_channel.send(embed=embed)
        await asyncio.sleep(3600)

@client.event
async def on_member_join(member):
    member_joinchannel = client.get_channel(828623138304163881)
    embed = discord.Embed(title=f'**Welcome to the Calender Official** {member.display_name} {member.id}')
    embed.set_thumbnail(url=member.avatar_url)
    #embed.set_image(url='https://image.freepik.com/free-vector/welcome-neon-sign-vector_53876-76088.jpg')
    await member_joinchannel.send(embed=embed)
    
#print(x)

#discod presense
async def ch_pr():
    await client.wait_until_ready()
    x =  'On '+str(len(client.guilds)) + ' Servers'
    statues = ['Discord.py',x,"Help | prefix:-'+'",'Under Development','Sleeping','Version - 0.8']
    
    while not client.is_closed():
        status = random.choice(statues)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(10)
client.loop.create_task(ch_pr())

    
@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason="No reason Provided"):
    #guild = client.fetch_guilds(*, limit=100, before=None, after=None)
    embed = discord.Embed(title = "kick", description = str(member.mention)+" has been kicked ", color=discord.Color.red())
    embed.set_thumbnail(url=member.avatar_url)
    await member.kick(reason=reason)
    await ctx.send(embed=embed)
    await member.send(reason)
    ###  await ctx.send(embed=embed)

#utility part

@client.command(aliases=['grt'])
async def greet(ctx,member : discord.Member):
    embed = discord.Embed(title="Greeting A member "+ str(member.name), description=":star_struck::star_struck: I am glad that you are here :partying_face::partying_face::star_struck::star_struck:"+str(member.mention),color=discord.Color.purple())
    embed.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed=embed)

@client.command(aliases=['RLD'])
async def rld(ctx):
    
    d=random.choice(dice)
    embed = discord.Embed(title = 'Rolling a Dice',description="Try Your Luck",color=discord.Color.dark_gray())
    embed.set_thumbnail(url='https://image.freepik.com/free-vector/two-vector-red-casino-falling-dice-with-white-dots-isolated-background_1284-48503.jpg')
    await ctx.send(embed=embed)
    await asyncio.sleep(2)
    embed= discord.Embed(title='You gotta:',description=d,color=discord.Color.dark_gray())
    embed.set_thumbnail(url='https://image.freepik.com/free-vector/two-vector-red-casino-falling-dice-with-white-dots-isolated-background_1284-48503.jpg')
    await ctx.send(embed=embed)


@client.command(aliases=['Flc'])
async def fleep(ctx):
    c = random.choice(coin)
    embed = discord.Embed(title='Fliping a Coin',description="Try your Luck",color=discord.Color.dark_orange())
    embed.set_thumbnail(url='https://image.freepik.com/free-vector/dollar_53876-25498.jpg')
    await ctx.send(embed=embed)
    await asyncio.sleep(2)
    embed= discord.Embed(title='You gotta',description=c,color=discord.Color.dark_orange())
    embed.set_thumbnail(url='https://image.freepik.com/free-vector/dollar_53876-25498.jpg')
    await ctx.send(embed=embed)


@client.command(aliases=['clr'])
@commands.has_permissions(manage_messages = True)
@commands.has_permissions(manage_channels = True)
async def clear(ctx,amount=2):
    embed = discord.Embed(title='Deleting Messages',description='Messages Deleted Succesfully',color=discord.Color.dark_magenta())
    await ctx.channel.purge(limit = amount)
    await ctx.send(embed=embed)
    await asyncio.sleep(2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    await ctx.channel.purge(limit = 1)                                                                                                                                                                                                                                                                  

#@client.command()
#async def userinfo(ctx,member : discord.Member = *):
 #   embed = discord.Embed(title='Userinfo Requested By-'+str(member.mention),description="Returns User Account Information",color=discord.Color.blue())
  #  embed.add_field(name="User Name",value=member.name,inline=True)
   # await ctx.send(embed=embed)
    
@client.command(aliases=['CC'],help='it convert the given currency to other currncy [currency1] [currency2] [amount]')
async def convcurr(ctx,arg1,arg2,*,amount):
    curr1 = arg1.upper()
    curr2 = arg2.upper()
    value = c.convert(amount,curr1,curr2)
    term_decimal = "{:.2f}".format(value)
    embed = discord.Embed(title='Currency Converter',color=discord.Color.gold())
    embed.set_thumbnail(url='https://image.freepik.com/free-vector/indian-rupee-currency-exchange_23-2148002764.jpg')
    embed.add_field(name='Currency You are Converting From:-',value=curr1,inline=False)
    embed.add_field(name='Currency You are Converting to :-',value=curr2,inline=False)
    embed.add_field(name='Currency Amount:-',value=amount,inline=False)
    embed.add_field(name=f'Value of {amount} {curr1} in {curr2}:-',value=term_decimal,inline=False)
    await ctx.send(embed=embed)





@client.command(aliases=["hlp"])
async def h(ctx):
    embed = discord.Embed(title=':grey_question: HELP :grey_question: ',description="HELP commands:grey_question: ",color=discord.Color.blurple())
    embed.add_field(name='Help Prefix',value='#',inline=False)
    embed.add_field(name='help commands',value='kick,hlp,greet,flc,rld,game,clr,box,magic ball',inline=False)
    embed.add_field(name='Magic Ball',value='command prefix **__#mg__**',inline=False)
    await ctx.send(embed=embed)













@client.command()
async def invite(ctx,member:discord.Member = None):
    member = ctx.author if not member else member
    await ctx.send('**CHECK DMs**')
    new = discord.Embed(title='INVITE ME',description='**Here is the Link\n** https://discord.com/api/oauth2/authorize?client_id=816994265388417034&permissions=2081422583&scope=bot') 
    new.set_footer(text=f"Requested By {ctx.author}",icon_url=ctx.author.avatar_url)
    await member.send(embed=new)



@client.command(aliases=['magicball'])
async def mg(ctx):
    embed = discord.Embed(title='Magic Ball',description='you will get 10 seconds to Ask in your Mind',color=discord.Color.dark_purple())
    embed.set_thumbnail(url='https://image.freepik.com/free-vector/magic-sphere-illustration_1284-6361.jpg')
    embed.add_field(name='Get Advised',value='Ask Any question in your mind and Bot will answer and boost Your confidence')
    await ctx.send(embed=embed)
    await asyncio.sleep(10)
    magic_answer = random.choice(magic_ball)
    embed = discord.Embed(title='Your Answer is ',description=magic_answer,color=discord.Color.dark_purple())
    embed.set_thumbnail(url='https://image.freepik.com/free-vector/magic-sphere-illustration_1284-6361.jpg')
    await ctx.send(embed=embed)




@client.command(aliases=['usif'])
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(title='**__Userinfo__**',color=member.color,timestamps=ctx.message.created_at)
    embed.set_author(name=f"User Info {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}",icon_url=ctx.author.avatar_url)
    embed.add_field(name='ID',value=member.id,inline=False)
    embed.add_field(name='User Name in the server:',value=member.display_name,inline=False)
    embed.add_field(name='Discriminator:',value=member.discriminator,inline=False)
    embed.add_field(name='Current Status:',value=str(member.status).title(),inline=False)
    #embed.add_field(name='Current Activity:',value=f'{str(member.activity.type).title().split('.')[1]}{member.activity.name}' if member.activity is not None else 'None')
    embed.add_field(name='Created at:',value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p IST"),inline=False)
    embed.add_field(name='Joined at:',value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p IST"),inline=False)
    embed.add_field(name=f'Roles ({len(roles)})',value=" ".join([role.mention for role in roles]),inline=False)
    #embed.add_field(name=f'{member.mention} has permissions to mangage server?',value=ctx.member.manage_guild(),inline=False)
    #embed.add_field(name=f'{member.member} can manage server roles?', value=discord.manage_roles(),inline=False)
    #embed.add_field(name=f'{member.member} is on mobile discord?', value=member.is_on_mobile,inline=False)
    embed.add_field(name='Most Prior Role:',value=member.top_role.mention,inline=False)
    embed.add_field(name='Is Member a Bot?',value=member.bot,inline=False)
    
    await ctx.send(embed=embed)

@client.command(aliases=['wiki'])
async def wikisearch(ctx,search):
    serch_result = wikipedia.search(search,results=5)
    serch_embed = discord.Embed(title='WikiPedia Search',descrptions='React To See more about that',timestamps=ctx.message.created_at,color=discord.Color.dark_gray())
    serch_embed.set_footer(text=f"Requested By {ctx.author}",icon_url=ctx.author.avatar_url)
    serch_embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvWUVmzipFoMLQkshKJ57TGcjeyxCPo05paA&usqp=CAU')
    serch_embed.add_field(name='**Result ** :one:',value=serch_result[0],inline=False)
    serch_embed.add_field(name='**Result ** :two:',value=serch_result[1],inline=False)
    serch_embed.add_field(name='**Result ** :three:',value=serch_result[2],inline=False)
    serch_embed.add_field(name='**Result ** :four:',value=serch_result[3],inline=False)
    serch_embed.add_field(name='**Result ** :five:',value=serch_result[4],inline=False)
    serch_mess = await ctx.send(embed=serch_embed)
    await serch_mess.add_reaction('1️⃣')
    await serch_mess.add_reaction('2️⃣')
    await serch_mess.add_reaction('3️⃣')
    await serch_mess.add_reaction('4️⃣')
    await serch_mess.add_reaction('5️⃣')


    result_embed = discord.Embed(title='Showing Results',color=discord.Color.dark_red())
    result_embed.set_footer(text=f"Showing Results Requested By {ctx.author}",icon_url=ctx.author.avatar_url)
    
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["1️⃣", "2️⃣","3️⃣","4️⃣","5️⃣"]

    try:
        reaction, user = await client.wait_for("reaction_add", timeout=10, check=check)

        if str(reaction.emoji) == '1️⃣':
            result = wikipedia.page(serch_result[0])
            content = result.content
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content[:900]+'............**OPEN LINK TO READ MORE**'),inline=False)
            try:
                result_embed.set_image(url=result.images[0])
            except:
                result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)   
        elif str(reaction.emoji) == '2️⃣':
            result = wikipedia.page(serch_result[1])
            content = result.content
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content[:900]+'............**OPEN LINK TO READ MORE**'),inline=False)
            try:
                result_embed.set_image(url=result.images[0])
            except:
                result_embed.set_image(url=result.images[1])

            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)
        elif str(reaction.emoji) == '3️⃣':
            result = wikipedia.page(serch_result[2])
            content = result.content
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content[:900]+'............**OPEN LINK TO READ MORE**'),inline=False)
            try:
                result_embed.set_image(url=result.images[0])
            except:
                result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)
        elif str(reaction.emoji) == '4️⃣':
            result = wikipedia.page(serch_result[3])
            content = result.content
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content[:900]+'............**OPEN LINK TO READ MORE**'),inline=False)
            try:
                result_embed.set_image(url=result.images[0])
            except:
                result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)
        else:
            result = wikipedia.page(serch_result[4])
            content = result.content
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content[:900]+'............**OPEN LINK TO READ MORE**'),inline=False)
            try:
                result_embed.set_image(url=result.images[0])
            except:
                result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)
    except asyncio.TimeoutError:
        await ctx.send('**Time out**')


@client.command(aliases=['ngg'])
async def number_guess(ctx):
    chanses = 3
    choice = random.randint(1,101)
    start_embed = discord.Embed(title='NUMBER GUESSING GAME',description="This is a Number Guessing game,\n**RULES**\n1). It will give Various Hints so you can guess the number correctly\n2). You have 3 chanses to guess correctly",color=discord.Color.orange())
    await ctx.send(embed=start_embed)
    await asyncio.sleep(2)
    await ctx.send('**NUMBER CHOOSEN**')
    hint_embed = discord.Embed(title='HINTS',description='Read Hints Carefully',color=discord.Color.orange())
    if int(choice) in range(0,11):
        if int(choice) in range(1,6):
            hint_embed.add_field(name='Range Hint:',value='Number is between 1 to 5',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 6 to 10',inline=False)
    elif int(choice) in range(11,21):
        if int(choice) in range(11, 16):
            hint_embed.add_field(name='Range Hint:',value='Number is between 11 to 15',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 16 to 20',inline=False)
    elif int(choice) in range(21,31):
        if int(choice) in range(21,26):
            hint_embed.add_field(name='Range Hint:',value='Number is between 21 to 25',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 26 to 30',inline=False)
    elif int(choice) in range(31,41):
        if int(choice) in range(31,36):
            hint_embed.add_field(name='Range Hint:',value='Number is between 31 to 35',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 36 to 40',inline=False)
    elif int(choice) in range(41,51):
        if int(choice) in range(41,46):
            hint_embed.add_field(name='Range Hint:',value='Number is between 41 to 45',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 46 to 50',inline=False)
    elif int(choice) in range(51,61):
        if int(choice) in range(51,56):
            hint_embed.add_field(name='Range Hint:',value='Number is between 51 to 55',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 56 to 60',inline=False)
    elif int(choice) in range(61,71):
        if int(choice) in range(61,66):
            hint_embed.add_field(name='Range Hint:',value='Number is between 61 to 65',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 66 to 70',inline=False)
    elif int(choice) in range(71,81):
        if int(choice) in range(71,76):
            hint_embed.add_field(name='Range Hint:',value='Number is between 71 to 75',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 76 to 80',inline=False)
    elif int(choice) in range(81,91):
        if int(choice) in range(81,86):
            hint_embed.add_field(name='Range Hint:',value='Number is between 81 to 85',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 86 to 90',inline=False)
    else:
        if int(choice) in range(91,96):
            hint_embed.add_field(name='Range Hint:',value='Number is between 90 to 95',inline=False)
        else:
            hint_embed.add_field(name='Range Hint:',value='Number is between 96 to 100',inline=False)
    

    c = 1
    for x in range(2, int(choice / 2)):
        if int(choice) % x == 0:
            c = 0
            pass
    
    if c == 1:
        hint_embed.add_field(name='Prime Number Hint:',value="True",inline=False)
    else:
        hint_embed.add_field(name='Prime Number Hint:',value="False",inline=False)

    if int(choice)%2 == 0:
        hint_embed.add_field(name='ODD or EVEN Hint:',value="Even",inline=False)
    else:
        hint_embed.add_field(name='ODD or EVEN Hint:',value="Odd",inline=False)
    
    await ctx.send(embed=hint_embed)
    await asyncio.sleep(2)
    await ctx.send("**Start Guessing**")

    try:
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        #user_choice = (await client.wait_for('message', check=check,timeout=60)).content
        while chanses > 0:
            user_choice = (await client.wait_for('message', check=check,timeout=60)).content
            if user_choice==str(choice):
                await ctx.send('**You are Lucky this Time!You Guessed Right**')
                await ctx.send("**The Number Was :-**"+ str(choice))
                break
            else:
                await ctx.send("**'Try Again! Read Hints Carefully'**")
                chanses = chanses-1

            life = discord.Embed(title=f'Life Remaining {chanses}',color=discord.Color.orange())
            await ctx.send(embed=life)
    except asyncio.TimeoutError:
        await ctx.send('Timed Out')
    
    

    if chanses==3:
        title = "You are born Genius"
    elif chanses==2:
        title =  "You are like a Rookie Detective"
    elif chanses==1:
        title =  "You Won"
    else:
        title = 'Game OVER! You Loose'
        no = discord.Embed(title=f"The Number Was: {choice}",color=discord.Color.orange())
        await ctx.send(embed=no)
        
    r_embed = discord.Embed(title=title,color=discord.Color.orange())

    
    await ctx.send(embed=r_embed)



@client.command(aliases = ["stone_paper_scissors","rps"])
async def sps(ctx):    #rps is short for rock, paper, scissor
    emojis = ['✊', '🖐️', '✌️','❌']
    myscore = 0
    botscore = 0
    embedVar = discord.Embed(title="STONE PAPER SCISSOR GAME",description = "Choose between rock, paper, or scissors, {}." . format(ctx.author.mention), color = 0xff9900)
    embedVar.add_field(name=":fist: STONE", value="React with :fist: emoji to choose stone.", inline = False)
    embedVar.add_field(name=":hand_splayed: PAPER", value="React with :hand_splayed: emoji to choose paper.", inline = False)
    embedVar.add_field(name=":v: SCISSORS", value="React with :v: emoji to choose scissors.", inline = False)
    embedVar.add_field(name='Rules',value='1).You or Calender Will Get 100 point for Each Winning\n2).50 Points for Tie\n3).TimeOut:- 20secs')
    emb = await ctx.send(embed = embedVar)

    

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["✊", "🖐️","✌️","❌"]
    list1 =  ["stone", "paper", "scissor"]
    
    try:
        while True:
            play_embed = discord.Embed(title='React For Stone ✊/Paper 🖐️/Scissor ✌️/End ❌',color = 0xff9900)
            sent = await ctx.send(embed=play_embed)
            for emoji in emojis:
                await sent.add_reaction(emoji)
            
            reaction, user = await client.wait_for('reaction_add', check=check,timeout=25)


            r_choice = random.choice(list1)
            c_embed = discord.Embed(title='Choices',description=None,color=0xff9900)
            if str(reaction.emoji) == '✊':
                c_embed.add_field(name='You Choosen:',value='Stone')
                c_embed.add_field(name='Calender Choosen:',value=r_choice)
                await ctx.send(embed=c_embed)
                
                userchoice = 'stone'
            elif str(reaction.emoji) == '🖐️':
                c_embed.add_field(name='You Choosen:',value='Paper')
                c_embed.add_field(name='Calender Choosen:',value=r_choice)
                await ctx.send(embed=c_embed)
                userchoice = 'paper'
            elif str(reaction.emoji) == '✌️':
                c_embed.add_field(name='You Choosen:',value='Scissor')
                c_embed.add_field(name='Calender Choosen:',value=r_choice)
                await ctx.send(embed=c_embed)
                userchoice = 'scissor'
            elif str(reaction.emoji) == '❌':
                await ctx.send('**You Terminated the Game**')        
                break

            r_embed = discord.Embed(title='',color=0xff9900)
            await ctx.send(embed=r_embed)
            if r_choice == userchoice:
                r_embed = discord.Embed(title='Its a tie',description=None,color=0xff9900)
                await ctx.send(embed=r_embed)
                myscore = myscore+50
                botscore = botscore+50
            elif userchoice == 'stone':
                if r_choice == 'paper':
                    r_embed = discord.Embed(title='You are covered by the Bot! Bot wins',description=None,color=0xff9900)
                    await ctx.send(embed=r_embed)
                
                    botscore=botscore+100
                else:
                    
                    r_embed = discord.Embed(title='Well Done Player! You Crushed the Bot',description=None,color=0xff9900)
                    await ctx.send(embed=r_embed)
                    myscore=myscore+100
            elif userchoice == 'paper':
                if r_choice == 'scissor':
                    r_embed = discord.Embed(title='Bot Cut Down You in halves',description=None,color=0xff9900)
                    await ctx.send(embed=r_embed)
                    
                    botscore=botscore+100
                else:
                    myscore=myscore+100
                    r_embed = discord.Embed(title='You covered the Bot',description=None,color=0xff9900)
                    await ctx.send(embed=r_embed)
                    
                    
            else:
                if r_choice == 'stone':
                    botscore=botscore+100
                    r_embed = discord.Embed(title='Bot smashed You',description=None,color=0xff9900)
                    
                    await ctx.send(embed=r_embed)
                    
                    
                else:
                    myscore=myscore+100
                    r_embed = discord.Embed(title='You Cut Down The Bot! You won',description=None,color=0xff9900)
                    await ctx.send(embed=r_embed)
                    
                    

            score_embed=discord.Embed(title='SCOREBOARD',description=None,color=0xff9900)
            score_embed.add_field(name="Your Score",value=myscore)
            score_embed.add_field(name='Calender Score',value=botscore)
            await ctx.send(embed=score_embed)

        if botscore>myscore:
            title = 'Calender defeated You'
        elif botscore==myscore:
            title = 'Game tied'
        else:
            title = 'You Defeated Bot! you Won'
        res_embed=discord.Embed(title=title,description=None,color=0xff9900)
        res_embed.add_field(name='Your Total Score',value=myscore)
        res_embed.add_field(name='Calender Total Score',value=botscore)
        await ctx.send(embed=res_embed)

    except asyncio.TimeoutError:
        await ctx.send('Terminating Game Due to Timeout')




































































client.run('ODE2OTk0MjY1Mzg4NDE3MDM0.YEDDMw.U-Zq2m5PO0ZctUwcTQ0db9PoDuE')
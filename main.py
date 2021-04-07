import discord
from discord.ext import commands
import random
import asyncio
import qrcode
import PIL
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
    embed = discord.Embed(title='Currency Converter',color=discord.Color.gold())
    embed.set_thumbnail(url='https://image.freepik.com/free-vector/indian-rupee-currency-exchange_23-2148002764.jpg')
    embed.add_field(name='Currency You are Converting From:-',value=curr1,inline=False)
    embed.add_field(name='Currency You are Converting to :-',value=curr2,inline=False)
    embed.add_field(name='Currency Amount:-',value=amount,inline=False)
    embed.add_field(name=f'Value of {amount} {curr1} in {curr2}:-',value=value,inline=False)
    await ctx.send(embed=embed)





@client.command(aliases=["hlp"])
async def h(ctx):
    embed = discord.Embed(title=':grey_question: HELP :grey_question: ',description="HELP commands:grey_question: ",color=discord.Color.blurple())
    embed.add_field(name='Help Prefix',value='#',inline=False)
    embed.add_field(name='help commands',value='kick,hlp,greet,flc,rld,game,clr,box,magic ball',inline=False)
    embed.add_field(name='Magic Ball',value='command prefix **__#mg__**',inline=False)
    await ctx.send(embed=embed)



@client.command(aliases=['qrcode'])
async def qr(ctx,*,content,member:discord.Member = None):
    member = ctx.author if not member else member
    await ctx.channel.purge(limit = 1)
    await ctx.send('**CHECK YOUR DMs**')
    data=content
    qr = qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(data)
    img = qr.make_image(fill_color='white',back_color='black')
    embed = discord.Embed(title='Your Qr Code is Here',description=f'Qr code For link {content}',color=member.color,timestamps=ctx.message.created_at)
    img.save('QRcode.png')
    await member.send(embed=embed)
    await member.send(file=discord.File('QRcode.png'))
    await asyncio.sleep(1)
    #img.delete('QRcode.png')
    

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


    result_embed = discord.Embed(title='Showing Results',color=discord.Color.dark_theme())
    result_embed.set_footer(text=f"Showing Results Requested By {ctx.author}",icon_url=ctx.author.avatar_url)
    
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["1️⃣", "2️⃣","3️⃣","4️⃣","5️⃣"]

    try:
        reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)

        if str(reaction.emoji) == '1️⃣':
            result = wikipedia.page(serch_result[0])
            content = wikipedia.summary(result)
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content),inline=False)
            result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)   
        elif str(reaction.emoji) == '2️⃣':
            result = wikipedia.page(serch_result[1])
            content = wikipedia.summary(result)
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content),inline=False)
            result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)
        elif str(reaction.emoji) == '3️⃣':
            result = wikipedia.page(serch_result[2])
            content = wikipedia.summary(result)
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content),inline=False)
            result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)
        elif str(reaction.emoji) == '4️⃣':
            result = wikipedia.page(serch_result[3])
            content = wikipedia.summary(result)
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content),inline=False)
            result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)
        else:
            result = wikipedia.page(serch_result[4])
            content = wikipedia.summary(result)
            result_embed.add_field(name='Title of The Article',value=result.title,inline=False)
            result_embed.add_field(name='Content',value=str(content),inline=False)
            result_embed.set_image(url=result.images[1])
            result_embed.add_field(name='Link to the Article',value=result.url,inline=False)
            await ctx.send(embed=result_embed)
    except asyncio.TimeoutError:
        ctx.send('**Time out**')












@client.command(aliases=['sps'])
async def game(context):
    


    i = 1
    your_points = 0
    computer_points = 0

    list1 =  ["stone", "paper", "scissors"]



    embed = discord.Embed(title="Stone paper scissor game", description="Timeout is of 30 seconds" ,color=discord.Color.dark_gold())

    embed.add_field(name="Rules", value="**__Input should be in lowercase__**\n**__For Each winning you will Get 100points__**\n**__50 points for tie__**\n**__Spelling Should Be:- stone/paper/scissor__**", inline=False)

    embed.add_field(name="Input your Choice", value="Stone/Paper/Scissor", inline=True)

    embed.add_field(name="Your points", value="0", inline=True)

    embed.add_field(name="Bots points", value="0", inline=True)

    embed.add_field(name="Number of chances", value="6", inline=True)        #Loop runs 5 times

    sent = await context.send(embed=embed)


    try:

        while (i <= 6):


            msg = await client.wait_for("message", timeout=30 , check=lambda message: message.author == context.author and message.channel == context.channel and message.content)

            choice = random.choice(list1)



            if msg.content == choice:


                embed = discord.Embed(color=discord.Color.dark_gold())
                your_points = your_points + 50
                computer_points = computer_points +50



                embed.add_field(name="Score", value=f"You choose {msg.content} and Calender choose {choice}", inline=False)
                embed.add_field(name="Points", value="You Both Tried! Better Luck Next Time!", inline=False)
                await context.send(embed=embed)


            elif msg.content == 'stone' and choice == 'scissor':
                your_points = your_points + 100

                embed = discord.Embed(color=discord.Color.dark_gold())


                embed.add_field(name="Score", value=f"You choose {msg.content} and Bot choose {choice}", inline=False)

                embed.add_field(name="Points", value="You get 100 point", inline=False)

                await context.send(embed=embed)

            elif msg.content == 'scissor' and choice == 'stone':
                computer_points = computer_points + 100

                embed = discord.Embed(color=discord.Color.dark_gold())


                embed.add_field(name="Score", value=f"You choose {msg.content} and Bot choose {choice}", inline=False)

                embed.add_field(name="Points", value= "Bot gets 100 point", inline=False)


                await context.send(embed=embed)

            elif msg.content == 'paper' and choice == 'stone':
                
                your_points = your_points + 100

                embed = discord.Embed(color=discord.Color.dark_gold())


                embed.add_field(name="Score", value=f"You choose {msg.content} and Bot choose {choice}", inline=False)

                embed.add_field(name="Points", value="You get 100 point", inline=False)

                await context.send(embed=embed)

            elif msg.content == 'stone' and choice == 'paper':
                computer_points = computer_points + 100


                embed = discord.Embed(color=discord.Color.dark_gold())



                embed.add_field(name="Score", value=f"You chose {msg.content} and Bot chose {choice}", inline=False)

                embed.add_field(name="Points", value="Bot gets 100 point", inline=False)

                await context.send(embed=embed)

            elif msg.content == 'scissor' and choice == 'paper':
                your_points = your_points + 100


                embed = discord.Embed(color=discord.Color.dark_gold())


                embed.add_field(name="Score", value=f"You chose {msg.content} and Bot chose {choice}", inline=False)

                embed.add_field(name="Points", value="You get 100 point", inline=False)

                await context.send(embed=embed)

            elif msg.content == 'paper' and choice == 'scissor':
                computer_points = computer_points + 100



                embed = discord.Embed(color=discord.Color.teal())


                embed.add_field(name="Score", value=f"You chose {msg.content} and Bot chose {choice}", inline=False)

                embed.add_field(name="Points", value="Bot gets 100 point", inline=False)


                await context.send(embed=embed)



            else:
                embed = discord.Embed(title="Invalid input",description="Try again! Input stone\paper\scissors", color=discord.Color.dark_gold())

                await context.send(embed=embed)


                continue


            embed = discord.Embed(color=discord.Color.dark_gold())
            if 6 - i == 0:
                embed.add_field(name="Chances left", value="0", inline=False)
            else:
                embed.add_field(name="Chances Left", value=f"{6-i}, Please input your choice again", inline=False)
            await context.send(embed=embed)

            i = i + 1

        if i > 6:
            # print("Game over""\n")
            embed = discord.Embed(title="**__GAME OVER __**", color=discord.Color.dark_gold())
            # await context.send("Game over")
            await context.send(embed=embed)

            embed = discord.Embed(title="Scorecard", color=discord.Color.dark_gold())
            embed.add_field(name="Players Score", value=f"Your score:{your_points}\nBot's score:{computer_points}\n", inline=False)
            if computer_points > your_points:
                # print("The computer has won and you have lost")
                embed.add_field(name="Final result", value=f"Bot has won and {context.author.mention} has lost", inline=False)
                await context.send(embed=embed)
            elif your_points > computer_points:
                # print("You have won the round and the computer has lost ")
                embed.add_field(name="Final result", value=f" {context.author.mention} has won and Bot has lost", inline=False)
                await context.send(embed=embed)
            else:
                # print("It was a TIE")
                embed.add_field(name="Final result", value="No One Won ! You Both are Noob!", inline=False)

                await context.send(embed=embed)


    #  Bot will terminate the process if no input is received from the user
    except asyncio.TimeoutError:
        await sent.delete()
        embed = discord.Embed(title="Terminating the game due to timeout , Respond in Time lol",description=None,color=discord.Color.dark_magenta)
        await context.send(embed=embed)


























































client.run('ODE2OTk0MjY1Mzg4NDE3MDM0.YEDDMw.U-Zq2m5PO0ZctUwcTQ0db9PoDuE')
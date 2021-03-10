import discord
from discord.ext import commands
import random
import asyncio

client = commands.Bot(command_prefix="#")
coin = ['HEADs','TAILS']
dice = ['1','2','3','4','5']
magic_ball = ['As I see it, yes.','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Dont count on it','It is certain','It is decidedly so']
@client.event
async def on_ready():
    print(" Bot is ready")

x =  'On '+str(len(client.guilds)) + ' Servers'
#print(x)

#discod presense
async def ch_pr():
    await client.wait_until_ready()
    statues = ['Discord.py',x,'help#','Under DevelopMent','sleeping']
    
    while not client.is_closed():
        status = random.choice(statues)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(10)
client.loop.create_task(ch_pr())

    
@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason="No reason Provided"):
    embed = discord.Embed(title = "kick", description = str(member.mention)+" has been kicked from "+ str(), color=discord.Color.red())
    await member.kick(reason=reason)
    await ctx.send(embed=embed)
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
    embed = discord.Embed(title = 'Rolling a Dice',description="Try Your Luck",color=discord.Color.orange())
    embed.add_field(name='you Gotta:--',value=str(d),inline=True)
   #embed.set_footer(test='Requested By '+ str(url = member.avatar_url))
    await ctx.send(embed=embed)

@client.command(aliases=['Flp'])
async def flp(ctx):
    c = random.choice(coin)
    embed = discord.Embed(title='Fliping a Coin',description="Try your Luck",color=discord.Color.orange())
    embed.add_field(name='You Got ',value=str(c))
    await ctx.send(embed=embed)


@client.command(aliases=['clr'])
@commands.has_permissions(manage_messages = True)
@commands.has_permissions(manage_channels = True)
async def clear(ctx,amount=2):
    embed = discord.Embed(title='Deleting Messages',description='Messages Deleted Succesfully',color=discord.Color.dark_magenta())
    await ctx.channel.purge(limit = amount)
    await ctx.send(embed=embed)

#@client.command()
#async def userinfo(ctx,member : discord.Member = *):
 #   embed = discord.Embed(title='Userinfo Requested By-'+str(member.mention),description="Returns User Account Information",color=discord.Color.blue())
  #  embed.add_field(name="User Name",value=member.name,inline=True)
   # await ctx.send(embed=embed)
    
@client.command(aliases=['box'])
async def Box(ctx):
    a = random.choice(dice)
    await ctx.send(a)


@client.command(aliases=["hlp"])
async def h(ctx):
    embed = discord.Embed(title=':grey_question: HELP :grey_question: ',description="HELP commands:grey_question: ",color=discord.Color.blurple())
    embed.add_field(name='help commands',value='kick,hlp,greet,flp,rld,game,clr,box,magic ball')
    await ctx.send(embed=embed)



@client.command(aliases=['magicball'])
async def mb(ctx):
    embed = discord.Embed(title='Magic Ball',description='you will get 10 seconds to Ask in your Mind',color=discord.Color.dark_purple())
    embed.set_thumbnail(url='https://ibb.co/zXh4K2L')
    embed.add_field(name='Get Advised',value='Ask Any question in your mind and Bot will answer and boost Your confidence')
    await ctx.send(embed=embed)
    await asyncio.sleep(10)
    magic_answer = random.choice(magic_ball)
    embed = discord.Embed(title='Your Answer is ',description=magic_answer,color=discord.Color.dark_purple())
    embed.set_thumbnail(url='https://ibb.co/zXh4K2L')
    await ctx.send(embed=embed)








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


            msg = await client.wait_for("message", timeout=30 , check=lambda message: message.author == context.author and message.channel == context.channel and message.content in  ["stone", "paper", "scissors"] )

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

            embed = discord.Embed(title="Scorecard", color=discord.Color.teal())
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


























































client.run('ODE2OTk0MjY1Mzg4NDE3MDM0.YEDDMw.FxsjJKE_XmOSia3pagtNm25OyX0')

import discord
from discord.ext import commands
import os



client = commands.Bot(command_prefix = '!')
TOKEN=''

@client.event
async def on_ready():
    print('hello !')

def prestige_calculate(x : float):
    return x-(x/5)

  
  

@client.command()
async def prestige(ctx, x:float):
  
  
  
    res = prestige_calculate(x)
    prestige=discord.Embed(title="`--prestige details--`",color=0x39FF14)
    
    prestige.set_image(url="https://media.discordapp.net/attachments/844630736362274826/993550551046426664/Prestige.png")
  

  
    
  
    
    
    if x<=0:
      prestige.add_field(name="```btw bruh u will never have that prestige in game``` ",value="XD",inline=False)
      
    elif x<=4000:
      prestige.add_field(name="```kek u are bald ,start doing pvp```",value="XD",inline=False)
      
    elif x>4000 and x<=8000:
      prestige.add_field(name="```current rank :```",value="RECRUIT or UNCLEAN",inline=False)
      
      prestige.add_field(name="```current band :```",value="brown band [5 mov speed]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545878751154226/brown_band.png")
      
      
      
      
    elif x>8000 and x<=12000:
      prestige.add_field(name="```current rank : ```",value="NOVICE or BRAWLER",inline=False)
      prestige.add_field(name="```current band :```",value="wooden band,[50 mp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545917745610782/wooden_band.png")
      
      
    elif x>12000 and x<=16000:
      prestige.add_field(name="```current rank : ```",value="SQUIRE or SLAYER",inline=False)
      prestige.add_field(name="```current band :```",value="metal band [15% IF]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545957721518171/metal_band.png")
      
      
    elif x>16000 and x<=20000:
      prestige.add_field(name="```current rank : ```",value="APPRENTICE or RAVAGER",inline=False)
      prestige.add_field(name="```current band :silver band [5 min max dmg]```",value="silver band [5 min max dmg]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545981935239219/silver_band.png")
      
      
    elif x>20000 and x<=24000:
      prestige.add_field(name="```current rank :ADEPT or BREAKER```",value="ADEPT or BREAKER",inline=False)
      prestige.add_field(name="```current band :```",value="golden band [2 hp mp regian/5s]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546001510043668/golden_band.png")
      
     
    elif x>24000 and x<=28000:
      prestige.add_field(name="```current rank: ```",value="FIERCE MASTER or RUTHLESS DEMOLISHER",inline=False)
      prestige.add_field(name="```current crown : ```",value="brown crown [5 move speed]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546031067299840/brown_crown.png")
      
      
    elif x>28000 and x<=32000:
      prestige.add_field(name="```current rank :```",value="VALIANT KNIGHT or SAVAGE MARAUDER",inline=False)
      prestige.add_field(name="```current crown: ```",value="wooden crown [30 hp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546051782983730/wooden_crown.png")
      
      
    elif x>32000 and x<=36000:
      prestige.add_field(name="```current rank :```",value="GALLANT SOLDIER or WILD REAPER",inline=False)
      prestige.add_field(name="```current crown :```",value="metal crown[15% IF]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546074310578268/metal_crown.png")
      
      
    elif x>36000 and x<=40000:
      prestige.add_field(name="```current rank ```",value="FAMOUS VETERAN or DEFIANT LIBERATOR",inline=False)
      prestige.add_field(name="```current crown : ```",value="silver crown [5% crit]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546095202410617/silver_crown.png")
      
      
    elif x>40000 and x<=44000:
      prestige.add_field(name="```current rank :```",value="FEARLESS WARDEN or BOLD CHAMPION",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown [3% haste]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546117738410086/golden_crown_1.png")
      
      
    elif x>44000 and x<=48000:
      prestige.add_field(name="```current rank : ```",value="SUPREME COMMANDER or RESTLESS HERO",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown with blue diamond [30 hp]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546138403741776/golden_crown_blue.png")
      
      
    elif x>48000:
      prestige.add_field(name="```current rank :```",value="LORD or CHOSEN",inline=False)
      prestige.add_field(name="```current crown :```",value="golden crown with red diamond [5 min max dmg]",inline=False)
      prestige.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993532525303578675/golden_crown.png")
      
      
      
    prestige.add_field(name="------IF U DONT DO PVP FOR A WEEK ------",value="😐",inline=False)
    prestige.add_field(name="Your prestige will be :",value=res,inline=False)
  
  
    
    prestige.add_field(name=" you will lose :",value=res/4,inline=False)
    
    
  
    if res<=0:
      prestige.add_field(name="```btw bruh u will never have that prestige in game``` ",value="XD",inline=False)
      await ctx.send(embed=prestige)
    elif res<=4000:
      prestige.add_field(name="```kek u are bald ,start doing pvp```",value="XD",inline=False)
      await ctx.send(embed=prestige)
    elif res>4000 and res<=8000:
      prestige.add_field(name="```u will be RECRUIT or UNCLEAN ```",value="[brown band] [5 move speed]",inline=False)
      await ctx.send(embed=prestige)
      
      
      
    elif res>8000 and res<=12000:
      prestige.add_field(name="```u will be NOVICE or BRAWLER ```",value="[wooden band] [50 mp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>12000 and res<=16000:
      prestige.add_field(name="```u will be SQUIRE or SLAYER ```",value="[metal band] [15% IF]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>16000 and res<=20000:
      prestige.add_field(name="```u will be APPRENTICE or RAVAGER ```",value="[silver band] [5 min max dmg]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>20000 and res<=24000:
      prestige.add_field(name="```u will be ADEPT or BREAKER ```",value="[golden band] [2 hp mp regain /5s]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>24000 and res<=28000:
      prestige.add_field(name="```u will be FIERCE MASTER or RUTHLESS DEMOLISHER ```",value="[brown crown] [5 move speed]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>28000 and res<=32000:
      prestige.add_field(name="```u will be VALIANT KNIGHT or SAVAGE MARAUDER ```",value="[wooden crown] [30hp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>32000 and res<=36000:
      prestige.add_field(name="```u will be GALLANT SOLDIER or WILD REAPER ```",value="[metal crown] [15% IF]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>36000 and res<=40000:
      prestige.add_field(name="```u will be FAMOUS VETERAN or DEFIANT LIBERATOR ```",value="[silver crown] [5% crit]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>40000 and res<=44000:
      prestige.add_field(name="```u will be FEARLESS WARDEN or BOLD CHAMPION ```",value="[golden crown] [3% haste]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>44000 and res<=48000:
      prestige.add_field(name="```u will be SUPREME COMMANDER or RESTLESS HERO ```",value="[golden crown with blue gem] [30 hp]",inline=False)
      await ctx.send(embed=prestige)
      
    elif res>48000:
      prestige.add_field(name="```u will be LORD or CHOSEN ```",value="[golden crown with red gem] [5 min max dmg]",inline=False)
      prestige.add_field(name="```congrats! :D u have achieved top rank , mantain it by doing pvp and obelisk```",value="🥳",inline=False)
      
      await ctx.send(embed=prestige)

@client.command()
async def p(ctx, x:float):
  
  
  
    res = prestige_calculate(x)
    p=discord.Embed(title="`--prestige details--`",color=0x39FF14)
    p.set_image(url="https://media.discordapp.net/attachments/844630736362274826/993550551046426664/Prestige.png")
    

  
    
  
    
    
    if x<=0:
      p.add_field(name="```btw bruh u will never have that p in game``` ",value="XD",inline=False)
      
    elif x<=4000:
      p.add_field(name="```kek u are bald ,start doing pvp```",value="XD",inline=False)
      
    elif x>4000 and x<=8000:
      p.add_field(name="```current rank :```",value="RECRUIT or UNCLEAN",inline=False)
      
      p.add_field(name="```current band :```",value="brown band [5 mov speed]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545878751154226/brown_band.png")
      
      
      
      
    elif x>8000 and x<=12000:
      p.add_field(name="```current rank : ```",value="NOVICE or BRAWLER",inline=False)
      p.add_field(name="```current band :```",value="wooden band,[50 mp]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545917745610782/wooden_band.png")
      
      
    elif x>12000 and x<=16000:
      p.add_field(name="```current rank : ```",value="SQUIRE or SLAYER",inline=False)
      p.add_field(name="```current band :```",value="metal band [15% IF]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545957721518171/metal_band.png")
      
      
    elif x>16000 and x<=20000:
      p.add_field(name="```current rank : ```",value="APPRENTICE or RAVAGER",inline=False)
      p.add_field(name="```current band :silver band [5 min max dmg]```",value="silver band [5 min max dmg]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993545981935239219/silver_band.png")
      
      
    elif x>20000 and x<=24000:
      p.add_field(name="```current rank :ADEPT or BREAKER```",value="ADEPT or BREAKER",inline=False)
      p.add_field(name="```current band :```",value="golden band [2 hp mp regian/5s]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546001510043668/golden_band.png")
      
     
    elif x>24000 and x<=28000:
      p.add_field(name="```current rank: ```",value="FIERCE MASTER or RUTHLESS DEMOLISHER",inline=False)
      p.add_field(name="```current crown : ```",value="brown crown [5 move speed]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546031067299840/brown_crown.png")
      
      
    elif x>28000 and x<=32000:
      p.add_field(name="```current rank :```",value="VALIANT KNIGHT or SAVAGE MARAUDER",inline=False)
      p.add_field(name="```current crown: ```",value="wooden crown [30 hp]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546051782983730/wooden_crown.png")
      
      
    elif x>32000 and x<=36000:
      p.add_field(name="```current rank :```",value="GALLANT SOLDIER or WILD REAPER",inline=False)
      p.add_field(name="```current crown :```",value="metal crown[15% IF]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546074310578268/metal_crown.png")
      
      
    elif x>36000 and x<=40000:
      p.add_field(name="```current rank ```",value="FAMOUS VETERAN or DEFIANT LIBERATOR",inline=False)
      p.add_field(name="```current crown : ```",value="silver crown [5% crit]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546095202410617/silver_crown.png")
      
      
    elif x>40000 and x<=44000:
      p.add_field(name="```current rank :```",value="FEARLESS WARDEN or BOLD CHAMPION",inline=False)
      p.add_field(name="```current crown :```",value="golden crown [3% haste]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546117738410086/golden_crown_1.png")
      
      
    elif x>44000 and x<=48000:
      p.add_field(name="```current rank : ```",value="SUPREME COMMANDER or RESTLESS HERO",inline=False)
      p.add_field(name="```current crown :```",value="golden crown with blue diamond [30 hp]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993546138403741776/golden_crown_blue.png")
      
      
    elif x>48000:
      p.add_field(name="```current rank :```",value="LORD or CHOSEN",inline=False)
      p.add_field(name="```current crown :```",value="golden crown with red diamond [5 min max dmg]",inline=False)
      p.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/993532525303578675/golden_crown.png")
      
      
      
    p.add_field(name="------IF U DONT DO PVP FOR A WEEK ------",value="😐",inline=False)
    p.add_field(name="Your p will be :",value=res,inline=False)
  
  
    
    p.add_field(name=" you will lose :",value=res/4,inline=False)
    
    
  
    if res<=0:
      p.add_field(name="```btw bruh u will never have that p in game``` ",value="XD",inline=False)
      await ctx.send(embed=p)
    elif res<=4000:
      p.add_field(name="```kek u are bald ,start doing pvp```",value="XD",inline=False)
      await ctx.send(embed=p)
    elif res>4000 and res<=8000:
      p.add_field(name="```u will be RECRUIT or UNCLEAN ```",value="[brown band] [5 move speed]",inline=False)
      await ctx.send(embed=p)
      
      
      
    elif res>8000 and res<=12000:
      p.add_field(name="```u will be NOVICE or BRAWLER ```",value="[wooden band] [50 mp]",inline=False)
      await ctx.send(embed=p)
      
    elif res>12000 and res<=16000:
      p.add_field(name="```u will be SQUIRE or SLAYER ```",value="[metal band] [15% IF]",inline=False)
      await ctx.send(embed=p)
      
    elif res>16000 and res<=20000:
      p.add_field(name="```u will be APPRENTICE or RAVAGER ```",value="[silver band] [5 min max dmg]",inline=False)
      await ctx.send(embed=p)
      
    elif res>20000 and res<=24000:
      p.add_field(name="```u will be ADEPT or BREAKER ```",value="[golden band] [2 hp mp regain /5s]",inline=False)
      await ctx.send(embed=p)
      
    elif res>24000 and res<=28000:
      p.add_field(name="```u will be FIERCE MASTER or RUTHLESS DEMOLISHER ```",value="[brown crown] [5 move speed]",inline=False)
      await ctx.send(embed=p)
      
    elif res>28000 and res<=32000:
      p.add_field(name="```u will be VALIANT KNIGHT or SAVAGE MARAUDER ```",value="[wooden crown] [30hp]",inline=False)
      await ctx.send(embed=p)
      
    elif res>32000 and res<=36000:
      p.add_field(name="```u will be GALLANT SOLDIER or WILD REAPER ```",value="[metal crown] [15% IF]",inline=False)
      await ctx.send(embed=p)
      
    elif res>36000 and res<=40000:
      p.add_field(name="```u will be FAMOUS VETERAN or DEFIANT LIBERATOR ```",value="[silver crown] [5% crit]",inline=False)
      await ctx.send(embed=p)
      
    elif res>40000 and res<=44000:
      p.add_field(name="```u will be FEARLESS WARDEN or BOLD CHAMPION ```",value="[golden crown] [3% haste]",inline=False)
      await ctx.send(embed=p)
      
    elif res>44000 and res<=48000:
      p.add_field(name="```u will be SUPREME COMMANDER or RESTLESS HERO ```",value="[golden crown with blue gem] [30 hp]",inline=False)
      await ctx.send(embed=p)
      
    elif res>48000:
      p.add_field(name="```u will be LORD or CHOSEN ```",value="[golden crown with red gem] [5 min max dmg]",inline=False)
      p.add_field(name="```congrats! :D u have achieved top rank , mantain it by doing pvp and obelisk```",value="🥳",inline=False)
      
      await ctx.send(embed=p)
       

    
    
    
@client.command()
async def gloom(ctx):
  gloom=discord.Embed(title="```--GLOOMFURY WORLD BOSS TIMINGS--```",color=0x7F00FF)
  gloom.add_field(name="`All times based on UTC`",value="`[Coordinated Universal Time]`",inline=False)
  gloom.add_field(name="If u want to convert UTC into other time zones click below 🔽",value="https://savvytime.com/converter/utc",inline=False)
  gloom.set_image(url="https://media.discordapp.net/attachments/844630736362274826/991729935335034972/utc_gloom_border_sharpened.png")
  gloom.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/991563829790126151/unknown.png")
  await ctx.send(embed=gloom)
                      
                      

   
 

@client.command()
async def helpme(ctx):
  
  helpme=discord.Embed(title="PRESTIGE AND DEFENSE BOT",description="```COOL DISCORD BOT WHICH EASE YOUR TASK IN CALCULATIONS OF HORDES GAME```",color=0x4dff4d)
  
  
  helpme.set_author(name="Datablaze",icon_url="https://media.discordapp.net/attachments/844630736362274826/980888307728809994/speedy2.png?width=580&height=580")
  helpme.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/924693581137076225/discord-avatar-512-BU83E.png")
  
  helpme.add_field(name="```!prestige <amount> [or] !p <amount>```",value="It shows prestige details",inline=False)
  helpme.add_field(name="------------",value="SOME ADDITIONAL COMMANDS",inline=False)
  helpme.add_field(name="```!defense <enter your def> <incoming dmg> <your hp>```",value="It shows dmg u will take after reduction,also shows if u will be 1 shotted or not",inline=False)
  helpme.add_field(name="```!haste <enter your haste> <enter cast time or cooldown>```",value="shows u remaining cast time or remianing cooldown",inline=False)
  helpme.add_field(name="```!gloom```",value="It shows world boss details",inline=False)
  helpme.add_field(name="```!dps <class name> <min> <max> <haste> <crit>```",value="shows u approx gloom dps",inline=False)
  helpme.add_field(name="```!map```",value="shows u all 3 maps with monster levels",inline=False)
  helpme.add_field(name="```!obe```",value="shows obelisk spots",inline=False)
 
  await ctx.send(embed=helpme)




@client.command()
async def haste(ctx,x:float, y:float):
  t=y
  z=1/(1+(x/100))*100
  y=y*z/100
  
  haste=discord.Embed(title="```--Haste & Cooldown--```",color=0x39FF14)
  haste.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/981582799297458236/hordes_presskit_real.png")
  haste.add_field(name="Remaining cast time or cooldown is :",value=y,inline=False)
  haste.add_field(name="Cast time or cooldown reduced is :",value=t-y,inline=False)
  await ctx.send(embed=haste)
  

@client.command()
async def test(ctx,x:str):
  
  await ctx.send("your text is `{}`".format(x))

@client.command()
async def defense(ctx,i:float,j:float,z:float):
  defense=discord.Embed(title="```--Defense Report--```",color=0x39FF14)
  defense.add_field(name="------------------------⚔️--------------------------",value="```--ENTERED DETAILS--```",inline=False)
  defense.add_field(name="Your defense:",value=i,inline=True)
  defense.add_field(name="Entered incoming dmg :",value=j,inline=True)
  defense.add_field(name="Your hp :",value=z,inline=True)
  defense.add_field(name="---------------------------⚔️----------------------------",value="```--CALCULATED DETAILS--```",inline=False)
  defense.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/981582799297458236/hordes_presskit_real.png")
  defense.set_footer(text="usage: !defense <enter your def> <incoming damage> <your hp>")
  
  
  
  if(i<=310000):
    l=(1 - (1/(2.71828**(i*0.0022))))*0.87
    def_red=l*100
    
  else:
    await ctx.send("```too much def man ! overflow error 💀```")
    
    
  
  
  reduc=j*(def_red/100)
  inc_dmg=j-reduc
  
  
  
  defense.add_field(name="Finally u will take [approx]🛡️:",value=inc_dmg,inline=True)
  
  defense.add_field(name="Dmg reduction [%]:",value=def_red,inline=True)
  defense.add_field(name="Intake dmg reduced:",value=j-inc_dmg,inline=True)
  
  if (z-inc_dmg)<=0:
    defense.add_field(name="u will be 1 SHOTTED ",value="😭",inline=False)
    defense.add_field(name="FUN FACT :  AT DMG GREATER THAN THIS U WILL BE 1 SHOTTED ",value=(100*z)/(100-def_red),inline=False)
    defense.set_image(url="https://media.discordapp.net/attachments/844630736362274826/992454719215771688/1_shotted_resize_hd_yes.png")
    
    
    
    await ctx.send(embed=defense)
  else:
    k=z-inc_dmg
    inc_dmg=format(inc_dmg,".4f")
    k=format(k,".4f")
    defense.add_field(name="U will NOT be 1 shotted 😀[u will be left with below hp]",value=k,inline=False)
    defense.add_field(name="FUN FACT :  AT DMG GREATER THAN THIS U WILL BE 1 SHOTTED ",value=(100*z)/(100-def_red),inline=False)
    
    defense.set_image(url="https://media.discordapp.net/attachments/844630736362274826/992454744515805266/1_shotted_resize_hd_1_no.png")
    await ctx.send(embed=defense)


@client.command()
async def d(ctx,i:float,j:float,z:float):
  defense=discord.Embed(title="```--Defense Report--```",color=0x39FF14)
  defense.add_field(name="------------------------⚔️--------------------------",value="```--ENTERED DETAILS--```",inline=False)
  defense.add_field(name="Your defense:",value=i,inline=True)
  defense.add_field(name="Entered incoming dmg :",value=j,inline=True)
  defense.add_field(name="Your hp :",value=z,inline=True)
  defense.add_field(name="---------------------------⚔️----------------------------",value="```--CALCULATED DETAILS--```",inline=False)
  defense.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/981582799297458236/hordes_presskit_real.png")
  defense.set_footer(text="usage: !defense <enter your def> <incoming damage> <your hp>")
  
  
  
  if(i<=310000):
    l=(1 - (1/(2.71828**(i*0.0022))))*0.87
    def_red=l*100
    
  else:
    await ctx.send("```too much def man ! overflow error 💀```")
    
    
  
  
  reduc=j*(def_red/100)
  inc_dmg=j-reduc
  
  
  
  defense.add_field(name="Finally u will take [approx]🛡️:",value=inc_dmg,inline=True)
  
  defense.add_field(name="Dmg reduction [%]:",value=def_red,inline=True)
  defense.add_field(name="Intake dmg reduced:",value=j-inc_dmg,inline=True)
  
  if (z-inc_dmg)<=0:
    defense.add_field(name="u will be 1 SHOTTED ",value="😭",inline=False)
    defense.add_field(name="FUN FACT :  AT DMG GREATER THAN THIS U WILL BE 1 SHOTTED ",value=(100*z)/(100-def_red),inline=False)
    defense.set_image(url="https://media.discordapp.net/attachments/844630736362274826/992454719215771688/1_shotted_resize_hd_yes.png")
    
    
    
    await ctx.send(embed=defense)
  else:
    k=z-inc_dmg
    inc_dmg=format(inc_dmg,".4f")
    k=format(k,".4f")
    defense.add_field(name="U will NOT be 1 shotted 😀[u will be left with below hp]",value=k,inline=False)
    defense.add_field(name="FUN FACT :  AT DMG GREATER THAN THIS U WILL BE 1 SHOTTED ",value=(100*z)/(100-def_red),inline=False)
    
    defense.set_image(url="https://media.discordapp.net/attachments/844630736362274826/992454744515805266/1_shotted_resize_hd_1_no.png")
    await ctx.send(embed=defense)

@client.command()
async def map(ctx):
  map=discord.Embed(title="```--GUARDSTONE--```",color=0x39FF14)
  map.set_image(url="https://cdn.discordapp.com/attachments/221772925282287627/1002570697274556486/Guardstone_Mob_Levels.png?width=580&height=580")
  await ctx.send(embed=map)
  map=discord.Embed(title="```--HEADLESS--```",color=0x39FF14)
  map.set_image(url="https://cdn.discordapp.com/attachments/221772925282287627/1002570697631084564/Headless_Mob_Levels.png?width=580&height=580")
  await ctx.send(embed=map)
  
  map=discord.Embed(title="```--FAIVEL--```",color=0x39FF14)
  map.set_image(url="https://cdn.discordapp.com/attachments/221772925282287627/1002570697979219999/Faivel_Mob_Levels.png?width=580&height=580")
  await ctx.send(embed=map)

@client.command()
async def obe(ctx):
  obe=discord.Embed(title="```OBELISK SPOTS```",color=0x39FF14)
  obe.set_image(url="https://media.discordapp.net/attachments/221772925282287627/1002585345185034340/Obelisk_Spots.png?width=580&height=580")
  await ctx.send(embed=obe)

@client.command()
async def dps(ctx,class1:str,min:float,max:float,haste:float,crit:float):
  
  dps=discord.Embed(title="```APPROX GLOOM DPS```",color=0x39FF14)
  dps.set_thumbnail(url="https://media.discordapp.net/attachments/844630736362274826/991563829790126151/unknown.png")
  
  
  dps.set_footer(text="It depends on many other factors like duration, skill set etc")
  dmg=((min+max)/2)*((100+crit)/100)*((haste+100)/100)
  
  if(class1=="a" or class1=="archer" or class1=="m" or class1=="mage"):
    
    dps.add_field(name="--------------------------------------------------------------------", value="```--Before buffs--```",inline=False)
    dps.add_field(name="Min", value=min,inline=True)
    dps.add_field(name="Max", value=max,inline=True)
    dps.add_field(name="Haste", value=haste,inline=True)
    dps.add_field(name="Crit", value=crit,inline=True)
    dps.add_field(name="----------------------------------------------------------------------------", value="```--After buffs--```",inline=False)
    dps.add_field(name="Min", value=min+20,inline=True)
    dps.add_field(name="Max", value=max+33,inline=True)
    dps.add_field(name="haste [temp+canine]", value=haste+52,inline=True)
    dps.add_field(name="crit", value=crit+12,inline=True)
    
    
    dps.add_field(name="Approx gloom DPS :", value=dmg*3.4,inline=False)
    dps.add_field(name="NOTE: Its just approx DPS", value="Its just to get rough idea",inline=False)
    await ctx.send(embed=dps)
  elif(class1=="w" or class1=="warrior"):
     dps.add_field(name="-------------------------------------------------------------", value="```--Before buffs--```",inline=False)
     dps.add_field(name="Min", value=min,inline=True)
     dps.add_field(name="Max", value=max,inline=True)
     dps.add_field(name="Haste", value=haste,inline=False)
     dps.add_field(name="Crit", value=crit,inline=True)
     dps.add_field(name="-----------------------------------------------------------------------------------", value="```--After buffs--```",inline=False)
     dps.add_field(name="Min", value=min+20,inline=True)
     dps.add_field(name="Max", value=max+33,inline=True)
     dps.add_field(name="Haste [temp+canine]", value=haste+52,inline=True)
     dps.add_field(name="Crit", value=crit+12,inline=True)
     dps.add_field(name="Approx gloom DPS :", value=dmg*4.25,inline=False)
     dps.add_field(name="NOTE: Its just approx DPS", value="Its just to get rough idea",inline=False)
     await ctx.send(embed=dps)
  elif(class1=="s" or class1=="shaman"):
    dps.add_field(name="sorry! HPS is cuurently not available", value="😢 refer scout bot ",inline=False)
    await ctx.send(embed=dps)
  
  else:
    dps.add_field(name="Invalid syntax", value="usage : !dps <enter ur class > <min> <max> <haste> <crit>",inline=False)
    await ctx.send(embed=dps)
    
    


@client.command()
async def datablaze(ctx):
    datablaze=discord.Embed(title="```HELLO ITS ME !```",color=0x39FF14)
    datablaze.set_image(url="https://media.discordapp.net/attachments/822116199877181533/1014480517145559100/unknown.png")
    await ctx.send(embed=datablaze)
    
@client.command()
async def wyrm(ctx):
    wyrm=discord.Embed(title="```WYRM```",color=0x39FF14)
    wyrm.set_image(url="https://media.discordapp.net/attachments/1003284338454048948/1006497246302445568/unknown.png")
    await ctx.send(embed=wyrm)
    
    
@client.command()
async def yt(ctx):
    yt=discord.Embed(title="```MY YOUTUBE CHANNEL```",url="https://www.youtube.com/channel/UCHk0l3XUXYRHpHo6vI2xYjg",color=0xff0000 )
    yt.add_field(name="Link :", value="https://www.youtube.com/channel/UCHk0l3XUXYRHpHo6vI2xYjg",inline=True)
    yt.set_image(url="https://media.discordapp.net/attachments/822116199877181533/1014418551349706792/unknown.png?width=899&height=580")
    yt.set_thumbnail(url="https://media.discordapp.net/attachments/924626925161422849/929703058437443624/speedy2.png?width=580&height=580")
    yt.set_footer(text="Pls make sure to subscribe :D")
    
    await ctx.send(embed=yt)
    
    
    
    
    
  
  
  
  
  
      
    
    


  


token = os.environ.get("TOKEN")

client.run(TOKEN)

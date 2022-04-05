import discord
from discord.ext import commands
import youtube_dl
import ffmpeg
from youtube_url import return_song_url
import time
from main import *
import random

class music(commands.Cog):
    def __init__(self,client) :
        self.client = client    
        self.current_song = None
        self.current_author = None
        self.current_state = False
    @commands.command()
    async def join(self,ctx) :
        if ctx.author.voice is None :
            await ctx.send("you are not in a voice channel please enter a channel first !! Purvansh bkl !!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None :
            await voice_channel.connect()
        else :
            await ctx.voice_client.move_to(voice_channel)
    
    @commands.command()
    async def diconnect(self,ctx) :
        await ctx.voice_client.disconnect()
    
    @commands.command()
    async def play(self,ctx,playlist_link) :
        players = {}
        ctx.voice_client.stop()
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client
        music_links,names,authors = combined_spotify_youtube(playlist_link) 
        for url,name,author in zip(music_links,names,authors) :
            options = "-vn -ss "+str(random.randrange(1,50))
            FFMPEG_OPTIONS = { 'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':options}

            def check(m):
                return m.content.lower() == name.lower() 

            
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl :
                # url = return_song_url(song_name)
                vc.stop()

                info = ydl.extract_info(url,download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(executable="/workspace/Python/ffmpeg-N-106490-gbb4e0f6162-linux64-gpl/bin/ffmpeg",source=url2,**FFMPEG_OPTIONS)

                vc.play(source)

                await ctx.send("You should guess now!")
                try:
                    msg = await self.client.wait_for("message", check=check ,timeout=30)
                    await msg.add_reaction("✅")                   
                    # await ctx.send(f"Hello {msg.author}! You are absolutely right")
                    if msg.author in players :
                        players[msg.author]+=1
                    else:
                        players[msg.author]=1
                except:
                    await ctx.send("Aah you missed your window of opportunity!!")
                    await ctx.send("The correct answer was :"+name+" by :"+author)
                if len(players)>0 :
                    await ctx.send("the current standings are :")
                    for i in players :
                        await ctx.send(f"{i} : "+str(players[i]))
        
        if len(players)>0 :
            Keymax = max(zip(players.values(), players.keys()))[1]
            await ctx.send(f"{Keymax} You are the winner congrats !!!!")
        else :
            await ctx.send("you guys shud get better u fckers !!")
                    
        
    @commands.command()
    async def pause(self,ctx) :
        await ctx.voice_client.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self,ctx) :
        await ctx.voice_client.resume()
        await ctx.send("resume")







def setup(client) :
    client.add_cog(music(client))
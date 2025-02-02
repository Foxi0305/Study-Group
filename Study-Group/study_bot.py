import discord
from discord.ext import commands, tasks
import random
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

study_partners = []

# Beispiel-Pomodoro-Timer-Funktion
@bot.command(name="pomodoro")
async def pomodoro(ctx):
    await ctx.send("Pomodoro-Session gestartet! 🌟 Arbeite 25 Minuten lang und mache dann 5 Minuten Pause.")
    await asyncio.sleep(25 * 60)  # 25 Minuten arbeiten
    await ctx.send("Pausenzeit! 🍵 Mach 5 Minuten Pause.")
    await asyncio.sleep(5 * 60)  # 5 Minuten Pause
    await ctx.send("Die Pause ist vorbei, Zeit weiterzulernen! 💪")

# Study Partner Funktion: Zufällig Nutzer verbinden
@bot.command(name="study_partner")
async def study_partner(ctx):
    # Alle Mitglieder im Server bekommen
    members = [member for member in ctx.guild.members if not member.bot]
    if len(members) < 2:
        await ctx.send("Es gibt nicht genügend Mitglieder für einen zufälligen Study-Partner. Mehr Leute kommen lassen!")
        return
    partner1, partner2 = random.sample(members, 2)
    await ctx.send(f"Dein Study-Partner ist {partner1.mention} und {partner2.mention}! Viel Erfolg beim Lernen! 📚")

# Fortschritts-Tracker (nur eine einfache Funktion zur Demonstration)
@bot.command(name="progress")
async def progress(ctx, progress_percentage: int):
    if 0 <= progress_percentage <= 100:
        await ctx.send(f"Dein Fortschritt: {progress_percentage}% 🎯 Keep going!")
    else:
        await ctx.send("Bitte gib eine Zahl zwischen 0 und 100 ein.")

# Event: Wenn der Bot bereit ist
@bot.event
async def on_ready():
    print(f'{bot.user} hat sich erfolgreich mit Discord verbunden!')

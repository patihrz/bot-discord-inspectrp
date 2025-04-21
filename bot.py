
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

def fetch_server_data():
    scraper = cloudscraper.create_scraper()
    try:
        response = scraper.get("")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching server data: {e}")
        return None

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} sudah online!")

@bot.command()
async def jumlah(ctx):
    data = fetch_server_data()
    if data and "Data" in data:
        jumlah = data["Data"].get("clients", 0)
        maks = data["Data"].get("sv_maxclients", 0)
        await ctx.send(f"👥 Jumlah pemain online: **{jumlah} / {maks}**")
    else:
        await ctx.send("❌ Gagal ambil data dari API.")

@bot.command()
async def list(ctx):
    data = fetch_server_data()
    if data and "Data" in data:
        players = data["Data"].get("players", [])
        if not players:
            await ctx.send("😴 Tidak ada player online saat ini.")
            return

        player_lines = [f"- {p['name']}" for p in players]
        chunks = []
        chunk = ""

        for line in player_lines:
            if len(chunk + line + "\n") > 1024:
                chunks.append(chunk)
                chunk = ""
            chunk += line + "\n"
        if chunk:
            chunks.append(chunk)

        embeds = []
        for i, c in enumerate(chunks):
            embed = discord.Embed(
                title=f"📃 Player Online ({len(players)}) - Part {i+1}",
                description=c,
                color=discord.Color.blurple()
            )
            embed.set_footer(text="Data dari FiveM API")
            embeds.append(embed)

        for embed in embeds:
            await ctx.send(embed=embed)

    else:
        await ctx.send("❌ Gagal ambil data dari API.")

@bot.command()
async def cari(ctx, *, nama: str):
    data = fetch_server_data()
    if data and "Data" in data:
        players = data["Data"].get("players", [])
        found = [p for p in players if nama.lower() in p['name'].lower()]
        if found:
            result = "\n".join(f"✅ {p['name']}" for p in found)
            await ctx.send(f"🔍 Ditemukan:\n{result}")
        else:
            await ctx.send(f"❌ Tidak ditemukan player dengan nama **{nama}**.")
    else:
        await ctx.send("❌ Gagal ambil data dari API.")

@bot.command()
async def inspect(ctx, *, nama: str):
    data = fetch_server_data()
    if data and "Data" in data:
        players = data["Data"].get("players", [])
        for p in players:
            if nama.lower() in p['name'].lower():
                embed = discord.Embed(
                    title="🔍 Player Inspect",
                    description=f"Nama: **{p['name']}**\nPing: `{p.get('ping', 'N/A')} ms`",
                    color=0x2ecc71
                )
                embed.set_footer(text="Data dari FiveM public API (via Cloudscraper)")
                await ctx.send(embed=embed)
                return
        await ctx.send(f"❌ Tidak ditemukan player dengan nama **{nama}**.")
    else:
        await ctx.send("❌ Gagal ambil data dari API.")

keep_alive()
bot.run(DISCORD_BOT_TOKEN)
import discord
from discord.ext import commands
import cloudscraper
from keep_alive import keep_alive
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

def fetch_server_data():
    scraper = cloudscraper.create_scraper()
    try:
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Status Code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching server data: {e}")
        return None

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} sudah online!")

@bot.command()
async def jumlah(ctx):
    data = fetch_server_data()
    if data and "Data" in data:
        jumlah = data["Data"].get("clients", 0)
        maks = data["Data"].get("sv_maxclients", 0)
        await ctx.send(f"👥 Jumlah pemain online: **{jumlah} / {maks}**")
    else:
        await ctx.send("❌ Gagal ambil data dari API.")

@bot.command()
async def list(ctx):
    data = fetch_server_data()
    if data and "Data" in data:
        players = data["Data"].get("players", [])
        if not players:
            await ctx.send("😴 Tidak ada player online saat ini.")
            return

        player_lines = [f"- {p['name']}" for p in players]
        chunks = []
        chunk = ""

        for line in player_lines:
            if len(chunk + line + "\n") > 1024:
                chunks.append(chunk)
                chunk = ""
            chunk += line + "\n"
        if chunk:
            chunks.append(chunk)

        embeds = []
        for i, c in enumerate(chunks):
            embed = discord.Embed(
                title=f"📃 Player Online ({len(players)}) - Part {i+1}",
                description=c,
                color=discord.Color.blurple()
            )
            embed.set_footer(text="Data dari FiveM API")
            embeds.append(embed)

        for embed in embeds:
            await ctx.send(embed=embed)

    else:
        await ctx.send("❌ Gagal ambil data dari API.")

@bot.command()
async def cari(ctx, *, nama: str):
    data = fetch_server_data()
    if data and "Data" in data:
        players = data["Data"].get("players", [])
        found = [p for p in players if nama.lower() in p['name'].lower()]
        if found:
            result = "\n".join(f"✅ {p['name']}" for p in found)
            await ctx.send(f"🔍 Ditemukan:\n{result}")
        else:
            await ctx.send(f"❌ Tidak ditemukan player dengan nama **{nama}**.")
    else:
        await ctx.send("❌ Gagal ambil data dari API.")

@bot.command()
async def inspect(ctx, *, nama: str):
    data = fetch_server_data()
    if data and "Data" in data:
        players = data["Data"].get("players", [])
        for p in players:
            if nama.lower() in p['name'].lower():
                embed = discord.Embed(
                    title="🔍 Player Inspect",
                    description=f"Nama: **{p['name']}**\nPing: `{p.get('ping', 'N/A')} ms`",
                    color=0x2ecc71
                )
                embed.set_footer(text="Data dari FiveM public API (via Cloudscraper)")
                await ctx.send(embed=embed)
                return
        await ctx.send(f"❌ Tidak ditemukan player dengan nama **{nama}**.")
    else:
        await ctx.send("❌ Gagal ambil data dari API.")

@bot.command()
async def cekrole(ctx):
    data = fetch_server_data()
    if data and "Data" in data:
        players = data["Data"].get("players", [])
        role_counts = {
            "Polisi": 0,
            "Medis": 0,
            "Pemkot": 0,
            "Media": 0,
            "ICG": 0,
            "Koki Pulau": 0,
            "Tabib Pulau": 0,
            "Lainnya": 0
        }

        for p in players:
            name = p['name'].upper()
            if name.startswith(("POLTAS", "POLSUS", "POLSIP", "POL.")):
                role_counts["Polisi"] += 1
            elif name.startswith(("EMS", "EMT")):
                role_counts["Medis"] += 1
            elif name.startswith("PEMKOT"):
                role_counts["Pemkot"] += 1
            elif name.startswith(("MEDIA", "IDP MEDIA")):
                role_counts["Media"] += 1
            elif name.startswith("ICG"):
                role_counts["ICG"] += 1
            elif name.startswith("KOKI PULAU"):
                role_counts["Koki Pulau"] += 1
            elif name.startswith("TABIB PULAU"):
                role_counts["Tabib Pulau"] += 1
            else:
                role_counts["Lainnya"] += 1

        embed = discord.Embed(
            title="📊 Jumlah Pemain per Role",
            color=discord.Color.gold()
        )

        for role, count in role_counts.items():
            embed.add_field(name=role, value=f"**{count}**", inline=False)

        embed.set_footer(text="Data dari FiveM API")
        await ctx.send(embed=embed)
    else:
        await ctx.send("❌ Gagal ambil data dari API.")

keep_alive()
bot.run(DISCORD_BOT_TOKEN)

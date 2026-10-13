import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot logado como {bot.user}")


@bot.command()
async def start(ctx):
    conselhos = [
        {
            "titulo": "💡 Economize energia",
            "descricao": "Apague as luzes quando sair de um cômodo.",
            "imagem": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "🚲 Use transportes sustentáveis",
            "descricao": "Sempre que possível, caminhe, use bicicleta ou transporte público.",
            "imagem": "https://images.unsplash.com/photo-1502744688674-c619d1586c9e?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "💧 Economize água",
            "descricao": "Feche a torneira enquanto escova os dentes e evite desperdícios.",
            "imagem": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "♻️ Recicle",
            "descricao": "Separe materiais recicláveis do lixo comum.",
            "imagem": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "🌳 Cuide das árvores",
            "descricao": "Plante árvores e cuide das áreas verdes da sua cidade.",
            "imagem": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "🔌 Desligue aparelhos",
            "descricao": "Desligue aparelhos eletrônicos quando não estiver usando.",
            "imagem": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "🥕 Evite desperdício de alimentos",
            "descricao": "Planeje suas refeições e aproveite os alimentos ao máximo.",
            "imagem": "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "🛍️ Evite sacolas descartáveis",
            "descricao": "Use sacolas reutilizáveis sempre que puder.",
            "imagem": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "🌎 Consuma com consciência",
            "descricao": "Antes de comprar algo, pense se realmente precisa daquele produto.",
            "imagem": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=800&q=80"
        },
        {
            "titulo": "🍃 Reutilize",
            "descricao": "Tente reutilizar objetos antes de jogá-los fora.",
            "imagem": "https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?auto=format&fit=crop&w=800&q=80"
        }
    ]

    conselho = random.choice(conselhos)

    embed = discord.Embed(
        title=conselho["titulo"],
        description=conselho["descricao"],
        color=discord.Color.green()
    )

    embed.set_footer(
        text="🌱 EcoAção — Cada atitude faz diferença!"
    )

    embed.set_image(url=conselho["imagem"])

    await ctx.send(embed=embed)


@bot.command()
async def hello(ctx):
    introducao = (
        "🌱 **Bem-vindo ao EcoAção!**\n\n"
        "Este bot fornece dicas para promover a sustentabilidade "
        "e a preservação do meio ambiente.\n\n"
        "Use `!start` para receber um conselho aleatório "
        "ou `!video` para encontrar vídeos sobre sustentabilidade!"
    )

    await ctx.send(introducao)


@bot.command()
async def video(ctx):
    embed = discord.Embed(
        title="🌎 Aprenda a cuidar do planeta!",
        description=(
            "Assista a vídeos sobre sustentabilidade, "
            "aquecimento global e preservação do meio ambiente."
        ),
        color=discord.Color.green()
    )

    embed.add_field(
        name="▶️ Assistir aos vídeos",
        value=(
            "[Clique aqui para assistir no YouTube]"
            "(https://www.youtube.com/watch?v=xEMAmLlZx-g)"
        ),
        inline=False
    )

    embed.set_footer(
        text="🌱 EcoAção — Cada atitude faz diferença!"
    )

    await ctx.send(embed=embed)



bot.run("SEU_TOKEN")

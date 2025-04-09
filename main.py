import discord
from discord.ext import commands
import random
import requests
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mnu(ctx):
    embed = discord.Embed(
        title="EcoBot - Comandos disponibles",
        description="Aquí tienes todos los comandos que puedes usar:",
        color=discord.Color.green()
    )
    embed.add_field(
        name="/info",
        value="Explicación sobre lo que es el cambio climático",
        inline=False
    )
    embed.add_field(
        name="/consejos",
        value="Consejos para ayudar contra el cambio climático",
        inline=False
    )
    embed.add_field(
        name="/impacto",
        value="Información sobre el impacto del cambio climático",
        inline=False
    )
    embed.add_field(
        name="/meme",
        value="Memes relacionados con el cambio climático",
        inline=False
    )
    embed.set_author(
        name="Proyecto"
    )
    
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="EcoBot - Información",
        description="Aprende un poco mas sobre el cambio climático",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="¿Qué es el cambio climático?",
        value="El cambio climático se refiere a los cambios a largo plazo en las temperaturas y patrones climáticos. Estos cambios pueden ser naturales, pero desde el siglo XIX, las actividades humanas han sido el principal motor del cambio climático, debido principalmente a la quema de combustibles fósiles (como el carbón, el petróleo y el gas), que produce gases que atrapan el calor (gases de efecto invernadero).",
        inline=False
    )
    embed.add_field(
        name="Causas principales",
        value="- Emisiones de gases de efecto invernadero\n"
        "- Deforestación\n"
        "- Uso intensivo de recursos naturales\n"
        "- Contaminación industrial\n\n",
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def consejos(ctx):
    consejos=[
        "Usa bombillas LED: Consumen hasta un 80% menos de energía que las tradicionales.",
        "Camina o usa bicicleta: Reduce las emisiones de CO2 y mejora tu salud.",
        "Recicla correctamente: Separa papel, vidrio, plástico y orgánicos.",
        "Ahorra agua: Duchas cortas y cierra el grifo cuando no lo uses.",
        "Usa bolsas reutilizables: Evita las bolsas de plástico de un solo uso.",
        "Desconecta aparatos electrónicos: Aunque estén apagados, consumen energía.",
        "Planta un árbol: Los árboles absorben CO2 y liberan oxígeno.",
        "Usa transporte público: Reduce la huella de carbono individual.",
        "Educa a otros: Comparte información sobre el cambio climático. Por ejemplo, lo que aprendas de este bot"
    ]

    consejo_alt=random.sample(consejos, 5)

    embed = discord.Embed(
        title="Consejos",
        color= 0x1abc9c
    )
    embed.add_field(
        name ="Algunos consejos para ayudar contra el cambio climatico pueden ser:",
        value = "\n\n".join([f"• {consejo}" for consejo in consejo_alt]),
        inline=False
    )

    await ctx.send(embed=embed)


@bot.command()
async def impacto(ctx):
    embed=discord.Embed(
        title="Impacto del cambio climático:",
        description="Estos son algunos de los principales impactos que tiene el cambio climático",
        color=discord.Color.red()
    )
    embed.add_field(
        name="Aumento de temperaturas",
        value="La última década fue la más cálida registrada.",
        inline=False
    )
    embed.add_field(
        name="Derretimiento de glaciares",
        value="Pérdida de hielo en los polos y montañas.",
        inline=False
    )
    embed.add_field(
        name="Aumento del nivel del mar",
        value="Amenaza a ciudades costeras e islas.",
        inline=False
    )
    embed.add_field(
        name="Fenómenos meteorológicos extremos",
        value="Más huracanes, sequías e inundaciones",
        inline=False
    )
    embed.add_field(
        name="Pérdida de biodiversidad",
        value="Muchas especies en peligro de extinción.",
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
    images = random.choice(os.listdir("PROYECTOFINALKODLAND/images"))
    with open(f'PROYECTOFINALKODLAND/images/{images}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)




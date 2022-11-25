from main.app import discord


def on_start(server):
    discord.update_commands()

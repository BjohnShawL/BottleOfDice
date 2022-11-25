import enum
from flask_discord_interactions import DiscordInteractionsBlueprint, Embed, Message, embed
from os import getenv
from .roll import process_command


class Sum(enum.Enum):
    Sum = "Sum"
    NotSum = "Not Sum"


bp = DiscordInteractionsBlueprint()


@bp.command(annotations={"dice_roll": "The dice rolled in [x]d[y] +[z] format", "sum": "To Sum, or Not to Sum"})
def roll(ctx, dice_roll: str, _sum: Sum):
    "Test function for dice rolls"
    username = ctx.author.display_name
    is_sum = {"Sum": True, "Not Sum": False}
    result = process_command(dice_roll, is_sum[_sum])

    d_embed = Embed()
    embed_fields = []
    d_embed.title = f"-- {username} has rolled the dice! --"
    d_embed.description = dice_roll
    for i, r in enumerate(result):
        d_field = embed.Field(name=f"Roll # {i + 1}", value=str(r))
        embed_fields.append(d_field)
    d_embed.fields = embed_fields

    return Message(embed=d_embed)
    # return f"Hey there {username} - You rolled {process_command(dice_roll, is_sum[sum])}"


def build_discord_routes(d, app):
    d.set_route("/interactions", app)
    # d.update_commands(guild_id=getenv("TESTING_GUILD"), app=app)

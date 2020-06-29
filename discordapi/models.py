from django.db import models
from django.db.models import CharField, BooleanField, IntegerField


# Create your models here.
class User(models.Model):
    id = CharField(max_length=250, help_text="the user's id", primary_key=True)  # TODO: Transform to snowflake
    username = CharField(max_length=250, help_text="the user's username, not unique across the platform")
    discriminator = CharField(max_length=250, help_text="the user's 4-digit discord-tag")
    avatar = CharField(max_length=250, help_text="the user's avatar hash")
    bot = BooleanField(help_text="whether the user belongs to an OAuth2 application")
    system = BooleanField(
        help_text="whether the user is an Official Discord System user (part of the urgent message system)")
    mfa_enabled = BooleanField(help_text="whether the user has two factor enabled on their account")
    locale = CharField(max_length=250, help_text="the user's chosen language option")
    verified = BooleanField(help_text="whether the email on this account has been verified")
    email = CharField(max_length=250, help_text="the user's email")
    flags = CharField(max_length=250, help_text="the flags on a user's account")
    premium_type = CharField(max_length=250, help_text="the type of Nitro subscription on a user's account")
    public_flags = CharField(max_length=250, help_text="the public flags on a user's account")


class Guild(models.Model):
    id = CharField(max_length=250, help_text="guild id", primary_key=True)
    name = CharField(max_length=250,
                     help_text="guild name (2-100 characters, excluding trailing and leading whitespace)")
    icon = CharField(max_length=250, help_text="icon hash")
    splash = CharField(max_length=250, help_text="splash hash")
    discovery_splash = CharField(max_length=250,
                                 help_text="discovery splash hash; only present for guilds with the \"DISCOVERABLE\" feature")
    owner = BooleanField(help_text="true if the user is the owner of the guild")
    owner_id = CharField(max_length=250, help_text="id of owner")
    permissions = IntegerField(
                            help_text="total permissions for the user in the guild (excludes overrides)")
    region = CharField(max_length=250, help_text="voice region id for the guild")
    afk_channel_id = CharField(max_length=250, help_text="id of afk channel")
    afk_timeout = IntegerField(help_text="afk timeout in seconds")
    embed_enabled = BooleanField(
                              help_text="true if the server widget is enabled (deprecated, replaced with widget_enabled)")
    embed_channel_id = CharField(max_length=250,
                                 help_text="the channel id that the widget will generate an invite to, or null if set to no invite (deprecated, replaced with widget_channel_id)")
    verification_level = IntegerField(help_text="verification level required for the guild")
    default_message_notifications = IntegerField(help_text="default message notifications level")
    explicit_content_filter = IntegerField(help_text="explicit content filter level")
    roles = CharField(max_length=250, help_text="roles in the guild") # TODO: Add custom model
    emojis = CharField(max_length=250, help_text="custom guild emojis") # TODO: Add custom model
    features = CharField(max_length=250, help_text="enabled guild features") # TODO: Add custom model
    mfa_level = IntegerField(max_length=250, help_text="required MFA level for the guild")
    application_id = CharField(max_length=250, help_text="application id of the guild creator if it is bot-created")
    widget_enabled = BooleanField(max_length=250, help_text="true if the server widget is enabled")
    widget_channel_id = CharField(max_length=250,
                                  help_text="?snowflake	the channel id that the widget will generate an invite to, or null if set to no invite")
    system_channel_id = CharField(max_length=250,
                                  help_text="the id of the channel where guild notices such as welcome messages and boost events are posted")
    system_channel_flags = IntegerField(max_length=250, help_text="system channel flags")
    rules_channel_id = CharField(max_length=250,
                                 help_text="the id of the channel where guilds with the \"PUBLIC\" feature can display rules and/or guidelines")
    joined_at = CharField(max_length=250, help_text="when this guild was joined at")
    large = BooleanField(help_text="true if this is considered a large guild")
    unavailable = BooleanField(help_text="true if this guild is unavailable due to an outage")
    member_count = IntegerField(help_text="total number of members in this guild")
    voice_states = CharField(max_length=250,
                             help_text="states of members currently in voice channels; lacks the guild_id key") # TODO: Add custom objects
    members = CharField(max_length=250, help_text="users in the guild") # TODO: Add custom objects
    channels = CharField(max_length=250, help_text="channels in the guild") # TODO: Add custom objects
    presences = CharField(max_length=250,
                          help_text="presences of the members in the guild, will only include non-offline members if the size is greater than large threshold") # TODO: Add custom objects
    max_presences = IntegerField(max_length=250,
                              help_text="the maximum number of presences for the guild (the default value, currently 25000, is in effect when null is returned)")
    max_members = IntegerField(max_length=250, help_text="the maximum number of members for the guild")
    vanity_url_code = CharField(max_length=250, help_text="the vanity url code for the guild")
    description = CharField(max_length=250, help_text="the description for the guild, if the guild is discoverable")
    banner = CharField(max_length=250, help_text="banner hash")
    premium_tier = IntegerField(max_length=250, help_text="premium tier (Server Boost level)")
    premium_subscription_count = IntegerField(max_length=250, help_text="the number of boosts this guild currently has")
    preferred_locale = CharField(max_length=250,
                                 help_text="the preferred locale of a guild with the \"PUBLIC\" feature; used in server discovery and notices from Discord; defaults to \"en-US\"")
    public_updates_channel_id = CharField(max_length=250,
                                          help_text="the id of the channel where admins and moderators of guilds with the \"PUBLIC\" feature receive notices from Discord")
    max_video_channel_users = IntegerField(max_length=250, help_text="the maximum amount of users in a video channel")
    approximate_member_count = IntegerField(max_length=250,
                                         help_text="approximate number of members in this guild, returned from the GET /guild/<id> endpoint when with_counts is true")
    approximate_presence_count = IntegerField(max_length=250,
                                           help_text="approximate number of non-offline members in this guild, returned from the GET /guild/<id> endpoint when with_counts is true")

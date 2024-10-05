from tortoise import fields
from tortoise.models import Model


class User(Model):
    tg_id = fields.BigIntField(primary_key=True)
    username = fields.TextField(
        null=True, description="Username of telegram user"
    )
    first_visit = fields.DatetimeField(auto_now_add=True, description="Datetime of when user first joined bot"
    )
    is_banned = fields.BooleanField(description="Whether bot won't respond to user")
    state = fields.TextField(null=True)
    data = fields.JSONField(null=True)
    class Meta:
        table = "users"
        table_description = "This table contains a list of all users"

    def __str__(self):
        return str(self.tg_id)



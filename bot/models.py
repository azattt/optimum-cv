from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(primary_key=True)
    username = fields.TextField(
        null=True, description="Username of telegram user"
    )
    first_visit = fields.DatetimeField(
        null=False, auto_now_add=True, description="Datetime of when user first joined bot"
    )

    class Meta:
        table = "users"
        table_description = "This table contains a list of all users"

    def __str__(self):
        return str(self.id)

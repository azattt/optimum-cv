from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.BigIntField(primary_key=True)
    name = fields.TextField(description="Name of the event that corresponds to an action")
    first_visit = fields.DatetimeField(
        null=False, auto_now_add=True, description="Datetime of when user first joined bot"
    )

    class Meta:
        table = "event"
        table_description = "This table contains a list of all the example events"

    def __str__(self):
        return self.name
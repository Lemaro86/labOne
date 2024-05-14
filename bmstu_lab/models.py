import uuid

from django.db import models


class Card(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    description = models.TextField()
    img = models.TextField()
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'card'
        app_label = 'bmstu_lab'

# card1 = Card.objects.create(title='Обработка помещений после ковида', description='Дэзинфекция объектов', img='./img/1.png',
#                             cost=50500, id=1)
# card2 = Card.objects.create(title='Обработка помещения от тараканов', description='Дэзинфекция объектов против тараканов',
#                             img='./img/2.jpeg', cost=45300, id=2)
# card3 = Card.objects.create(title='Обработка зелёного массива от клещей', description='Дэзинфекция леса от боррелиоза',
#                             img='./img/3.png', cost=22300, id=3)
# card4 = Card.objects.create(title='Обработка озера от комаров', description='Очистка водных угодий', img='./img/4.jpeg',
#                             cost=123111, id=4)
# card5 = Card.objects.create(title='Обработка территории от грызунов', description='Дэзинфекция от мышей, кротов и крыс',
#                             img='./img/5.png', cost=80200, id=5)

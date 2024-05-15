from django.db import models


class Service(models.Model):
    service_id = models.IntegerField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    img = models.TextField()
    cost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'service'


class Order(models.Model):
    order_id: models.IntegerField(primary_key=True)
    status = models.TextField()
    created = models.DateTimeField()
    activated = models.DateTimeField()
    completed = models.DateTimeField()
    creator_id = models.TextField()
    moderator_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'order'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    login = models.TextField()
    password = models.TextField()
    admin = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'user'


class OrderEvent(models.Model):
    order_id = models.IntegerField(),
    service_id = models.IntegerField(),

    class Meta:
        managed = False
        db_table = 'order_event'


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

from django.db import models


class Game_Type(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)



class Tournaments(models.Model):
    def __str__(self):
        return self.name

    Tournament_status = (
        ('compleated', 'compleated'),
        ('running', 'running'),
        ('late reg', 'late reg'),
        ('upcoming', 'upcoming')
    )

    Tournament_type =(
        ('freezout', 'freezout'),
        ('R&A', 'R&A'),
        ('PKO', "PKO"),
        ('Knockot', 'Knockout')
    )

    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    buy_in = models.DecimalField(max_digits=12, decimal_places=2)
    players = models.IntegerField(blank=True, null=True)
    prizepool = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(choices=Tournament_status, max_length = 30)
    type = models.CharField(choices=Tournament_type, max_length = 30)
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Tournament'
        verbose_name_plural = 'Tournaments'

class Cash_Games(models.Model):
    def __str__(self):
        return self.prices

    prices = models.CharField(max_length=50)
    players = models.IntegerField(blank=True, null=True)
    min_buy_in = models.DecimalField(max_digits=12, decimal_places=2)
    max_buy_in = models.DecimalField(max_digits=12, decimal_places=2)
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Cash_Games'
        verbose_name_plural = 'Cash_Games'

class Sit_Go(models.Model):
    def __str__(self):
        return self.name

    Status = (
        ('registering', 'registering'),
        ('running', 'running')
    )

    name = models.CharField(max_length=50)
    players = models.CharField(max_length=50)
    buy_in = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(choices=Status, max_length=30)
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Sit & Go'
        verbose_name_plural = 'Sit & Go'


class Spin(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, default = 'BLAST')
    buy_in = models.DecimalField(max_digits=12, decimal_places=2)
    total_prizepool = models.DecimalField(max_digits=12, decimal_places=2)
    blind_level = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Spin'
        verbose_name_plural = 'Spins'
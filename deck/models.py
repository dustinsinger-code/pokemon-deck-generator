from django.db import models


class Card(models.Model):

    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128, null=True, blank=True)
    card_id = models.CharField(max_length=16)


class Deck(models.Model):

    cards = models.ManyToManyField(Card, through='DeckCard')


class DeckCard(models.Model):

    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

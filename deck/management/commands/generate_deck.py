import random
import time
from django.core.management.base import BaseCommand
from django.db.models import Q
from pokemontcgsdk import RestClient, Type, Card
from deck.models import Card as CardModel, Deck, DeckCard

RestClient.configure('f29778c0-a71d-499e-a234-2f9f677900d6')


class Command(BaseCommand):

    def handle(self, *args, **options):
        ENERGY_CARD_COUNT = 10
        random_type = random.choice(Type.all())
        print("type: ", random_type)

        start_time = time.time()
        cards = Card.where(q=F'types:{random_type} supertype:pokemon')
        trainer_cards = Card.where(q='supertype:trainer')

        selected_pokemon_cards = random.sample(cards, random.randint(12, 16))
        selected_trainer_cards = random.sample(
            trainer_cards,
            60 - (len(selected_pokemon_cards) + ENERGY_CARD_COUNT)
        )
        deck = selected_pokemon_cards + selected_trainer_cards
        card_ids = []

        for card in deck:
            card_ids.append(card.id)
            CardModel.objects.get_or_create(
                card_id=card.id,
                defaults={
                    'name': card.name,
                    'type': ",".join(card.types) if card.types else None,
                    'card_id': card.id
                }
            )

        new_deck = Deck.objects.create()
        deck_cards = CardModel.objects.filter(card_id__in=card_ids)

        for card in deck_cards:
            DeckCard.objects.create(
                card=card,
                deck=new_deck
            )

        energy_card = CardModel.objects.filter(Q(name__contains=random_type) & Q(name__contains='Energy')).first()

        DeckCard.objects.create(
            card=energy_card,
            deck=new_deck,
            count=ENERGY_CARD_COUNT
        )

        for deck_card in DeckCard.objects.filter(deck=new_deck):
            for i in range(deck_card.count):
                print("_________________________________")
                print(deck_card.card.name)

        print("time: ", time.time() - start_time)


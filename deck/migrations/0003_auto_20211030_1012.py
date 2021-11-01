# Generated by Django 3.2.8 on 2021-10-30 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0002_auto_20211030_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DeckCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck.card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck.deck')),
            ],
        ),
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(through='deck.DeckCard', to='deck.Card'),
        ),
    ]

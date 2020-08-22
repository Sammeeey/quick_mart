# Generated by Django 3.0.8 on 2020-08-19 06:26

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200818_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='diet_restrictions',
        ),
        migrations.AddField(
            model_name='profile',
            name='diet_restrictions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('vegan', 'vegan'), ('vegetarian', 'vegetarian'), ('gluten-free', 'gluten-free'), ('wheat-free', 'wheat-free'), ('tree-nut-free', 'tree-nut-free'), ('soy-free', 'soy-free'), ('shellfish-free', 'shellfish-free'), ('sesame-free', 'sesame-free'), ('low-sugar', 'low-sugar'), ('no-oil-added', 'no-oil-added'), ('mustard-free', 'mustard-free')], default=['vegan'], max_length=125),
        ),
        migrations.DeleteModel(
            name='DietRestrictions',
        ),
    ]
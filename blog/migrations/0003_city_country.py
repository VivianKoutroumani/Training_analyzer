from django.db import migrations, models
import django.db.models.deletion


"""
This migration was generated when one of our group members wanted to experiment with the graphs that are currently
displayed on FitHub under the "analysis" tab. The models this migration creates (city and country) gave us access to 
dummy data, which we could manipulate and analyze without concern. Thanks to this model, the group member tasked with 
making the graphs could continue working while the other member who was tasked with making the "workout" model
refined his work. 
"""


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201118_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('population', models.PositiveIntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Country')),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-22 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app123", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={"verbose_name": "Category", "verbose_name_plural": "Categories",},
        ),
        migrations.AlterField(
            model_name="todolist", name="content", field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="category",
            field=models.ForeignKey(
                default="general",
                on_delete=django.db.models.deletion.CASCADE,
                to="app123.category",
            ),
        ),
        migrations.DeleteModel(name="Catagory",),
    ]

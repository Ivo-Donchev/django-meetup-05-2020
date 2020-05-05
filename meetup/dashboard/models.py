from django.db.models import (
    Model,
    CharField,
    IntegerField,
    TextField,
    ForeignKey,
    CASCADE
)


class Author(Model):
    name = CharField(max_length=255)
    age = IntegerField()

    author_field_1 = CharField(max_length=255)
    author_field_2 = CharField(max_length=255)
    author_field_3 = CharField(max_length=255)
    author_field_4 = CharField(max_length=255)
    author_field_5 = CharField(max_length=255)
    author_field_6 = CharField(max_length=255)
    author_field_7 = CharField(max_length=255)
    author_field_8 = CharField(max_length=255)
    author_field_9 = CharField(max_length=255)

    author_field_10 = CharField(max_length=255)
    author_field_11 = CharField(max_length=255)
    author_field_12 = CharField(max_length=255)
    author_field_13 = CharField(max_length=255)
    author_field_14 = CharField(max_length=255)
    author_field_15 = CharField(max_length=255)
    author_field_16 = CharField(max_length=255)
    author_field_17 = CharField(max_length=255)
    author_field_18 = CharField(max_length=255)
    author_field_19 = CharField(max_length=255)
    author_field_20 = CharField(max_length=255)

    author_field_20 = CharField(max_length=255)
    author_field_21 = CharField(max_length=255)
    author_field_22 = CharField(max_length=255)
    author_field_23 = CharField(max_length=255)
    author_field_24 = CharField(max_length=255)
    author_field_25 = CharField(max_length=255)
    author_field_26 = CharField(max_length=255)
    author_field_27 = CharField(max_length=255)
    author_field_28 = CharField(max_length=255)
    author_field_29 = CharField(max_length=255)
    author_field_30 = CharField(max_length=255)

    @property
    def articles_count(self):
        return self.articles.count()


class Article(Model):
    title = CharField(max_length=255)
    content = TextField()
    author = ForeignKey(
        Author,
        related_name='articles',
        on_delete=CASCADE
    )

    article_field_1 = CharField(max_length=255)
    article_field_2 = CharField(max_length=255)
    article_field_3 = CharField(max_length=255)
    article_field_4 = CharField(max_length=255)
    article_field_5 = CharField(max_length=255)
    article_field_6 = CharField(max_length=255)
    article_field_7 = CharField(max_length=255)
    article_field_8 = CharField(max_length=255)
    article_field_9 = CharField(max_length=255)

    article_field_10 = CharField(max_length=255)
    article_field_11 = CharField(max_length=255)
    article_field_12 = CharField(max_length=255)
    article_field_13 = CharField(max_length=255)
    article_field_14 = CharField(max_length=255)
    article_field_15 = CharField(max_length=255)
    article_field_16 = CharField(max_length=255)
    article_field_17 = CharField(max_length=255)
    article_field_18 = CharField(max_length=255)
    article_field_19 = CharField(max_length=255)
    article_field_20 = CharField(max_length=255)

    article_field_20 = CharField(max_length=255)
    article_field_21 = CharField(max_length=255)
    article_field_22 = CharField(max_length=255)
    article_field_23 = CharField(max_length=255)
    article_field_24 = CharField(max_length=255)
    article_field_25 = CharField(max_length=255)
    article_field_26 = CharField(max_length=255)
    article_field_27 = CharField(max_length=255)
    article_field_28 = CharField(max_length=255)
    article_field_29 = CharField(max_length=255)
    article_field_30 = CharField(max_length=255)

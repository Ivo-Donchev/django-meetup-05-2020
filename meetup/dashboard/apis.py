from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import Serializer, CharField, IntegerField
from django.db import models

from .models import Article, Author


class Demo1Api(APIView):
    class ArticleSerializer(Serializer):
        title = CharField(max_length=255)
        content = CharField(max_length=255)
        author_name = CharField(max_length=255, source='author.name')

    def get(self, request):
        """
        Get first 200 articles with the author_name
        """
        queryset = Article.objects.all()[:200]

        serializer = self.ArticleSerializer(
            queryset,
            many=True
        )

        return Response(data=serializer.data)


class Demo2Api(APIView):
    def get(self, request):

        # Are these equal ?
        print(Article.objects.all() == Article.objects.all())

        # Are these equal ?
        print(list(Article.objects.all()) == list(Article.objects.all()))

        articles = Article.objects.all()  # Am I making a query ?

        for article in articles:  # Am I making a query ?
            pass

        for article in articles:  # Am I making a query ?
            pass

        for article in articles.all():  # Am I making a query ?
            pass

        return Response()


class Demo3Api(APIView):
    class AuthorSerializer(Serializer):
        name = CharField()
        articles_count = IntegerField(
            # source='_articles_count'
        )

    def get(self, request):
        queryset = Author.objects.all()[:100]
        # queryset = Author.objects\
        #     .annotate(_articles_count=models.Count('articles'), group=models.F('id'))

        serializer = self.AuthorSerializer(queryset, many=True)

        return Response(data=serializer.data)

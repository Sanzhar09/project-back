from django.shortcuts import render


from api.models import Category, Article, Publisher
from api.serializers import CategorySerializer, ArticleSerialize, PublisherSerializer
from rest_framework.views import APIView, status
from rest_framework.response import Response

class CategoryListView(APIView):
    def get(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        Category.objects.create(
            name = request.data['name']
        )
        return Response({"":"successs"}, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view
@api_view(['GET'])
def articles(request):
    articles = Article.objects.all()
    serializer = ArticleSerialize(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def articles_for_publisher(request):
    try:
        category = Category.objects.get(name=request.data['category'])
        author = Publisher.objects.get(name=request.data['author'])
    except:
        category = Category.objects.create(name=request.data['category'])
        author = Publisher.objects.create(name=request.data['author'])

    Article.objects.create(
        category = category,
        author = author,
        title = request.data['title'],
        image = request.data['image'],
        text = request.data['text']
    )
    return Response({"":""}, status=status.HTTP_200_OK)

class EditorView(APIView):
    def put(self, request, id):
        article = Article.objects.get(id=request.data['id'])
        article.title = request.data['title']
        article.text = request.data['text']

        article.save()
        return Response({"":""}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        article = Article.objects.get(id=request.data['id'])
        article.delete()
        return Response({"":""}, status=status.HTTP_200_OK)


from django.urls import path
from graphene_django.views import GraphQLView
from user.schema import schema

urlpatterns = [
    path("user/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
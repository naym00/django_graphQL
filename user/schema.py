import graphene
from graphene_django.types import DjangoObjectType
from django.contrib.auth.hashers import make_password
from user import models as M_USER
    
class UserType(DjangoObjectType):
    class Meta:
        model = M_USER.User
        fields = '__all__'

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_id = graphene.Field(UserType, id=graphene.Int())
    user_username = graphene.Field(UserType, username=graphene.String())

    def resolve_all_users(self, info):
        return M_USER.User.objects.all()
    
    def resolve_user_id(self, info, id):
        return M_USER.User.objects.get(pk=id)
    
    def resolve_user_username(self, info, username):
        return M_USER.User.objects.get(username=username)
    
class CreateUser(graphene.Mutation):
    class Arguments:
        password = graphene.String(required=True)
        username = graphene.String(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        email = graphene.String(required=False)
        
        gender = graphene.String(required=False)
        phone = graphene.String(required=False)
        designation = graphene.Int(required=False)
        religion = graphene.Int(required=False)
        shift = graphene.Int(required=False)

    user = graphene.Field(UserType)

    def mutate(self, info, password, username, **kwargs):
        user = M_USER.User.objects.create(
            password=make_password(password),
            username=username,
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'),
            email=kwargs.get('email'),
            gender=kwargs.get('gender'),
            phone=kwargs.get('phone'),
            designation=M_USER.Designation.objects.get(id=kwargs.get('designation')),
            religion=M_USER.Religion.objects.get(id=kwargs.get('religion')),
            shift=M_USER.Shift.objects.get(id=kwargs.get('shift'))
        )
        return CreateUser(user=user)
    
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
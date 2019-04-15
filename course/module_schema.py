import graphene
from graphene_django import DjangoObjectType

from course.models import Module
from course.schema import CourseInput

# create the type
class ModuleType(DjangoObjectType):
    class Meta:
        model = Module


# create the query
class Query(graphene.ObjectType):
    modules = graphene.List(ModuleType)

    def resolve_modules(self, info, **kwargs):
        rertun Modules.objects.all()


# create the mutation
class CreateModule(graphene.Mutation):
    id = graphene.Int()
    module_title = graphene.String()
    description = graphene.String()
    body = graphene.String()
    date_created = graphene.Date()
    course = graphene.Field(CourseInput)

    class Arguments:
        module_title = graphene.String()
        description = graphene.String()
        body = graphene.String()
        course_id = graphene.Int()
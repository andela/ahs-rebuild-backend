import graphene
from graphene_django import DjangoObjectType

from  course.models import Course
from users.schema import UserType


class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class Query(graphene.ObjectType):
    courses = graphene.List(CourseType)

    def resolve_courses(self, info, **kwargs):
        return Course.objects.all()

# create an input class for mutations
class CourseInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()
    

# create the mutations to create a course
class CreateCourse(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()
    date_created = graphene.Date()
    created_by = graphene.Field(UserType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()

    def mutate(self, info, title, description, **kwargs):
        user = info.context.user
        if user is None:
            raise Exception('Must be signed in to create a course')
        else:
            course = Course(title=title, description=description, created_by=user)
            course.save()
    
            
        

        return CreateCourse(
            id = course.id,
            title = course.title,
            description = course.description,
            created_by = course.created_by
        )

class Mutation(graphene.ObjectType):
    create_course = CreateCourse.Field()
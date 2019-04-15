import graphene
from graphene_django import DjangoObjectType

from course.models import Module,Course
from course.schema import CourseInput

# create the type
class ModuleType(DjangoObjectType):
    class Meta:
        model = Module


# create the query
class Query(graphene.ObjectType):
    modules = graphene.List(ModuleType)

    def resolve_modules(self, info, **kwargs):
        return Module.objects.all()


# create the mutation
class CreateModule(graphene.Mutation):
    id = graphene.Int()
    module_title = graphene.String()
    description = graphene.String()
    body = graphene.String()
    date_created = graphene.Date()
    course_id = graphene.Int()

    class Arguments:
        module_title = graphene.String()
        description = graphene.String()
        body = graphene.String()
        course_id = graphene.Int()
    
    def mutate(self, info, module_title, description, body, course_id):
        user = info.context.user
        if user is None:
            raise Exception("You must have permission to create a course")
        else:
            course = Course.objects.get(id=course_id)
            module = Module(
                module_title=module_title, 
                description=description, 
                body=body, 
                course=course
            )
            module.save()

        return CreateModule(
            id = module.id,
            module_title = module.module_title,
            description = module.description,
            body = module.body,
            course_id = module.course.id
        ) 

class Mutation(graphene.ObjectType):
    create_module = CreateModule.Field()
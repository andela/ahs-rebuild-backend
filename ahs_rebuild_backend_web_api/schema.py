import graphene
import graphql_jwt

import course.schema
import users.schema
import course.module_schema

class Query(users.schema.Query, course.schema.Query, course.module_schema.Query, graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, course.schema.Mutation, course.module_schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
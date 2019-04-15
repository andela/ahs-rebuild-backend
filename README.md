[![Build Status](https://travis-ci.com/andela/ahs-rebuild-backend.svg?branch=develop)](https://travis-ci.com/andela/ahs-rebuild-backend)

# ANDELA HOME STUDY


## Create a user
When creating a user you can use this mutation

#### Mutation
```json
mutation{
    createUser(
        email:"someemail", 
        password: "somepassword",
        username: "someusername"
    ){
        user{
            id
            username
        }
    }
}
```
You will  obtain a response similar to this:

#### Response
```json
{
  "data": {
    "createUser": {
      "user": {
        "username": "someusername",
        "id": "2"
      }
    }
  }
}
```

## Obtain a token for the user. 
This token is what shall be used to grant a user access to courses
#### Mutation
```json
mutation{
  tokenAuth(
    username: "someusername", 
    password:"somepassword"
    )
  {
    token
  }
}
```
#### Response
```json
{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImVtYWxpbmdhIiwiZXhwIjoxNTU2NjIzNzIzLCJvcmlnSWF0IjoxNTU2NjIzNDIzfQ.HD46xDvdJqoUurFwgFNLZ4J6DWiP4QM5zNYfTrkXqhU"
    }
  }
}
```

## Create a course 

#### Mutation
```json
mutation{
  createCourse(
    title: "Introduction to Python",
    description: "An introductory course to python"
  ){
    id
    title
    description
    dateCreated
    createdBy{
      username
    }
  }
}
```
#### Response
```json
{
  "data": {
    "createCourse": {
      "id": 1,
      "title": "Introduction to Python",
      "description": "An introductory course to python",
      "dateCreated": null,
      "createdBy": {
        "username": "someusername"
      }
    }
  }
}
```

## Create a Module
#### Mutation
```json
  modules{
    id
    moduleTitle
    description
    body
    dateCreated
    course{
      id
      title
    }
  }
```

#### Response
```json
{
  "data": {
    "modules": [
      {
        "id": "1",
        "moduleTitle": "Data Structures",
        "description": "In depth look at python data structures. Lists, dictionaries, tuples e.t.c",
        "body": "Data structures body",
        "dateCreated": "2019-04-30",
        "course": {
          "id": "1",
          "title": "Introduction to Python"
        }
      }
  }

```
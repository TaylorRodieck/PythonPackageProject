from ariadne.asgi import GraphQL
from ariadne import gql, QueryType, make_executable_schema

# Define type definitions (schema) using SDL
type_defs = gql(
   """
   type Query {
       places: [Place]
       songs: [Music]
   }


   type Place {
       name: String!
       description: String!
       country: String!
       language: String!
       dish: String!
       }  

    type Music {
        name: String!
        genre: String!
        years: String!
    }
   """
)

# Initialize query

query = QueryType()

# Define resolvers
@query.field("places")
def places(*_):
   return [
       {"name": "Paris", "description": "The city of lights", "country": "France", "language":"French", "dish":"Snails"},
       {"name": "Rome", "description": "The city of pizza", "country": "Italy", "language":"Italian"},
       {
           "name": "London",
           "description": "The city of big buildings",
           "country": "United Kingdom",
           "language":"English",
       },
   ]

@query.field("songs")
def songs(*_):
   return [
      {"name":"All Night Long", "genre":"R&B", "years":"1997"},
   ]

# Create executable schema
schema = make_executable_schema(type_defs, query)

# Create ASGI application
app = GraphQL(schema)
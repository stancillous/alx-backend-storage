#!/usr/bin/env python3
"""
script that lists all documents with name
starting by Holberton in the collection school
"""


def top_students(mongo_collection):
  """
  script that lists all documents with name
  starting by Holberton in the collection school
  """
        
  pipeline = [
          {
              "$project": {
                  'name': "$name",
                  'topics': "$topics",
                  'averageScore': {"$avg": "$topics.score"}
              }
          },
          {
          "$sort": {"averageScore": -1}
          }
  ]

  return mongo_collection.aggregate(pipeline)

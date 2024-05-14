#!/usr/bin/env python3
"""
Top Students
"""


def top_students(mongo_collection):
    """ Find top students by average score """

    # Aggregate pipeline to calculate average score
    pipeline = [
        {
            "$project":
                {
                    "student_name": "$name",
                    "average_score": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "average_score": -1
                }
        }
    ]

    # Perform aggregation using the pipeline
    return mongo_collection.aggregate(pipeline)

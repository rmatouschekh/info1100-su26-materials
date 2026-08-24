# Assignment 4: Course Correction
# due Monday 07/20 at 9:00am (EST)

# Author: 
# NetID: 


import os
import re


def regex_search_course(regex, course):
    """
    Returns the match of the regex pattern in the course.

    regex: a regex pattern
    course: a string representing a course
    returns: a match for the regex pattern in course
    """

    pass # Replace with Task 3 code


def get_course_info(course):
    """
    Returns the a tuple representing the following course information:
        number, name, description, when offered, min # credits, max # credits
        liberal arts requirements, tags, and faculty

    course: a string representing a course
    returns: the tuple of course information
    """

    pass # Replace with Task 4 code


def joint_requirements(course_1, course_2):
    """
    Returns the liberal arts requirements shared by course_1 and course_2

    course_1, course_2: tuples representing two courses
    returns: a set of liberal arts requirements shared by both courses
    """

    pass # Replace with Task 7 code


class Course:
    """ Represents a Course """


def create_course(course):
    """
    Creates a course object representing the same data as the course tuple

    course: a tuple representing a course
    returns: a Course object storing all information in the course tuple
    """

    pass # Replace with Task 9 code


def is_offered(course, term):
    """
    Returns whether course is offered during term

    course: a Course object
    term: a string representing a term
    returns: whether the course is offered during the term
    """

    pass # Replace with Task 11 code


if __name__ == "__main__":
    courses = []

    for i in range(20):
        with open(os.path.join("course-data", f"course-{i+1}.txt")) as f:
            c = f.read()
            courses.append(c)
    
    # Create course tuples

    # Find overlapping requirements

    # Create Course objects

    # Check term offerings

    # Call your free spot function here
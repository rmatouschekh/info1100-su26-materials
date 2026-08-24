# Assignment 3: Reddit Deep-Dive
# due Monday 07/13 at 9:00am (EST)

# Author: 
# NetID: 


from datetime import datetime, timezone
import json
import os


def load_json(file_name):
    """
    Returns a dictionary with the loaded JSON data.

    file_name: a reddit file topic
    returns: a dictionary with the loaded Reddit data
    """

    with open(os.path.join("reddit-data", file_name + ".json")) as f:
        data = json.load(f)
    
    return data


def convert_timestamp(time):
    """
    Returns time in a legible format.

    time: time in seconds since January 1, 1970 in UTC
    returns: the time as a String with format [month] [day], [year] [hour]:[minutes].
    """

    dt = datetime.fromtimestamp(time, tz=timezone.utc)
    return dt.strftime('%B %-d, %Y %H:%M')


def pretty_post(post):
    """
    Returns a string version of the post.

    post: a post dictionary
    returns: a string with a pretty representation of the post
    """

    pass # Replace with Task 2 code


def pretty_comment(comment):
    """
    Returns a string version of the comment.

    comment: a comment dictionary
    returns: a string with a pretty representation of the comment
    """
    
    pass # Replace with Task 3 code


def pretty_top_comments(comments):
    """
    Prints the 'pretty' version of all top-level comments for a post.

    comments: the list of all comments for a post
    """

    pass # Replace with Task 4 code


def find_longest_thread(comments):
    """
    Finds the longest thread of comments originating at one of the comments
    in the provided list

    comments: a list of comments
    returns: the longest thread of replies starting at one of the
        comments in comments
    """

    pass # Replace with Task 5 code


def find_longest_thread_recursive(comments):
    """
    Finds the longest thread of comments originating at one of the comments
    in the provided list

    comments: a list of comments
    returns: the longest thread of replies starting at one of the
        comments in comments
    """

    pass # Replace with Task 6 code


def count_comments(comments):
    """
    Counts the total number of comments in the list, including replies

    comments: a list of comments
    returns: the total number of comments represented by the list comments,
        including replies
    """

    pass # Replace with Task 7 code


def count_comments_recursive(comments):
    """
    Counts the total number of comments in the list, including replies

    comments: a list of comments
    returns: the total number of comments represented by the list comments,
        including replies
    """

    pass # Replace with Task 8 code


if __name__ == "__main__":
    # Load data with input reddit topic
    file_name = input("Enter the file topic: ")

    while file_name not in ["bench-clearing", "fisking", "tontine"]:
        print()
        print(f"{file_name} isn't a valid topic!")
        print()
        file_name = input("Enter the file topic: ")
    print()

    data = load_json(file_name)

    ###################### Task 2 ######################

    # Write the Task 2 test here

    ###################### Task 4 ######################

    # Write the Task 4 test here

    ###################### Task 5 ######################

    # Write the Task 5 test here

    ###################### Task 6 ######################

    # Write the Task 6 test here

    ###################### Task 7 ######################

    # Write the Task 7 test here

    ###################### Task 8 ######################

    # Write the Task 8 test here

    ###################### Task 11 ######################

    # Write the Task 11 test here
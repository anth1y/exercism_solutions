"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    for index, value in enumerate(student_scores):
        rounded_value = round(value)
        student_scores[index] = rounded_value
    return student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    counter = 0 
    for i in student_scores:
        if i <= 40:
            counter += 1
    return counter


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_scores = []
    for scores in student_scores:
        if scores >= threshold:
            best_scores.append(scores)
    return best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    failing_threshold = 40
    score_range = highest - failing_threshold
    interval_size = score_range // 4
    d_threshold = failing_threshold + 1
    c_threshold = d_threshold + interval_size
    b_threshold = c_threshold + interval_size
    a_threshold = b_threshold + interval_size
    
    return [d_threshold, c_threshold, b_threshold, a_threshold]
    
        
        
        


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    student_ranks = [f"{i+1}. {name}: {score}" for i, (name, score) in enumerate(zip(student_names, student_scores))]
    return student_ranks
    
def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    target_score = 100
    for student in student_info:
        if student[1] == target_score:
            return student
    return []

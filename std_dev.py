# Author: Mahtab Zilaie
# Date: November 6 2019
# Description: class called person with datamembers: name and age
# and seperate function std_dev finds standard dev of person's ages

class Person:
    def __init__(self, name, age):
        """name and age of person"""
        self.name = name
        self.age = age

def std_dev(person_list):
    """standard deviation formula for persons and ages"""
    total = 0
    sd = 0

    length = len(person_list)
    for person in person_list:
        total += person.age

    mean = total / length

    for person in person_list:
        sd += (person.age - mean)**2
    return (sd / length)**.5

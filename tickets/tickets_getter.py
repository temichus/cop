# -*- coding: utf-8 -*-
import random
from copy import copy

class TicketsGetter(object):
    def __init__(self):
        with open("students.txt") as f:
            students = f.readlines()
        self.students = [x.strip() for x in students]
        self.tickets = [x for x in range(1,15)]
        self.current_deck = copy(self.tickets)

    def __iter__(self):
        out_dict= dict()

        random.shuffle(self.current_deck)
        random.shuffle(self.students)
        is_deck_empty = 0
        while not is_deck_empty:
            for student in self.students:
                if student not in out_dict:
                    out_dict[student]= list()
                out_dict[student].append(self.current_deck.pop())
                if not self.current_deck:

                    is_deck_empty = 1
                    self.current_deck = copy(self.tickets)
        out_list = ["student: {0}, tickets : {1}".format(key,value) for key,value in out_dict.iteritems()]

        with open('output.csv', 'wb') as output_file:
            for row in out_list:
                output_file.write(row)
                output_file.write("\n")

        return iter(out_list)


for i in TicketsGetter():
    raw_input("Press Enter to get next student...")
    print i
print "The End "



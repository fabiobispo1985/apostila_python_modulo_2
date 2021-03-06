#!/usr/bin/env python3
# -*-coding: utf-8 -*-


# classe pai /parent class
class Bird:
    def __init__(self):
        print("Bird is ready.")

    def whoIsThis(self):
        print('Bird!!')

    def swim(self):
        print('Swim faster!')


# classe filha / child class
class Penguin(Bird):
    def __init__(self):
        #chamando super() funcao
        super().__init__()
        print("Penguin is ready!!")

    def whoIsThis(self):
        print("Penguin")

    def run(self):
        print("Run faster.")

peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.run()

azul = Bird()
azul.whoIsThis()
azul.swim()

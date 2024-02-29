#!/usr/bin/python3

"""Writes the initial class Base"""

import json
import csv
import turtle


class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function to return json string representation of list_dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a func to return JSON string representation of list_objs to a file
         Args:
            list_objs (list): A list of inherited Base instance
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(obj_dicts)
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """function to return  list of the JSON string representation json_string
       Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """a function to return instance with all attributes  set
        Args:
            **dictionary : values pairs of attributes to initialize"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """a function that returns a list of instances
        Returns:
            If a file does not exist, return an empty list
            Otherwise - nstantiated classes."""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list = cls.from_json_string(file.read())
                return [cls.create(**dic) for dic in list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """a functin to save  list of objects to a CSV file
        Args:
            list_obj : list of inherited base instances.
        """
        filename = cls.__name__ + ".csv"  
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")  
            else:
                if cls.__name__ == "Rectangle":
                    
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """reads data from a CSV file &
        returns a list of instantiated classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    
                    
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                
                list = csv.DictReader(file, fieldnames=fieldnames)

                
                list = [dict([k, int(v)] for k, v in d.items())
                        for d in list]
                return [cls.create(**d) for d in list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ a funct to draw Rectangles & Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

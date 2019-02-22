import cv2
import numpy as np

from constants import *
from enums import Piece


class Square:
    """Square(Board, location)

    The Square object analyzes a square section from the location (Tuple)
    on the image referenced by the board object (Board) and processes the
    image to determine the color of piece on the square or empty.
    """

    def __init__(self, board, location):
        self.board = board
        self.location = location

        # Corner to corner pixel location
        self.x, self.y = self.location

        self.xs, self.ys = self.x * SQUARE_SIZE, self.y * SQUARE_SIZE

        self.xe = self.xs + SQUARE_SIZE
        self.ye = self.ys + SQUARE_SIZE

        # BGR and HSV square images
        self.bgr = self.board.bgr[self.xs: self.xe, self.ys: self.ye]
        self.hsv = self.board.hsv[self.xs: self.xe, self.ys: self.ye]

        #
        self.green_pixels = self.calculate_pixels(LOWER_GREEN, UPPER_GREEN)
        self.black_pixels = self.calculate_pixels(LOWER_BLACK, UPPER_BLACK)
        self.white_pixels = self.calculate_pixels(LOWER_WHITE, UPPER_WHITE)

        self.piece = self.classify_square()

    def __repr__(self):
        return "Piece: {} at Square({}, {})".format(
            self.get_piece(), self.board, self.location)

    def __str__(self):
        return "Square: {}; White: {:5d}, Green: {:5d}, Black: {:5d}, Piece?: {}".format(
            (self.x + 1, self.y + 1), self.white_pixels, self.green_pixels, self.black_pixels,
            self.get_piece())

    def calculate_pixels(self, lower, upper):
        """calculate_pixels(lower, upper)

        Calculate the number of pixels falling in between the
        lower and upper ranges for HSV images.

        :param lower: list
        :param upper: list
        :return: int
        """

        lower_range = np.array(lower)
        upper_range = np.array(upper)

        mask = cv2.inRange(self.hsv, lower_range, upper_range)
        return (mask == 255).sum()

    def classify_square(self):
        piece_exists = (self.white_pixels < WHITE_THRESHOLD) and \
                       (self.green_pixels < GREEN_THRESHOLD)

        if piece_exists and (self.black_pixels > BLACK_THRESHOLD):
            piece = Piece(False)
        elif piece_exists:
            piece = Piece(True)
        else:
            piece = Piece(None)

        return piece

    def get_piece(self):
        return self.piece

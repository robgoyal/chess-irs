import cv2
import numpy as np

from constants import *


class Square:

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
        self.green_pixels = self.calculate_green_pixels()
        self.black_pixels = self.calculate_black_pixels()
        self.white_pixels = self.calculate_white_pixels()

        #
        # self.contains_piece = self.detect_piece()
        self.piece = self.classify_square()

    def __repr__(self):
        return "Square({}, {})".format(self.board, self.location)

    def __str__(self):
        return "Square: {}; White Pixels: {:5d}, Green Pixels: {:5d}, Black Pixels: {:5d}, Piece?: {}".format(
            (self.x + 1, self.y + 1), self.white_pixels, self.green_pixels, self.black_pixels,
            self.get_piece())

    def calculate_white_pixels(self):
        lower_white = np.array(LOWER_WHITE)
        upper_white = np.array(UPPER_WHITE)

        white_mask = cv2.inRange(self.hsv, lower_white, upper_white)
        return (white_mask == 255).sum()

    def calculate_green_pixels(self):
        lower_green = np.array(LOWER_GREEN)
        upper_green = np.array(UPPER_GREEN)

        green_mask = cv2.inRange(self.hsv, lower_green, upper_green)
        return (green_mask == 255).sum()

    def calculate_black_pixels(self):
        lower_black = np.array(LOWER_BLACK)
        upper_black = np.array(UPPER_BLACK)

        black_mask = cv2.inRange(self.hsv, lower_black, upper_black)
        return (black_mask == 255).sum()

    def classify_square(self):
        piece_exists = (self.white_pixels < WHITE_THRESHOLD) and \
                       (self.green_pixels < GREEN_THRESHOLD)

        if piece_exists and (self.black_pixels > BLACK_THRESHOLD):
            piece = "Black"
        elif piece_exists:
            piece = "White"
        else:
            piece = "Empty"

        return piece

    def get_piece(self):
        return self.piece

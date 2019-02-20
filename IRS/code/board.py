import cv2
import sys
import numpy as np
import argparse

from pprint import pprint

from square import Square
from constants import *


class Board:
    def __init__(self, processed_img, preprocessed_img=None):
        self.input_path = preprocessed_img
        self.output_path = processed_img

        self.bgr = cv2.imread(self.output_path)
        self.hsv = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2HSV)

        self.squares, self.piece_locations = self.populate_matrices()

        if DEBUG:
            self.debug()

    def debug(self):
        def show_image(img_resize, window_name):
            # pre_proc_img_resize = cv2.resize(cv2.imread(img_path), (0, 0), fx=0.5, fy=0.5)
            cv2.namedWindow(window_name)
            cv2.moveWindow(window_name, 40, 30)
            cv2.imshow(window_name, img_resize)
            cv2.waitKey(0)
            cv2.destroyWindow(window_name)

        squares_flat = np.asarray(self.squares).flatten()

        if PRE_PROCESSED_IMAGE and self.input_path:
            pre_proc_img_resize = cv2.resize(cv2.imread(self.input_path), (0, 0), fx=0.25, fy=0.25)
            show_image(pre_proc_img_resize, "Pre Processed Board Image")

        if PROCESSED_IMAGE:
            proc_img_resize = cv2.resize(self.bgr, (0, 0), fx=0.5, fy=0.5)
            show_image(proc_img_resize, "Processed Board Image")

        for sqr in squares_flat:
            print(sqr)

            # from IPython import embed
            # embed()

            if SHOW_SQUARES:

                # Maintain copy of bgr to to replace
                bgr_copy = proc_img_resize.copy()
                border = cv2.rectangle(bgr_copy, (sqr.ys // 2, sqr.xs // 2), (sqr.ye // 2, sqr.xe // 2),
                                      (0, 0, 255), 5)
                overlay_winname = str(sqr)[:15]
                show_image(border, overlay_winname)

    def destroy_cv2_windows(self):
        cv2.destroyAllWindows()

    def populate_matrices(self):
        sqr_matrix = [[Square(self, (x, y)) for y in range(8)] for x in range(8)]
        loc_matrix = [[sqr_matrix[i][j].get_piece() for j in range(8)]
                      for i in range(8)]

        return sqr_matrix, loc_matrix

    def get_piece_locations(self):
        return self.piece_locations

    def __repr__(self):
        return "Board({})".format(self.input_path)

    def __str__(self):
        return self.__repr__()



if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description="Analyze image to determine location "
    #                                              "of pieces on a green and white chess board")
    # parser.add_argument("processed image path", )

    board = Board(sys.argv[1], )


    pprint(board.get_piece_locations())
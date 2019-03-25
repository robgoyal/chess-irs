import boto3
from datetime import datetime
from move import Move

BUCKET_NAME = 'gamestateimages'
STATE_FILE_NAME = 'state.jpg'
RAW_SERVER_PATH = "/home/ubuntu/Desktop/CAPSTONE_R/chess-irs/pictures/raw_states/"
PROCESSED_SERVER_PATH = "/home/ubuntu/Desktop/CAPSTONE_R/chess-irs/pictures/processed_states"


def upload_response(path):
    s3 = boto3.client('s3')
    s3.upload_file(path, BUCKET_NAME, STATE_FILE_NAME)


def grab_image():
    s3 = boto3.resource('s3')
    filename = str(datetime.today()).replace(" ", "-") + ":" + STATE_FILE_NAME
    s3.Bucket(BUCKET_NAME).download_file(STATE_FILE_NAME, RAW_SERVER_PATH + filename)
    return filename

def process_image():
    previous_state = ""
    filename = grab_image()
    move_info = Move(previous_state, RAW_SERVER_PATH + filename,
                     PROCESSED_SERVER_PATH + filename)
    
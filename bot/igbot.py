import random
import time
import os
import glob
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from pathlib import Path
from lib.yt_dl_app import (read_caption_mention,
                           countdown_sleep)

# THIS IS THE BACKEND CODE THAT RUNS MAIN.PY
# CHANGING ANYTHING IN THIS FILE COULD BREAK THE MAIN FUNCTIONS!


class InstagramBot:

    def __init__(self, username, password, proxy: str = None,
                 delay_range: list = (5, 10)):
        self.filepath = None
        self.username = username
        self.password = password
        self.proxy = proxy
        self.delay_range = delay_range
        self.client = Client()

    def login_user(self):
        logger = self.get_logger()
        str_path = "./ig_settings.json"
        path = Path(str_path)
        if self.proxy is None:
            pass
        else:
            self.client.set_proxy(self.proxy)

        if self.first_login():
            print("Logging in for the first time\n Creating session data")
            self.client.login(self.username, self.password)
            self.client.dump_settings(path)
            return
        else:
            print("Session data found")
            pass
        session = self.client.load_settings(path)
        login_via_session = False
        login_via_pw = False
        if session:
            try:
                self.client.set_settings(session)
                self.client.login(self.username, self.password)

                # check if session is valid
                try:
                    self.client.get_timeline_feed()
                except LoginRequired:
                    print("Login required")
                    logger.info("Login required")

                    old_session = self.client.get_settings()

                    # use the same device uuids across logins
                    self.client.set_settings({})
                    self.client.set_uuids(old_session["uuids"])

                    self.client.login(self.username, self.password)
                    self.client.dump_settings(path)
                login_via_session = True
                print("Logged in via session information")
            except Exception as e:
                print(f"An error occurred during login: {e}")
                logger.info("Couldn't login via session information: %s" % e)
                raise
        if not login_via_session:
            try:
                print('test')
                logger.info("Attempting to login via username and password. username: %s" % self.username)
                self.client.login(self.username, self.password)
                self.client.dump_settings(path)
                if self.client.get_timeline_feed():
                    login_via_pw = True
            except Exception as e:
                logger.info("Couldn't login user using username and password: %s" % e)
            if not login_via_pw and not login_via_session:
                raise Exception("Couldn't login user with either password or session")

    @staticmethod
    def first_login():
        folder = os.path.dirname(os.path.abspath(__file__))
        file = glob.glob(folder + "/*.json")
        print(file)
        if file:
            return False
        else:
            return True

    def reels_to_instagram(self, reel_path, post_data_path, thumbnail_path,
                           hashtags=".", call_to_action=".", user_mention: bool = True):
        data_paths = post_data_path
        video_paths = reel_path
        my_hashtags = hashtags
        my_call_to_action = call_to_action

        while video_paths:
            # loop for videos in the directory
            print(f"Remaining files: {len(video_paths)}")
            filepath = video_paths.pop(0)
            datapath = data_paths.pop(0)
            caption, mention = read_caption_mention(datapath)
            # for user_mention bool
            if user_mention:
                mention = f"@ {mention}"
            else:
                mention = ""
            reel_caption = f"{caption}\n\n{my_call_to_action}\n\n{my_hashtags}\n\n{mention}"
            print(f"Processing file: {filepath}, Caption: {caption}, Mention: {mention}")

            filepath = Path(filepath)
            datapath = Path(datapath)

            try:
                print(f"Starting upload for {filepath}")
                self.client.clip_upload(filepath, reel_caption)
                # logger.info("Posted to Reels")
                print(f"Successfully posted {filepath} to Reels")
                time.sleep(3)
                os.remove(filepath)  # Delete the file after successful upload
                os.remove(datapath)
                # going to delete the generated thumbnail as well
                directory = thumbnail_path
                # Pattern to match all .jpg files
                pattern = os.path.join(directory, '*.jpg')
                # Find all .jpg files in the directory
                jpg_files = glob.glob(pattern)
                # Remove each .jpg file
                for file_path in jpg_files:
                    os.remove(file_path)
                print(f"Finished cleaning up")
            except LoginRequired as e:
                print(f"Login required exception for {filepath}: {e}")
                # logger.exception(f"Login required, {e}")
                self.client.relogin()
                self.client.clip_upload(filepath, reel_caption)
                os.remove(filepath)  # Delete the file after successful upload
                os.remove(datapath)
            except Exception as e:
                print(f"General exception for {filepath}: {e}")
                # logger.exception(f"Error occurred: {e}")
            finally:
                sleep_duration = random.randint(60 * 50, 60 * 80)
                print(f"Going to sleep now for {int(sleep_duration // 60)} minutes")
                print("Don't disturb my slumber...")
                countdown_sleep(sleep_duration, interval=60 * 10)

    @staticmethod
    def get_logger():
        import logging

        logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO)
        logger = logging.getLogger('igbot')
        return logger

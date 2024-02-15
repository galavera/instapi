import random
import time
import os
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from pathlib import Path
from datetime import datetime, timedelta
from threading import Event

# THIS IS THE BACKEND CODE THAT RUNS MAIN.PY
# CHANGING ANYTHING IN THIS FILE COULD BREAK THE MAIN FUNCTIONS!

# stop_event as a global variable
stop_event = Event()


class InstagramBot:

    def __init__(self, delay_range=None):
        if delay_range is None:
            delay_range = [5, 10]
        elif not (isinstance(delay_range, list) and len(delay_range) == 2
                  and all(isinstance(n, int) for n in delay_range)):
            raise ValueError("delay_range must be a list of two integers.")
        self.client = Client()
        self.client.delay_range = delay_range

    def login_user(self, username, password, proxy=None):
        self.configure_client(username, password, proxy)
        settings_path = Path("ig_settings.json")

        if not self.attempt_login_with_session(settings_path):
            self.attempt_login_with_credentials(settings_path)

    def configure_client(self, username, password, proxy):
        self.client.username = username
        self.client.password = password
        if proxy:
            self.client.proxy = proxy
            self.client.set_proxy(proxy)

    def attempt_login_with_session(self, settings_path):
        if settings_path.exists():
            print("Session data found\nAttempting to login, please wait...")
            session = self.client.load_settings(settings_path)
            if self.login(session):
                print("Logged in via session information")
                return True
        else:
            print("Logging in for the first time\nCreating session data")
        return False

    def login(self, session=None):
        try:
            if session:
                self.client.set_settings(session)
            self.client.login(self.client.username, self.client.password)
            self.client.get_timeline_feed()  # Validates the session
            return True
        except (LoginRequired, Exception) as e:  # Replace Exception with specific exceptions
            self.handle_login_exception(e, settings_path=Path("ig_settings.json"))
            return False

    def handle_login_exception(self, exception, settings_path):
        logger = self.get_logger()
        if isinstance(exception, LoginRequired):
            print("Login required, attempting to relogin...")
            logger.info("Login required, attempting to relogin...")
            try:
                old_session = self.client.get_settings()
                # use the same device uuids across logins
                self.client.set_settings({})
                self.client.set_uuids(old_session["uuids"])
                self.client.login(self.client.username, self.client.password)
                self.client.dump_settings(settings_path)
                logger.info("Re-login successful, settings updated")
            except Exception as e:
                # Log the exception with traceback for debugging
                print(f"An error occurred during re-login: {e}")
                logger.info(f"An error occurred during re-login: {e}")
                # Reraise the exception to be handled or logged by upstream logic
                raise
        else:
            print(f"An error occurred during login: {exception}")
            logger.exception(f"Couldn't login: {exception}")

    def attempt_login_with_credentials(self, settings_path):
        if not self.login():
            raise Exception("Couldn't login with either password or session")

    def reels_to_instagram(self, reel_paths, post_data_paths, thumbnail_dir,
                           hashtags=".", call_to_action=".", user_mention: bool = True,
                           input_duration=60):
        global stop_event
        stop_event.clear()
        for reel_path, post_data_path in zip(reel_paths, post_data_paths):
            if not stop_event.is_set():
                print(f"Remaining files: {len(reel_paths)}")
                caption, mention = self.read_caption_mention(post_data_path)
                mention = f"@{mention}" if user_mention else ""
                reel_caption = f"{caption}\n\n{call_to_action}\n\n{hashtags}\n\n{mention}"
                print(f"Processing file: {os.path.basename(reel_path)}\nCaption: {caption}\nMention: {mention}")
                try:
                    print(f"Starting upload for {os.path.basename(reel_path)}")
                    self.client.clip_upload(reel_path, reel_caption)
                    print(f"Successfully posted {os.path.basename(reel_path)} to Reels")
                    os.remove(reel_path)
                    os.remove(post_data_path)
                except LoginRequired as e:
                    print(f"Login required exception for {os.path.basename(reel_path)}: {e}")
                    self.handle_relogin_and_upload(reel_path, reel_caption, post_data_path)
                except Exception as e:
                    print(f"General exception for {os.path.basename(reel_path)}: {e}")
                self.cleanup_thumbnails(thumbnail_dir)
                if len(reel_paths) > 0:
                    sleep_duration = random.randint(60 * input_duration, 60 * (input_duration + 15))
                    future_time = datetime.now() + timedelta(seconds=sleep_duration)
                    formatted_time = future_time.strftime("%I:%M %p").lstrip("0").replace("AM", "am").replace("PM", "pm")
                    print(f"Starting the sleep timer.\n"
                          f"Next post will be uploaded after the sleep timer ends\n(approx:{formatted_time})\n"
                          f"You can minimize the app and I'll continue working.\n")
                    self.interruptible_sleep(sleep_duration, 30)
                else:
                    print("Finished uploading all reels.")
                    break
            else:
                print("Instabot has been defeated in battle.")
                break

    def handle_relogin_and_upload(self, reel_path, reel_caption, post_data_path):
        self.client.relogin()
        self.client.clip_upload(reel_path, reel_caption)
        os.remove(reel_path)  # Consider moving these to ensure they're always executed
        os.remove(post_data_path)

    @staticmethod
    def cleanup_thumbnails(thumbnail_dir):
        for thumbnail_path in Path(thumbnail_dir).glob('*.jpg'):
            os.remove(thumbnail_path)
        print("Finished cleaning up thumbnails.")

    @staticmethod
    def interruptible_sleep(sleep_duration, check_interval):
        global stop_event
        start_time = time.time()
        while (time.time() - start_time) < sleep_duration:
            if stop_event.is_set():
                # Stop event is set, break the sleep
                break
            time.sleep(min(check_interval, sleep_duration - (time.time() - start_time)))

    @staticmethod
    def stop_bot():
        print("Stopping the bot...please wait.")
        stop_event.set()

    @staticmethod
    def countdown_sleep(duration, interval=60 * 10):
        """
        Sleep for a specified duration, printing the time remaining every interval seconds.

        :param duration: Total sleep time in seconds.
        :param interval: Interval in seconds at which to print the remaining time.
        """
        remaining = duration
        while remaining > 0:
            print(f"Wait time until the next post is {int(remaining // 60)} minutes...\n")
            time.sleep(min(interval, remaining))
            remaining -= interval

    @staticmethod
    def read_caption_mention(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            line = file.readline().strip()
        if '|' in line:
            caption, mention = line.split('|', 1)
            return caption.strip(), mention.strip()
        else:
            return "", ""

    @staticmethod
    def get_logger():
        import logging

        logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.INFO)
        logger = logging.getLogger('igbot')
        return logger

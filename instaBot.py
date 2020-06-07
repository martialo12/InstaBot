import schedule
import time

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

from config.config import InstaBotConfig

# reading configuration from json configuration file
InstaBotConfig.read_from_file()
insta_username = InstaBotConfig.USERNAME
insta_password = InstaBotConfig.PASSWORD

#path to your workspace
set_workspace(path='InstaPy')


def insta_bot():
    # run with browser GUI
    session = InstaPy(username=insta_username, password=insta_password)

    # run without browser GUI
    # session = InstaPy(username=username, password=password, headless_browser=True)
    with smart_run(session):

        session.login()
        session.like_by_tags(['cameroun', 'douala', 'yaounde', 'limbe'], amount=5)
        session.set_do_follow(True, percentage=50)
        session.set_do_comment(True, percentage=50)
        session.set_comments([u'This post is 🔥',u'More emojis are always better 💯',u'I love your posts 😍😍😍']);
        session.set_dont_like(["naked", "sex", "sexe", "ass"])
        session.set_quota_supervisor(enabled=True, peak_comments_daily=100, peak_comments_hourly=15)

        session.set_quota_supervisor(enabled=True,
                                     sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                     sleepyhead=True, stochastic_flow=True, notify_me=True,
                                     peak_likes_hourly=20,
                                     peak_likes_daily=200,
                                     peak_comments_hourly=15,
                                     peak_comments_daily=100,
                                     peak_follows_hourly=48,
                                     peak_follows_daily=15,
                                     peak_unfollows_hourly=10,
                                     peak_unfollows_daily=100)

        lazySmurf_following = session.grab_following(username="lazy.smurf", amount="full", live_match=True,
                                                     store_locally=True)

        session.end()


if __name__=='__main__':
    schedule.every().day.at("18:00").do(insta_bot)
    while True:
        schedule.run_pending()
        time.sleep(10)

from datetime import datetime
from dataclasses import dataclass
# each social channel has a type
# and the current number of followers
# SocialChannel = tuple[str, int]

# each post has a message and the timestamp when it should be posted
# Post = tuple[str, int]

@dataclass
class Post:
    message: str
    timestamp: datetime
@dataclass
class SocialChannel:
    type: str
    num_followers: int
    



def post_to_youtube(channel: SocialChannel, message: str) -> None:
    print(f"{channel.type} channel: {message}")


def post_to_facebook(channel: SocialChannel, message: str) -> None:
   print(f"{channel.type} channel: {message}")


def post_to_twitter(channel: SocialChannel, message: str) -> None:
    print(f"{channel.type} channel: {message}")

POST_FUNCTIONS = {
    "facebook":post_to_facebook,
    "twitter":post_to_twitter,
    "youtube":post_to_youtube
}

def post_a_message(channel: SocialChannel, message: str) -> None:
    try:
        post_function = POST_FUNCTIONS[channel.type]
    except KeyError as e:
        raise e
    
    post_function(channel, message)



def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        for channel in channels:
            if post.timestamp <= datetime.now():
                post_a_message(channel, post.message)


def main() -> None:
    posts = [
        Post(
            "Grandma's carrot cake is available again (limited quantities!)!",
            datetime.fromtimestamp(1568123400),
        ),
        Post("Get your carrot cake now, the promotion ends today!", datetime.fromtimestamp(1568133400)),
    ]
    channels = [
        SocialChannel("youtube", 100),
        SocialChannel("facebook", 100),
        SocialChannel("twitter", 100),
    ]
    process_schedule(posts, channels)


if __name__ == "__main__":
    main()

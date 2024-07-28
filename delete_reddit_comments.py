import praw

client_id = ""
client_secret = ""
user_agent = ""
username = ""
password = ""

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

user = reddit.user.me()

excluded_subreddits = []

for comment in user.comments.new():
    if comment.subreddit.display_name not in excluded_subreddits:
        print(f'Deleting Comment: {comment.body}')
        comment.delete()
    else:
        print(f'Skipping comment: {comment.body} in subreddit: {comment.subreddit.display_name}')

print("All Comments Deleted")

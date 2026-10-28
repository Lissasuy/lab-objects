"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts
    alice = User('alice')
    bob = User('bob')
    users = [alice, bob]
    posts = [
        Tweet('alice', 'learning #python and #oop today'),
        Tweet('bob', 'just a normal tweet'),
        Tweet('alice', 'Games! Games! Bring Snacks!')
    ]
    alice.follow()
    alice.follow()
    alice.unfollow()
    bob.follow()

    posts[0].like()
    posts[0].like()
    posts[1].like()
    posts[1].unlike()

    return users, posts

def main():
    # Call build_feed and display the returned objects and hashtags.
    users, posts = build_feed()

    for user in users:
        print(user)
    for post in posts:
        print(post)
        print(post.hashtags())

if __name__ == '__main__':
    main()

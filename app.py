def save(username, content, url, time):
    return "tweet saved"

class Tweet:
    def __init__(self, username, content, url, time):
        self.username = username
        self.content = content
        self.url = url
        self.time = time


    def save(self):
        keep = save(
            self.username,
            self.content,
            self.url,
            self.time
        )
        print(keep)




tweet = Tweet("david", "cool", "example.com", "2022-01-01")
tweet.save()
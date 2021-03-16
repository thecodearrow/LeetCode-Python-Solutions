
import random
import string
class Codec:
    def __init__(self):
        self.url_store={}
        self.chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' #string.ascii_letters
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        #let's say we generate 8 random characters
        code="https://tinyurl.com/"
        for i in range(8):
            c=random.choice(self.chars)
            code+=c
        
        self.url_store[code]=longUrl
        return code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if(shortUrl in self.url_store):
            return self.url_store[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
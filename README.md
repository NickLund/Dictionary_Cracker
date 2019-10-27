# Dictionary_Cracker
For sha512-crypt(3) to add salt to dictionary words

So, I started to make this at midnight. Its working now, I hope. I'm starting to hallucinate shapes in my perifrial vision, so I'm quickly makeing this then I'm out of here.
Basically, it takes linux password hashes, a dictionary file, and your premade list of salts, and makes a hash from the salts/dictionary combo. It then takes the hash and compares that to the provided hashes, and if it matches writes the password to a file (FattyList.txt).

##This is a work in progress
I hope to make this in a faster language, like C/C++
I need to add functionality so you can choose your own files.
I'm sure there is a faster method too, but idk
I also need to improve it where you just dump the hash file, and I extract the salt/hash version, then crack it.

##Use
Currently, only works with $6$ hashes (sha512-crypt, see: https://docs.python.org/3/library/crypt.html, https://en.wikipedia.org/wiki/Crypt_(Unix))
You need 3 files:
1: realhuman_phill.txt  -> This is your dictionary file
2: salts.txt            -> This is your file of salts (prepend hash version, so it looks like: $6$IQ4tZq7P, in my case prepending $6)
3: compare.txt          -> This is your complete unix hash, method ($6, $salt, $hash) (ex: $6$IQ4tZq7P$39hcxZmhN667muiAB0RzdEB4AIdaWvjQEnM0qooZceYxghxZOE2pF/yIN7YfhUbjKTLzcX4cQY11cn/c4FoBV0)
Make sure that the salts and compare lists are in correct order (first salt goes to the first hash)

##Brief Explanation
It takes the first salt and hash in their respective lists, then puts then in the cracking function. 
Then it takes the salt, adds it to a line from the provided dictionary into the hash function, and saves it as a string.
Then that string gets compared to the imported hash.
If they match, then the password and hash are written to a file (FattyList.txt). If it doesn't exist, then it creates it. If it does, then it appends to it.
To make you look like a cwel h@x0r I output bullshit like, "Attempt number [counter] Password: [dictionary word] is hashed as: [hash]"
If you want a clean bash output, then you can comment that out no biggie, but I'll judge you if I ever find out. 
I also print out the success. But, since I have l33t output being printed at the speed of light, you'll never see it lol

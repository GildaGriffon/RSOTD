import praw, pprint, pickle
user_agent = "/u/Gilda_Griffon's RSOTD Tool" ##input("Please input your desired user agent to display to reddit: ")
r = praw.Reddit(user_agent=user_agent)
nsfwCheck = input("Allow NSFW subs to be displayed?(True or False): ")
subreddit = r.get_random_subreddit(nsfw=nsfwCheck)
storeIt = pprint.pprint(subreddit)
strSub = str(subreddit)
storeIt
outfile = open('RSOTD.txt','w')
outfile.write(strSub)


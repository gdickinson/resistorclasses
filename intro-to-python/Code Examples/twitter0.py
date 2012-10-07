#!/usr/bin/python



import twitter

api = twitter.Api()

usernames = ["gdickinson",
	"jwgayle",
	"feneets",
	"bennettmorrison",
	"BarackObama",
	"briansabbeth",
	"JustinBieber",
	"jesuschrist",
	"deez79",
	"nycresistor",
	"mikebloomberg"]

for name in usernames:
	user = api.GetUser(name)
	# Get total number of tweets
	#print("%s  %d" % (name, user.statuses_count))
	print(name)
	print(user.statuses_count)
	print()
	# Print out the result


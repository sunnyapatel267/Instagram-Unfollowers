import json

# reads data from the 'following' json file
with open('following.json') as following:
    data_following = json.load(following)

# create empty list/array 
followings = []

#adds the name of each person I follow in 'followings' array
for i in data_following['relationships_following']:
    followings.append(i['string_list_data'][0]['value'])

#------------------------------------------------------------/
# reads data from the 'followers' json file
with open('followers.json') as follower:
    data_followers = json.load(follower)

# create empty list/array 
followers = []

#adds the name of each person that 'followers' array
for i in data_followers['relationships_followers']:
    followers.append(i['string_list_data'][0]['value'])
    
#------------------------------------------------------------/
#Empty List created to add accounts to unfollow
unfollowers = []

# if followings account does not follow unfollow
for i in followings:
    if i not in followers:
        unfollowers.append(i)

#Print accounts to unfollow onto txt file
f = open("unfollow.txt","w")
f.write("Number of Accounts to Unfollow: " + str(len(unfollowers)))
f.write("\n\n")
for i in unfollowers:
    f.write(i + "\n")
f.close

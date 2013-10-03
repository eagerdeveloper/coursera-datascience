import sys
import json
import re

hashtag_scores = {} # initialize sentiments dictionary

def calculate_top_ten_hashtags(tweet_file):
    # initialize tweets dictionary
    #counter = 0
    # 1. Read all tweets from file
    for line in tweet_file.readlines():
        tweet = json.loads(line)

        # 2. Verify each tweet for location, language
        store_hashtags_from_tweet(tweet)
        #counter += 1
         
        #if counter == 5000:
        #    break;

    tweet_file.close()

    print_top_ten_hashtags(hashtag_scores)


def store_hashtags_from_tweet(tweet):
    key = "entities"
    if key in tweet.keys():
        if tweet[key]:
            #print "ENTITIES: ", tweet[key].values()
            #print "TWEET: ", tweet["text"].encode('utf-8')
            if "hashtags" in tweet[key].keys():
                for h in tweet[key]["hashtags"]:
                    #print h
                    hashtag = h["text"].encode('utf-8')
                    if hashtag:
                        #print "HASHTAG: ", h["text"]
                        if hashtag in hashtag_scores.keys():
                            hashtag_scores[hashtag] += 1
                        else:
                            hashtag_scores[hashtag] = 1
        

def print_top_ten_hashtags(hashtag_scores):

   import operator
   sort = sorted(hashtag_scores.iteritems(),key = operator.itemgetter(1))
   sort.reverse()
   for freq in sort[0:10]:
      print str(freq[0]), "%.04f" % freq[1]
   #totalkeys = len(hashtag_scores)
   #count = 0
   #for key,value in sorted(hashtag_scores.iteritems(), key=lambda (k,v): (v,k)):
   #    if count >= (totalkeys - 10):
   #        print key, "%.04f" % value
   #    count += 1

   #for value in newlist.items():
      
   #import operator
   #print max(hashtag_scores.iteritems(), key = operator.itemgetter(1))[0]
  
def hw(tweet_file):
    calculate_top_ten_hashtags(tweet_file)

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()

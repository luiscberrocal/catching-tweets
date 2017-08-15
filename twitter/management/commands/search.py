import tweepy

from twitter.management.base import TweepyCommand, MyStreamListener


class Command(TweepyCommand):

    help = 'Listen to a Twitter stream'

    def handle(self, **options):
        search_query = '#djangocon'
        tweets_per_qry = 100
        max_id = -1
        since_id = None
        max_tweets = 1000

        new_tweets = list()
        tweet_count = 0
        count = 1
        while tweet_count < max_tweets:
            if max_id <= 0:
                if since_id is None:
                    new_tweets = self.api.search(q=search_query, count=tweets_per_qry)
                else:
                    new_tweets = self.api.search(q=search_query, count=tweets_per_qry,
                                                     max_id=str(max_id - 1),
                                                     since_id=since_id)
            else:
                if since_id is None:
                    new_tweets = self.api.search(q=search_query, count=tweets_per_qry,
                                                     max_id=str(max_id - 1))
                else:
                    new_tweets = self.api.search(q=search_query, count=tweets_per_qry,
                                                     max_id=str(max_id - 1),
                                                     since_id=since_id)

            if not new_tweets:
                self.stdout.write("No more tweets found")
                break
            for tweet in new_tweets:
                self.stdout.write('{} - {} - {}'.format(count, tweet.created_at, tweet.text))
                count += 1
            tweet_count += len(new_tweets)
            max_id = new_tweets[-1].id



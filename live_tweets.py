{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "e299ea0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('Live Twitter Sentiment Analysis with Tweepy and HuggingFace Transformers')\n",
    "st.markdown('This app uses tweepy to get tweets from twitter based on the input name/phrase. It then processes the tweets through HuggingFace transformers pipeline function for sentiment analysis. The resulting sentiments and corresponding tweets are then put in a dataframe for display which is what you see as result.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "83a2c03c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def run():\n",
    "    with st.form(key=\"Enter name\"):\n",
    "        search_words = st.text_input(\"Enter the name for which you want to know the sentiment\")\n",
    "        number_of_tweets = st.number_input(\"Enter the number of latest tweets for which you want to know the sentiment(Maximum 50 tweets)\", 0,50,10)\n",
    "        submit_button = st.form_submit_button(label=\"Submit\")\n",
    "    if submit_button:\n",
    "        tweets =tw.Cursor(api.search_tweets,q=search_words,lang=\"en\").items(number_of_tweets)\n",
    "        tweet_list = [i.text for i in tweets]\n",
    "        p = [i for i in classifier(tweet_list)]\n",
    "        q=[p[i][\"label\"] for i in range(len(p))]\n",
    "        df = pd.DataFrame(list(zip(tweet_list, q)),columns =[\"Latest \"+str(number_of_tweets)+' Tweets'+ 'on' +search_words, 'sentiment'])\n",
    "    st.write(df)\n",
    " \n",
    "\n",
    "    if __name__==\"__main__\":\n",
    "        run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

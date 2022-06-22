from Trie import *
from moon_utils import *
import graph
# 表单
def search_form(request):
    return render(request, './app/sentiment.html')


from django.shortcuts import render


def analyse(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
        print(request)
        article_arr = trie_utils().preprocess(request.POST['q'])

        trie = trie_utils().pickle_load_trie()
        sentiment = trie.sentiment_search(article_arr)
        score = trie_utils().get_score(sentiment)
        ctx['score'] = score
        ctx['positive'] = sentiment[1]
        ctx['negative'] = sentiment[-1]
        ctx['stop'] = sentiment[11]
        ctx['neutral'] = sentiment[0]
        print(score)
        return render(request, "app/sentiment.html", ctx)

def analyse_countries(request):
    ctx = {}
    if request.POST:
        top5 = pick_country(5)

        # build sentiment trie
        trie = trie_utils().pickle_load_trie()
        data_list = []
        res = []
        # sentiment analysis by words
        for country in articles.keys():
            article_arr = trie_utils().preprocess(articles[country])
            sentiment = trie.sentiment_search(article_arr)
            score = trie_utils().get_score(sentiment)

            data_list.append([country, sentiment[0], sentiment[-1], sentiment[1], sentiment[11], score])
            # ctx[country] = f"{country} has {sentiment[0]} neutral words, {sentiment[-1]} negative words, {sentiment[1]} positive words, {sentiment[11]} stop words\n"+ "{country} has a score of {score}")
            # res.append("
            # print(
            #     f"{country} has {sentiment[0]} neutral words, {sentiment[-1]} negative words, {sentiment[1]} positive words, {sentiment[11]} stop words")
            # print(f"{country} has a score of {score}")
        # to draw the graphs, use:
        graph.bar_graph(data_list)
        graph.score_graph(data_list)
        return render(request, "app/sentiment.html", ctx)
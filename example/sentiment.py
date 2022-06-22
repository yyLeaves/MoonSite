from Trie import *
from moon_utils import *
import graph
from cfg import *
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
            ctx[f"{country}Score"] = f"{score:.05f}"
            ctx[f"{country}Pos"] = sentiment[1]
            ctx[f"{country}Neg"] = sentiment[-1]
            ctx[f"{country}Neutral"] = sentiment[0]
            ctx[f"{country}Stop"] = sentiment[11]
            print(f"{country}Score")

        graph.bar_graph(data_list, bar_graph_path)
        graph.score_graph(data_list, rank_graph_path)

        ctx["bar"] = "graphs/Bar.html"
        return render(request, "app/country.html", ctx)
from Trie import *

# 表单
def search_form(request):
    return render(request, './app/sentiment.html')


from django.shortcuts import render


# 接收POST请求数据
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
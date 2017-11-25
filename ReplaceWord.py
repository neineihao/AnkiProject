#!/usr/bin/env python
# coding: utf-8
import MeCab

# text = "お腹いっぱいすぎるぜ"
# t = MeCab.Tagger("-Owakati")
# result = t.parse(text)
# print(result)
# def Replace(sentance, word):
input = '土地勘のあるきみに協力して欲しいだけなのさ、三人目の、あるいは百一人目の被害者を出さないために」 　' \
            'たまには縁もゆかりもない女子を助けてみるのも乙だろう──と、臥煙さんは、僕の来歴を揶揄するようなことを言ってきた。'
mt = MeCab.Tagger("-Ochasen")
mt.parse('')
node = mt.parseToNode(input)
# print(node.surface)
# for item in node:
#     print("Node surface : {}".format(item.surface))
#     print("Node feature : {}".format(item.feature))
while node:
    print (node.surface, node.feature)
    print("surface : {}".format(node.surface))
    print("feature : {}".format(node.feature))
    print("type of feature : {}".format(node.feature.split(',')[6]))
    node = node.next
print(type(node))
# -*- coding: utf-8 -*-
import MeCab
def replaceWord(sentance, word):
    if word in sentance:
        sentance = sentance.replace(word, '_____')
    else:
        mt = MeCab.Tagger("-Ochasen")
        mt.parse('')
        node = mt.parseToNode(sentance)
        while node:
            # print(node.surface, node.feature)
            # print("surface : {}".format(node.surface))
            # print("feature : {}".format(node.feature))
            # print("type of feature : {}".format(node.feature.split(',')[6]))
            words = node.feature.split(',')
            if words[6] == word:
                sentance = sentance.replace(node.surface,'_____')
            node = node.next
    return sentance

if __name__ == '__main__':
    inputSentance = '土地勘のあるきみに協力して欲しいだけなのさ、三人目の、あるいは百一人目の被害者を出さないために」 　' \
            'たまには縁もゆかりもない女子を助けてみるのも乙だろう──と、臥煙さんは、僕の来歴を揶揄するようなことを言ってきた。'
    print(replaceWord(inputSentance, "出す"))
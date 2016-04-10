from simserver import SessionServer
from gensim import utils

class Indexer(object):
    def __init__(self):
        self.server = SessionServer("./tmp")

    def _create_corpus(self, texts):
        corpus = []
        for id, text in texts:
            corpus.append({
                'id': id,
                'tokens': utils.simple_preprocess(text)
            })
        return corpus

    def index(self, texts):
        corpus = self._create_corpus(texts)
        utils.upload_chunked(self.server, corpus, chunksize=1000)
        self.server.train(corpus, method='lsi')
        self.server.index(corpus)

    def add_documents(self, texts):
        self.index(texts)

    def recommend(self, id, max_results=10):
        print "Id is: ", id
        return self.server.find_similar(id, max_results=max_results)

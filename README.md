Create a recommender system based on the Latent Semantic Indexing model. The index
is created from documents that are added via the /index endpoint. For the sake of
having a non empty corpus, I used the brown corpus (category=news), to create an
index from a set of about 4000 documents. The Web API is written in Node.js and exposes
two endpoints
* /index -> Index documents from the brown corpus
* /recommend/:id -> Given the id of a document, return all similar documents.

The indexing engine is written using gensim and simserver in python. The Node.js API
and the python indexing engine communicate via RPC using the zerorpc API (running over ZeroMQ). This is a WIP.

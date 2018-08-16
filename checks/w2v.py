# encoding: utf-8
import nltk
from nltk.cluster import KMeansClusterer
from gensim.models import Word2Vec

sentences = []
f = open('check.txt', 'r')
for line in f:
    sentences.append(line.split(' '))

num_features = 512
min_word_count = 5
num_workers = 256
context = 5
downsampling = 1e-3

model = Word2Vec(sentences, workers = num_workers, size = num_features, min_count = min_word_count, window = context, sample = downsampling)
model.save('w2v_first')

X = model[model.wv.vocab]

NUM_CLUSTERS = 10

kclusterer = KMeansClusterer(NUM_CLUSTERS, distance=nltk.cluster.util.cosine_distance, repeats=25)
assigned_clusters = kclusterer.cluster(X, assign_clusters = True)

print(model.wv.vocab.keys()[2])

f.close()

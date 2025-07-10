import redis
from embeddings import televisions, fan

try:
  r = redis.Redis(host='localhost', port=6379)
  r.set('aes::textEmbeddingCache::televisions', televisions)
except Exception as e:
  print("Redis exception")
  print(e)

import numpy as np
import hashlib

class LSH(object):
	def __init__(self, num_bands, band_width, num_buckets = 1000, random_seed=50):
		self._num_bands = num_bands
		self._band_width = band_width
		self._num_buckets = num_buckets

	def find_lsh_buckets(self, hash_signature):
		bands = [ tuple(hash_signature[i:i + self._band_width]) for i in range(0,len(hash_signature), self._band_width) ]
		lsh_hashes = [ (hash(row) % self._num_buckets) for row in bands]
		return lsh_hashes
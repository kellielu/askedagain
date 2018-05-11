import os
import boto3
import botocore
import time
import pickle

from termcolor import colored
from functools import reduce

from pyspark.sql import DataFrame

from itertools import chain
from nltk.corpus import wordnet


''' General utility functions used across multiple files '''


# Retrieves AWS bucket object
def get_bucket(bucket_name):
        s3 = boto3.resource('s3')
        try:
            s3.meta.client.head_bucket(Bucket=bucket_name)
        except botocore.exceptions.ClientError as e:
            return None
        else:
            return s3.Bucket(bucket_name)

# Unions dataframes with same schema
def union_dfs(*dfs):
    return reduce(DataFrame.unionAll, dfs)

# Decorator for timing processess
def time_process(func, process_name):
    start_time = time.time()
    func()
    end_time = time.time()
    print(colored("{0} run time (seconds): {1}".format(process_name, end_time - start_time), "magenta"))

# Wrappers for loading/saving pickle files
def load_pickle_file(filepath):
    if(os.path.isfile(filepath)):
        with open(filepath, "rb") as p:
            hs = pickle.load(p)
        return hs
    return None

def save_pickle_file(data, filename):
    with open(filename, "wb") as p:
        pickle.dump(data, p, protocol=pickle.HIGHEST_PROTOCOL)

# Returns first N synonyms of given word
def n_synonyms(n, word):
    synonyms = wordnet.synsets(word)
    lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
    return lemmas if n == "all" else lemmas[:n]

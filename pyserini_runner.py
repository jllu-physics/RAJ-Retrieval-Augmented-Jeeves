import subprocess

def run_pyserini_search(index_path, query, k=5):
    result = subprocess.run([
        "docker", "run", "--rm",
        "-v", ".:/app",
        "jeeves-pyserini",
        "python3", "-c",
        f"""
from pyserini.search.lucene import LuceneSearcher

searcher = LuceneSearcher('{index_path}')
hits = searcher.search('{query}', {k})
print([(h.docid, h.score) for h in hits])
"""
    ], capture_output=True, text=True)

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

if __name__ == '__main__':
    run_pyserini_search('indexes/sample_collection_jsonl', 'document', 5)

from fastapi import FastAPI, Query
from pyserini.search.lucene import LuceneSearcher

app = FastAPI()

# Load index once on startup
searcher = LuceneSearcher("/index")
searcher.set_bm25()  # Optional: tune parameters

@app.get("/search")
def search(q: str, k: int = 5):
    hits = searcher.search(q, k)
    results = [
        {"rank": i+1, "docid": hit.docid, "score": hit.score}
        for i, hit in enumerate(hits)
    ]
    return {"results": results}

from dotenv import load_dotenv
import os
import pickle

from langchain_core.documents import Document
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
from langchain_huggingface import (
    HuggingFaceEmbeddings
)
from langchain_pinecone import (
    PineconeVectorStore
)
from pinecone import (
    Pinecone,
    ServerlessSpec,
)

from utils import (
    extract_video_id,
    get_playlist_videos,
    get_video_title,
    get_transcript,
)

load_dotenv()

INDEX_NAME = "youtube-rag-assistant"

os.makedirs("data/bm25", exist_ok=True)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

pc = Pinecone(
    api_key=os.getenv(
        "PINECONE_API_KEY"
    )
)

if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1",
        ),
    )

index = pc.Index(INDEX_NAME)

vector_store = PineconeVectorStore(
    index=index,
    embedding=embeddings,
)

url = input(
    "Video or Playlist URL: "
)

videos = get_playlist_videos(url)

for video_url in videos:

    title = get_video_title(
        video_url
    )

    print(f"\nProcessing: {title}")

    video_id = extract_video_id(
        video_url
    )

    transcript = get_transcript(
        video_id
    )

    documents = []

    for seg in transcript:
        documents.append(
            Document(
                page_content=seg.text,
                metadata={
                    "video_id": video_id,
                    "video_title": title,
                    "source": video_url,
                    "timestamp": seg.start,
                },
            )
        )

    splitter = (
        RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
    )

    chunks = (
        splitter.split_documents(
            documents
        )
    )

    vector_store.add_documents(
        chunks,
        namespace=video_id,
    )

    with open(
        f"data/bm25/{video_id}.pkl",
        "wb",
    ) as f:
        pickle.dump(
            chunks,
            f,
        )

    print(
        f"Indexed {title}"
    )

print(
    "\nAll videos indexed successfully!"
)
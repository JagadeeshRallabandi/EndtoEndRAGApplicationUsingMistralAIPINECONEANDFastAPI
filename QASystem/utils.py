
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
HF_API_KEY = os.getenv("HF_TOKEN")
os.environ['HF_API_TOKEN'] = HF_API_KEY
print("Import Successfully")

def pinecone_config():
   
    document_store = PineconeDocumentStore(
            # environment="gcp-starter",
            index="default",
            namespace="default",
            dimension=768
        )
    return document_store
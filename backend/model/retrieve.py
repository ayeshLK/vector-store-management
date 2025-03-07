from typing import Optional
from pydantic import BaseModel, StrictStr, StrictInt, StrictFloat, Field


class VectorStoreRetrieveRequest(BaseModel):
    vectordb_provider: StrictStr = Field(..., title="Vectordb Provider",
                                         description="The provider of the vector database (e.g., 'Chroma', 'Pinecone')")
    pinecone_apikey: Optional[StrictStr] = Field(None, title="Pinecone Apikey",
                                                 description="API key for accessing the vector database provider")
    chroma_url: Optional[StrictStr] = Field(None, title="Chroma Url",
                                            description="The URL for the Chroma vector database instance")
    chroma_port: Optional[StrictStr] = Field(None, title="Chroma Port", description="The port Chroma is running on")
    postgres_host: Optional[StrictStr] = Field(None, title="Postgres Host", description="Host of the Postgres Database")
    postgres_user: Optional[StrictStr] = Field(None, title="Postgres User", description="User of the Postgres Database")
    postgres_password: Optional[StrictStr] = Field(None, title="Postgres Password",
                                                   description="Password of the Postgres Database")
    postgres_dbname: Optional[StrictStr] = Field(None, title="Postgres Dbname",
                                                 description="Name of the Postgres Database")
    postgres_table_name: Optional[StrictStr] = Field(None, title="Postgres Table Name",
                                                     description="Name of the table in the Postgres Database")
    collection_name: StrictStr = Field(..., title="Collection Name",
                                       description="The name of the collection to store or query from in the vector DB")
    embedding_model: StrictStr = Field(..., title="Embedding Model",
                                       description="The model used for embedding (e.g., OpenAI)")
    embedding_model_apikey: StrictStr = Field(..., title="Embedding Model Apikey",
                                              description="API key for accessing the embedding model")
    user_query: StrictStr = Field(..., title="User Query",
                                  description="The query submitted by the user for which the similar text chunks from the vector store will be retrieved")
    max_retrieve_chunks: StrictInt = Field(..., title="Max Retrieve Chunks",
                                           description="The maximum number of chunks to retrieve from the vector store")
    min_similarity_threshold: StrictFloat = Field(..., title="Min Similarity Threshold",
                                                  description="The minimum similarity to the given embedding of the given query, each retrieved chunk must have. (Value between 0 and 1)",
                                                  ge=0.0, le=1.0)

    class Config:
        schema_extra = {
            "example": {
                "chroma_url": "http://localhost:8000",
                "collection_name": "my_collection",
                "embedding_model": "OpenAI",
                "embedding_model_apikey": "your_embedding_model_apikey",
                "max_retrieve_chunks": 5,
                "min_similarity_threshold": 0.75,
                "user_query": "What is the capital of France?",
                "vectordb_provider": "Chroma"
            }
        }

class Chunk(BaseModel):
    text: StrictStr = Field(..., title="Text")
    source: StrictStr = Field(..., title="Source")

    class Config:
        schema_extra = {
            "example": {
                "text": "This is a chunk of text.",
                "source": "Some Source"
            }
        }

class RetrieveResponse(BaseModel):
    query: StrictStr = Field(..., title="Query")
    retrieved_chunks: list[Chunk] = Field(..., title="Retrieved Chunks")

    class Config:
        schema_extra = {
            "example": {
                "query": "What is the capital of France?",
                "retrieved_chunks": [
                    {
                        "text": "Paris is the capital of France.",
                        "source": "Wikipedia"
                    }
                ]
            }
        }

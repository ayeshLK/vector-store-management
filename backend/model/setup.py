from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr, Field


class VectorStoreSetupRequest(BaseModel):
    """Represents a request to set up a vector store with metadata and configurations."""

    request_id: StrictStr = Field(
        ...,
        title="Request Id",
        description="Unique identifier to link setup and upload requests"
    )
    file_count: Optional[StrictInt] = Field(
        1,
        title="File Count",
        description="The number of files uploaded with the request id"
    )
    vectordb_provider: StrictStr = Field(
        ...,
        title="VectorDB Provider",
        description="The provider of the vector database (e.g., 'Chroma', 'Pinecone')"
    )
    pinecone_apikey: Optional[StrictStr] = Field(
        None,
        title="Pinecone API Key",
        description="API key for accessing the Pinecone vector database"
    )
    chroma_url: Optional[StrictStr] = Field(
        None,
        title="Chroma URL",
        description="The URL for the Chroma vector database instance"
    )
    postgres_host: Optional[StrictStr] = Field(
        None,
        title="Postgres Host",
        description="Host of the Postgres Database"
    )
    postgres_user: Optional[StrictStr] = Field(
        None,
        title="Postgres User",
        description="User of the Postgres Database"
    )
    postgres_password: Optional[StrictStr] = Field(
        None,
        title="Postgres Password",
        description="Password of the Postgres Database"
    )
    postgres_dbname: Optional[StrictStr] = Field(
        None,
        title="Postgres Database Name",
        description="Name of the Postgres Database"
    )
    postgres_table_name: Optional[StrictStr] = Field(
        None,
        title="Postgres Table Name",
        description="Name of the table in the Postgres Database"
    )
    collection_name: StrictStr = Field(
        ...,
        title="Collection Name",
        description="The name of the collection to store or query from in the vector database"
    )
    embedding_model: StrictStr = Field(
        ...,
        title="Embedding Model",
        description="The model used for embedding (e.g., OpenAI)"
    )
    embedding_model_apikey: StrictStr = Field(
        ...,
        title="Embedding Model API Key",
        description="API key for accessing the embedding model"
    )
    chunking_strategy: StrictStr = Field(
        ...,
        title="Chunking Strategy",
        description="Strategy for chunking the file or text (e.g., 'sentence', 'paragraph')"
    )
    max_segment_size: StrictInt = Field(
        ...,
        title="Max Segment Size",
        description="The maximum size of each chunk/segment (in characters or tokens)"
    )
    max_overlap_size: StrictInt = Field(
        ...,
        title="Max Overlap Size",
        description="The maximum overlap size between chunks (in characters or tokens)"
    )

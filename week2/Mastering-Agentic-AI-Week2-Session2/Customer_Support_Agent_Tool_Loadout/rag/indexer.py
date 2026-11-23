import chromadb
from chromadb.api.shared_system_client import SharedSystemClient
from langchain_chroma import Chroma
from utils.embeddings import build_embeddings
from tools import catalog, ToolCard


def build_tool_index(persist_dir: str = ".chroma_tools") -> tuple[Chroma, dict[str, ToolCard]]:
    """Embed every tool's `name: description` and store it in a Chroma index.

    Returns the vector store (for semantic tool search) and a name -> ToolCard
    lookup so selected tool names can be mapped back to their callable handles.
    """
    embeddings = build_embeddings()
    name_to_card = {card.name: card for card in catalog}

    # Re-running this in a notebook leaves a cached Chroma system for this
    # persist_dir; a fresh build then fails with "An instance of Chroma already
    # exists ... with different settings". Clear the cache and own the client so
    # the cell is safely re-runnable.
    SharedSystemClient.clear_system_cache()
    client = chromadb.PersistentClient(path=persist_dir)

    # If the index already exists (and is fully populated), reuse it instead of
    # re-embedding every tool description.
    try:
        existing = client.get_collection("tool_cards")
        if existing.count() == len(catalog):
            print(f"  Reusing existing Chroma index ({existing.count()} tools, persist_dir={persist_dir!r})")
            vector_store = Chroma(
                client=client,
                collection_name="tool_cards",
                embedding_function=embeddings,
            )
            return vector_store, name_to_card
        # Partial/stale collection — drop it and rebuild from scratch.
        client.delete_collection("tool_cards")
    except Exception:
        # Collection doesn't exist yet — fall through to build it.
        pass

    texts, metadatas, ids = [], [], []
    for i, card in enumerate(catalog):
        texts.append(f"{card.name}: {card.description}")
        metadatas.append({"name": card.name})
        ids.append(f"tool-{i}")

    print(f"  Embedding {len(texts)} tool descriptions into Chroma (persist_dir={persist_dir!r})")
    vector_store = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas,
        ids=ids,
        collection_name="tool_cards",
        client=client,
    )

    return vector_store, name_to_card

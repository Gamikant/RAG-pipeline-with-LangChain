from src.search import RAGSearch

## Example usage
if __name__ == "__main__":
    rag_search = RAGSearch()
    print("Hello! I'm a RAG-based chatbot developed by you!")
    while True:
        query = input("RAG Bot: ")
        if not query:
            print("Please enter a valid query!")
            continue
        if query == 'quit' or query == 'exit':
            print("It was nice talking to you! GoodBye")
            break
        summary = rag_search.search_and_summarize(query, top_k = 3)
        print("Summary:", summary)

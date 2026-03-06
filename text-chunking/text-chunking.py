def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    if chunk_size < 1:
        raise ValueError("chunk_size should be >= 1")
    if not (0 <= overlap < chunk_size):
        raise ValueError('It must be "0 <= overlap < chunk_size"')

    step = chunk_size - overlap
    chunks = []
    start = 0

    while start < len(tokens):
        chunk = tokens[start:start + chunk_size]
        if not chunk:
            break
        chunks.append(chunk)
        if start + chunk_size >= len(tokens):
            break
        start += step

    return chunks
    
    
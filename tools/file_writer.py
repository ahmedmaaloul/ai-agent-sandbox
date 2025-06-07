def file_writer(*, path=None, content=None, filename=None, text=None) -> str:
    """
    Write content to a file.

    Args can be either:
    - path + content (correct input)
    - filename + text (fallback used by LLMs)

    Returns:
        str: status message
    """
    # Fallback for common LLM misnamings
    if path is None and filename is not None:
        path = filename
    if content is None and text is not None:
        content = text

    # Final check
    if not path or not content:
        return "❌ Missing required arguments: path/content or filename/text."

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ File written successfully to: {path}"
    except Exception as e:
        return f"❌ Failed to write file: {e}"

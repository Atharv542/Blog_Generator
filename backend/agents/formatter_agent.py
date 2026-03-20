import markdown

def formatter_agent(content: str):
    try:
        html = markdown.markdown(
            content,
            extensions=["fenced_code", "tables"]
        )

        return {
            "content_html": html,
            "content_markdown": content
        }

    except Exception as e:
        print("❌ Markdown Conversion Error:", e)

        return {
            "content_html": f"<p>{content}</p>",
            "content_markdown": content
        }
from agents.research_agent import get_research_agent
from agents.formatter_agent import formatter_agent   # ✅ ADD THIS
from agents.seo_agent import seo_agent
from agents.writer_agent import writer_agent
from agents.ui_agent import ui_agent
from agents.structure_agent import structure_agent
from orchestrator.zip_utils import create_zip

def generate_blog_pipeline(topic: str):

    topic = topic.strip()

    if len(topic.split()) <= 5:
        topic = f"Provide detailed research on {topic} with comparison if applicable"

    research_agent = get_research_agent()

    research_response = research_agent.invoke({
        "input": topic   # ✅ FIXED (important)
    })

    print("🔥 RAW RESEARCH:", research_response)

    research = research_response.get("output", "")

    if not research or len(research) < 50:
        research = f"Basic information about {topic}"

    draft = writer_agent(f"Topic: {topic}\n\nResearch:\n{research}")

    # 🔥 FORMATTER (VERY IMPORTANT)
    formatted = formatter_agent(draft)

    structured = structure_agent(draft)
    seo = seo_agent(draft)
    ui = ui_agent(structured)

    zip_path = create_zip(ui.get("files", {}))

    return {
        "title": seo.get("title"),
        "meta_description": seo.get("meta_description"),
        "slug": seo.get("slug"),
        "keywords": seo.get("keywords"),

        # ✅ THIS FIXES YOUR RAW TEXT ISSUE
        "content_html": formatted["content_html"],

        "structured": structured,
        "preview_html": ui.get("preview_html"),
        "download_path": zip_path
    }
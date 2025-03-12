from langchain_community.tools import YouTubeSearchTool

tool = YouTubeSearchTool()

def extract_youtube_link(name: str) -> str:
    return tool.run(f"{name} official trailer,1")

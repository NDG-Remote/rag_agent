from langchain_community.tools import YouTubeSearchTool
# from name_filter import extract_name

# name = extract_name("When did the movie The God Father come out?")

tool = YouTubeSearchTool()

def extract_youtube_link(name: str) -> str:
    return tool.run(f"{name} oficial trailer,1")

from src.states.blogstate import BlogState, Blog
from langchain_core.messages import SystemMessage, HumanMessage

class BlogNode:
    """
    A class representing a blog node
    """
    
    def __init__(self, llm):
        self.llm = llm
    
    def title_creation(self, state: BlogState):
        """
        Generate a title for the blog
        """
        if "topic" in state and state["topic"]:
            
            prompt = """
            You are an expert blogger content writer. Use markdown formatting. 
            Generate a blog title for the {topic}. This title should be creative and SEO friendly.
            """
            
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": response.content}}
        
        
    def content_generation(self, state: BlogState):
        """
        Generate a content for the blog
        """
        if "topic" in state and state["topic"]:
            
            prompt = """
            You are an expert blogger content writer. Use markdown formatting. 
            Generate a detailed blog content with detailed breakdown for the {topic}.
            Generate blog under 200 words.
            """
            
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state["blog"]["title"], "content": response.content}}

    def translation(self,state:BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt="""
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.

        ORIGINAL CONTENT:
        {blog_content}

        """
        print(state["current_language"])
        blog_content=state["blog"]["content"]
        messages=[
            HumanMessage(translation_prompt.format(current_language=state["current_language"], blog_content=blog_content))

        ]
        transaltion_content = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog": transaltion_content}
    
    def route(self, state: BlogState):
        """
        Route to the appropriate translation node based on the current language
        """
        return {"current_language": state["current_language"]}
    
    def route_decision(self, state: BlogState):
        """
        Decide the route based on the current language
        """
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french":
            return "french"
        else:
            return state["current_language"]
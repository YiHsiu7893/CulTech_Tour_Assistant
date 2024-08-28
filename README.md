# CulTech Tour Assistant
### Creating a Domain-Specific Voice Chatbot as a Virtual Tour Assistant
The goal is to build a Chinese language model that can respond to domain-specific questions and is mainly driven by voice. It also includes an avatar that simulates talking to create a more vivid conversation with the user.  
This is a side project as part of my participation in the 'Cultech +1' creativity competition. The resulting chatbot serves as a virtual tour assistant for Pei Gui Hall, a tourist attraction in Chiayi County.  
For more implementation details, refer to the [Report](https://github.com/YiHsiu7893/CulTech_Tour_Assistant/blob/main/Report.pdf). The flowchart is also provided below.
## Flowchart
<img src="https://github.com/YiHsiu7893/CulTech_Tour_Assistant/blob/main/pic/Flowchart.jpg" width=90% height=90%>

## Code Overview
| File                  | Functionality                                                                       |
|-----------------------|-------------------------------------------------------------------------------------|
| Avatar/add_block      | draws a conversation block on the avatar interface                                  |
| Knowledge/web_crawler | crawls information from the tourist attraction websites                             |
| FixedBase             | implements the fixed-base retrieval mechanism for chatbot responses                 |
| RAG                   | implements the RAG (Retrieve and Generate) mechanism for chatbot responses          |
| audio                 | converts speech to text and text to speech                                          |
| avatar                | creates an avatar interface that simulates talking and also synchronizes with voice |
| main                  | executes the chatbot application                                                    |

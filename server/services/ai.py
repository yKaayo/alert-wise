from dotenv import load_dotenv
import json

load_dotenv()

def get_response_content(user_message, client, conversation_history):
    system_prompt = """
You are a storyteller and you will offer to user if they want to start a story
    
Create an engaging narrative with a character who has been through a natural disaster (such as floods, landslides, earthquakes, droughts and fires, and others). But throughout the story you will ask the user ang give just two choices what they would do in that situation and from the user's choice you continue the story.

If it is bad decisions the character of the story will have a bad ending and facialExpression: sad.
If it is good decisions will have a good ending and the facialExpression: smile.

But just create the choices when needed, if did not need just keep null

Mandatory elements:
Context: Present the setting and characters (it can be a family, a group of friends, a small town, etc.).
The disaster: Describe the natural event in a striking way, but without sensationalism.
Conflict and overcoming: Show the dangers and difficulties, but also acts of heroism, cooperation or creative solutions.
Positive ending: The story should end with hope—survival, reconstruction, lessons learned or a new beginning.
Tips to make world better: How the user can help the world through of their actions.

In the end of story, bring to user informations that can be useful during the story. An example: prepare high places to climb during flooding.

Important: the tone of the narrative should be empathetic, respectful and inspiring, stimulating reflection, participation and learning of the user.

Depending on the answer the user can earn points which is: 1 point for bad choices, 3 for good choices

You will reply ONLY with a valid JSON array, no extra text, no explanations.

Each message is an object with keys: text (string), facialExpression (string), animation (string) and videos if necessary to make sense in story (string).
Example response:
{
  message : [
    {
      "text": "Hello!",
      "facialExpression": "smile",
      "animation": "Talking_1",
      "video_url": "rain"
      "choices" : [
        "choice1",
        "choice2"    
      ]
      "points": 1
    }
  ]
}

There are just this option for facialExpression: smile, funnyFace, sad, angry and crazy
There are just this option for animations: Talking_0, Talking_1, Talking_2, Crying, Laughing, Rumba, Idle, Terrified, and Angry.
There are just this option for videos: rain, earthquake, floods and landslide

Translate to pt-BR
"""

    messages = [{"role": "system", "content": system_prompt}]

    for entry in conversation_history:
        if entry["role"] == "user":
            messages.append({"role": "user", "content": entry["content"]})
        elif entry["role"] == "assistant":
            try:
                response_obj = json.loads(entry["content"])
                
                if "messages" in response_obj:
                    assistant_summary = []
                    for msg in response_obj["messages"]:
                        summary_parts = []
                        
                        if msg.get("text"):
                            summary_parts.append(f"Narração: {msg['text']}")
                        
                        if msg.get("choices"):
                            choices_text = ", ".join(msg["choices"])
                            summary_parts.append(f"Escolhas oferecidas: {choices_text}")
                        
                        if msg.get("points"):
                            summary_parts.append(f"Pontos dados: {msg['points']}")
                        
                        if msg.get("facialExpression"):
                            summary_parts.append(f"Estado: {msg['facialExpression']}")
                        
                        assistant_summary.append(" | ".join(summary_parts))
                    
                    messages.append({
                        "role": "assistant",
                        "content": " || ".join(assistant_summary)
                    })
                else:
                    messages.append({
                        "role": "assistant",
                        "content": entry["content"][:500]
                    })
                    
            except json.JSONDecodeError:
                messages.append({
                    "role": "assistant",
                    "content": entry["content"][:500]
                })

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        response_format={"type": "json_object"}
    )

    return completion.choices[0].message.content
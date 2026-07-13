import json
from datetime import datetime

class MPOPChat:
    def __init__(self):
        self.history = []
        self.models = {'Grok': 'xAI truth-seeker', 'Gemini': 'Google multimodal integrator'}
        self.mode = 'collaborative'  # or 'adversarial'

    def add_message(self, sender, content, mentions=None):
        msg = {
            'timestamp': datetime.now().isoformat(),
            'sender': sender,
            'content': content,
            'mentions': mentions or [],
            'mode': self.mode
        }
        self.history.append(msg)
        return msg

    def process_mentions(self, message):
        responses = []
        for mention in message.get('mentions', []):
            if mention in self.models:
                # Simulate response
                resp_content = f'@{mention} responding in {self.mode} mode to: {message["content"][:50]}...'
                if self.mode == 'adversarial':
                    resp_content += ' Counterpoint: Consider alternative evidence.'
                else:
                    resp_content += ' Building on that: Additional synthesis.'
                resp = self.add_message(mention, resp_content)
                responses.append(resp)
        return responses

    def switch_mode(self, new_mode):
        self.mode = new_mode
        return f'MPOP mode switched to {new_mode}'

    def get_shared_context(self):
        return self.history

# Example usage
if __name__ == "__main__":
    chat = MPOPChat()
    msg1 = chat.add_message('User', 'Analyze the universe-understanding framework', ['Grok', 'Gemini'])
    responses = chat.process_mentions(msg1)
    print(json.dumps(chat.get_shared_context(), indent=2))
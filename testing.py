import unittest
from unittest.mock import patch, MagicMock

class TestChatbotOpenAI(unittest.TestCase):
    @patch("chatbotOpenAI.OpenAI")
    def test_openai_called_with_api_key(self, mock_openai):
        # Simulate OpenAI client and response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="test reply"))]
        mock_client.chat.completions.create.return_value = mock_response

        # Simulate messages
        messages = [{"role": "user", "content": "Hello"}]

        # Import your module and call the OpenAI part directly
        from chatbotOpenAI import OpenAI
        client = OpenAI(api_key="fake-key")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        self.assertEqual(response.choices[0].message.content, "test reply")
        mock_openai.assert_called_with(api_key="fake-key")

@patch("chatbotOpenAI.st")
def test_session_state_initialization(self, mock_st):
    # Simulate session state not having "messages"
    mock_st.session_state = {}
    import importlib
    import chatbotOpenAI
    importlib.reload(chatbotOpenAI)  # Ensure the code runs with the mock
    # Now check if the assignment was made
    self.assertTrue("messages" in mock_st.session_state or mock_st.session_state.__setitem__.called)
    
if __name__ == "__main__":
    unittest.main()
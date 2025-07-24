import unittest
from unittest.mock import patch, MagicMock
import openai from chatbotOpenAI
class TestChatbotOpenAI(unittest.TestCase):

    @patch("openai.OpenAI")
    def test_openai_called_with_api_key(self, mock_openai):
        # Mock the client and its response
        mock_client = MagicMock()
        mock_openai.return_value = mock_client

        mock_response = MagicMock()
        mock_response.choices = [MagicMock(message=MagicMock(content="test reply"))]
        mock_client.chat.completions.create.return_value = mock_response

        # Simulate calling OpenAI
        from openai import OpenAI
        messages = [{"role": "user", "content": "Hello"}]

        client = OpenAI(api_key="fake-key")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        self.assertEqual(response.choices[0].message.content, "test reply")
        mock_openai.assert_called_with(api_key="fake-key")

if __name__ == "__main__":
    unittest.main()

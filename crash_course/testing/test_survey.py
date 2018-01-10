import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.survey = AnonymousSurvey(question)
        self.responses = ['English', 'Russian', 'Spanish']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.survey.store_response(self.responses[0])

        self.assertIn(self.responses[0], self.survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.survey.responses)

unittest.main()
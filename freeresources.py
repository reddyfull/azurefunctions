import unittest
from unittest.mock import patch
from your_module import get_resource_groups, is_resource_empty

class TestResourceFunctions(unittest.TestCase):

    @patch('requests.get')
    def test_get_resource_groups_success(self, mock_get):
        # Mocking a successful response from the Azure API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"value": [{"name": "group1"}, {"name": "group2"}]}

        subscription_id = "217d2bdc-2706-4aa7-be71-457045f1baba"
        token = "sample_token"

        result = get_resource_groups(subscription_id, token)
        self.assertEqual(result, [{"name": "group1"}, {"name": "group2"}])

    @patch('requests.get')
    def test_get_resource_groups_failure(self, mock_get):
        # Mocking a failure response from the Azure API
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        subscription_id = "217d2bdc-2706-4aa7-be71-457045f1baba"
        token = "sample_token"

        with self.assertRaises(Exception) as context:
            get_resource_groups(subscription_id, token)

        self.assertIn('Failed to get resource groups', str(context.exception))

    def test_is_resource_empty(self):
        # As the is_resource_empty function always returns False, we can directly test that
        resource = {"name": "sample_resource"}
        result = is_resource_empty(resource)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()

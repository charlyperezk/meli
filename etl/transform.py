import pandas as pd

class Transformer:
    """Data transformation class responsible for transforming MercadoLibre API response into a DataFrame.

    This class takes a MercadoLibre API response and extracts relevant information to create a structured DataFrame.

    Attributes:
        df (DataFrame): Pandas DataFrame to store the transformed data.

    Methods:
        transform(response): Transform the API response into a structured DataFrame.
    """

    def __init__(self) -> None:
        """Initialize the Transformer.

        Initializes an empty Pandas DataFrame for storing transformed data.

        Args:
            None
        """
        self.df = pd.DataFrame()

    def transform(self, response):
        """Transform the API response into a structured DataFrame.

        This method processes the provided API response, extracts relevant information, and creates a structured DataFrame with specific columns.

        Args:
            response (dict): The MercadoLibre API response.

        Returns:
            None
        """
        columns = ['id', 'title', 'condition', 'thumbnail_id']

        for result in response['results']:
            result_dict = {
                'id': result['id'],
                'title': result['title'],
                'condition': result['condition'],
                'thumbnail_id': result['thumbnail_id']
            }

            for attribute in result['attributes']:
                attribute_name = attribute['name']
                attribute_value = attribute['value_name']
                result_dict[attribute_name] = attribute_value

                if attribute_name not in columns:
                    columns.append(attribute_name)

            self.df = pd.concat(
                [self.df, pd.DataFrame([result_dict])], ignore_index=True)

        self.df = self.df[columns]

        print("\n", self.df)

class MockingHelper:
    @staticmethod
    def mock_static_or_regular_function():
        pass

    @staticmethod
    def get_name_of_attribute_or_function(x):
        return x.__name__
import json

class SelectionHandler:
    """Handles the selection of filters and options for querying MercadoLibre products.

    Attributes:
        selection (list): List of selected filters and options.

    Methods:
        choose(attrs: json) -> list: Allows the user to select filters and options based on provided attributes.
        show_filters(attrs: json) -> dict or None: Displays available filters with values and enables user selection.
        choose_options(filter: dict) -> list: Enables the user to select options for a chosen filter.

    Args:
        attrs (json): A JSON object containing filter and option attributes.
    """

    def __init__(self):
        self.selection = []

    def choose(self, attrs: json) -> list:
        """Allows the user to select filters and options based on provided attributes.

        Args:
            attrs (json): A JSON object containing filter and option attributes.

        Returns:
            list: List of selected filters and options.
        """

        try:
            if len(attrs) > 0:
                while True:
                    selected_filter = self.show_filters(attrs)
                    if selected_filter:
                        self.selection.append(selected_filter)
                    else:
                        break
                return self.selection
            else:
                print("No filters available.")
                return []
        except Exception:
            return None

    def show_filters(self, attrs) -> dict or None:
        """Displays available filters with values and enables user selection.

        Args:
            attrs (json): A JSON object containing filter and option attributes.

        Returns:
            dict or None: The selected filter or None if the user quits.
        """

        print("\nCategories with values: ")
        available_filters = [f for f in attrs if 'values' in f and len(
            f['values']) > 0 and not f.get('tags', {}).get('hidden')]
        for index, filter in enumerate(available_filters, 1):
            selected_text = "[Selected]" if filter.get('selected') else ""
            print(f"\t{index}. {filter['name']} {selected_text}")

        selected = input(f"Select a filter (or 'Q' to quit): ").strip().lower()
        if selected == 'q':
            return None

        try:
            selected_index = int(selected)
            if 1 <= selected_index <= len(available_filters):
                selected_filter = available_filters[selected_index - 1]
                selected_filter['selected'] = True
                return self.choose_options(selected_filter)
            else:
                print("Invalid input. Please enter a valid filter index.")
        except ValueError:
            print("Invalid input. Please enter a valid filter index.")
        return None

    def choose_options(self, filter) -> list:
        """Enables the user to select options for a chosen filter.

        Args:
            filter (dict): The selected filter.

        Returns:
            list: List of selected options.
        """

        selected_filter = filter
        while True:
            print(f"\nSelected filter: {selected_filter['name']}")
            if 'values' in selected_filter and len(selected_filter['values']) > 0:
                print("\nOptions: ")
                for sub_index, option in enumerate(selected_filter['values'], 1):
                    selected_text = "[Selected]" if option.get(
                        'selected') else ""
                    print(f"\t{sub_index}. {option['name']} {selected_text}")

                sel = input(
                    "Select an option (or 'Q' to quit): ").strip().lower()
                if sel == 'q':
                    break

                try:
                    selected_index = int(sel)
                    if 1 <= selected_index <= len(selected_filter['values']):
                        selected_option = selected_filter['values'][selected_index - 1]
                        if not selected_option.get('selected'):
                            selected_option['selected'] = True
                        else:
                            print(
                                "Option is already selected. Please choose a different option.")
                    else:
                        print("Invalid input. Please enter a valid option index.")
                except ValueError:
                    print("Invalid input. Please enter a valid option index.")
            else:
                print("No options available.")
                break

        return selected_filter

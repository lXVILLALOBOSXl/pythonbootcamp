def get(sentence, instance):
    correct = False
    while not correct:
        try:
            user_input = input(sentence)
            if instance == str:
                user_input = user_input.lower()  # Convert to lowercase
            input_instance = instance(user_input)  # Try to create an instance using user_input
            correct = True  # Input is valid
            return input_instance  # Return the valid instance
        except KeyboardInterrupt:
            raise  # Re-raise the KeyboardInterrupt to exit gracefully
        except ValueError:
            print("Invalid input. Please try again.")



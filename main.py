# =============================================================================
# OmniCo Confidential
# -------------------
# This source code contains proprietary information of OmniCo.
# =============================================================================

def main():
    # Initialize the stats dictionary for each algorithm
    stats = {
        'JoyStream': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'SerenityFlow': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'DeepPulse': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        }
    }

    # Open the CSV file and read data
    with open('euphoria_data.csv', 'r') as file:
        # Skip the header line
        header = file.readline()

        # Read each line in the file
        for line in file:
            # Remove any trailing whitespace characters like newline
            line = line.strip()

            # Split the line into a list of values
            columns = line.split(',')

            # Assign each column to a variable
            user_id = columns[0]
            algorithm = columns[1]

            # TODO: Define session_duration and happiness_rating variables and convert them to integers
            # Hint: Use the int() function to convert strings to integers
            # session_duration = ?
            # happiness_rating = ?

            # Update stats based on the algorithm
            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                # Handle any unexpected algorithm names
                print(f"Unknown algorithm: {algorithm}")

    # TODO: Calculate averages for each algorithm
    # For each algorithm in the stats dictionary:
    #   - Calculate avg_happiness = total_happiness / session_count
    #   - Calculate avg_duration = total_duration / session_count
    #   - Store these back into the stats dictionary under 'avg_happiness' and 'avg_duration'

    # TODO: Determine the algorithm with the highest average happiness rating
    # Initialize variables to keep track of the highest average happiness and the corresponding algorithm
    # Loop through stats to compare avg_happiness values

    # TODO: Determine the algorithm with the longest average session duration
    # Initialize variables to keep track of the longest average duration and the corresponding algorithm
    # Loop through stats to compare avg_duration values

    # TODO: Print the report
    # Use print statements to display the results in a formatted way
    # Follow the structure provided in the example output

if __name__ == "__main__":
    main()
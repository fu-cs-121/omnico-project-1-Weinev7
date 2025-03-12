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

            
            session_duration = int(columns[2])
            happiness_rating = int(columns[3])

            # Update stats based on the algorithm
            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                # Handle any unexpected algorithm names
                print(f"Unknown algorithm: {algorithm}")

        largest_algorithm_avg =0
        largest_algorithm_happiness=""
        largest_algorithm_duration=0
        largest_algorithm_length=""
    # TODO: Calculate averages for each algorithm
    #print(stats['JoyStream'].get('total_happiness'))
    print("Average Happiness Rating per Algorithm:")
    for algorithm,algorithm_stats in stats.items():
        algorithm_avg= algorithm_stats['total_happiness']/algorithm_stats['session_count']
        
        print(f"-{algorithm}: {algorithm_avg}")
        if largest_algorithm_avg<algorithm_avg:
            largest_algorithm_avg=algorithm_avg
            largest_algorithm_happiness= algorithm
    print("\n")
    print("Total Number of Sessions per Algorithm:")
    for algorithm,algorithm_stats in stats.items():
        algorithm_sessions= algorithm_stats['session_count']
        
        print(f"-{algorithm}: {algorithm_sessions}")
    print("\n")
    for algorithm,algorithm_stats in stats.items():
        algorithm_duration= algorithm_stats['total_duration']/algorithm_stats['session_count']
        
        print(f"-{algorithm}: {algorithm_duration}")
        if largest_algorithm_duration<algorithm_duration:
            largest_algorithm_duration=algorithm_duration
            largest_algorithm_length= algorithm
    print("\n")
    print("Highest Average Happiness Rating:")
    print(f"-{largest_algorithm_happiness} with an average happiness rating of {largest_algorithm_avg}")

    print("\nLongest Average Session Duration:")
    print(f"-{largest_algorithm_length} with an average session duration of {largest_algorithm_duration} minutes")


if __name__ == "__main__":
    main()
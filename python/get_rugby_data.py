from bs4 import BeautifulSoup
import urllib


# Gather rugby data from online database (http://www.lassen.co.nz/pickandgo.php) and put into a csv file

# Parse data from specified 'url' and save in CSV format
def get_rugby_data(url, filename):
    html_data = urllib.urlopen(url).read()

    # Create BeautifulSoup parser based on HTML data from url
    soup = BeautifulSoup(html_data)

    # Extract results table from HTML
    results = soup.find_all('table')[1]

    # Parse all table data into a CSV string - not too much data from one request
    results_string = ''
    for row in results.find_all('tr')[1:]:
        # Get all columns for one row
        cells = row.findAll('td')
        try: 
            teams = cells[3].get_text().split(' v ')  # In format 'TEAMA v TEAMB'
            team_a = teams[0]
            team_b = teams[1]
            results = cells[4].get_text().split('-')  # In format 'XX-YY'
            result_a = results[0]
            result_b = results[1]
            tries = cells[5].get_text().split(':')  # In format 'XX:YY'
            try_a = tries[0]
            try_b = tries[1]
        except:
            continue

        # Sort fixtures alphabetically - easier to process for Gephi use
        if team_a < team_b:
            results_string += team_a + "," + team_b + "," + result_a + "," + result_b + "," + try_a + "," + try_b + "\n"
        else:
            results_string += team_b + "," + team_a + "," + result_b + "," + result_a + "," + try_b + "," + try_a + "\n"

    # Save obtained data to specified file
    results_file = open(filename, 'w')
    results_file.write('TeamA, TeamB, ScoreA, ScoreB, TriesA, TriesB \n')  # Header row
    results_file.write(results_string)  # Data rows
    results_file.close()

# Example usage - all World Cup matches
# get_rugby_data('http://www.lassen.co.nz/pickandgo.php?fyear=1987&tyear=2015&teama=ALL&tourn=WC#hrh', 'test.csv')
import csv
import os

def clean_movie_data(input_file, output_file):
    # Year corrections dictionary
    year_corrections = {
        'Memento': 2000, 'Get Out': 2017, 'The Incredibles': 2004, 
        'The Hunger Games': 2012, 'The Departed': 2006, 'Inglourious Basterds': 2009,
        'Encanto': 2021, 'Titanic': 1997, 'Divergent': 2014, 'Soul': 2020,
        'The Ring': 2002, 'Toy Story': 1995, 'The Flash': 2023, 'The Godfather': 1972,
        'Forrest Gump': 1994, 'The Suicide Squad': 2021, 'Blue Beetle': 2023,
        'Shrek': 2001, 'Django Unchained': 2012, 'Spider-Man: No Way Home': 2021,
        'Frozen': 2013, 'Superman': 1978, 'Interstellar': 2014, 'Iron Man': 2008,
        'Twilight': 2008, 'Captain America: Civil War': 2016, 'Deadpool': 2016,
        'Mad Max: Fury Road': 2015, 'Inside Out': 2015, 'Us': 2019,
        'Avengers: Endgame': 2019, 'Insidious': 2010, 'A Quiet Place': 2018,
        'Zootopia': 2016, 'Big Hero 6': 2014, 'Logan': 2017, 'Birdman': 2014,
        'The Conjuring': 2013, 'Catch Me If You Can': 2002, 'Arrival': 2016,
        'Ratatouille': 2007, 'Inception': 2010, '12 Years a Slave': 2013,
        'Guardians of the Galaxy': 2014, 'Kung Fu Panda': 2008, 'Wonder Woman': 2017,
        'Moana': 2016, 'Man of Steel': 2013, 'The Matrix': 1999, 'Whiplash': 2014
    }
    
    # Genre corrections
    genre_corrections = {
        'Memento': 'Thriller', 'Get Out': 'Horror', 'The Incredibles': 'Animation',
        'The Hunger Games': 'Action', 'The Departed': 'Crime', 'Inglourious Basterds': 'War',
        'Encanto': 'Animation', 'Titanic': 'Romance', 'Divergent': 'Action',
        'Soul': 'Animation', 'The Ring': 'Horror', 'Toy Story': 'Animation',
        'The Flash': 'Action', 'The Godfather': 'Crime', 'Forrest Gump': 'Drama',
        'The Suicide Squad': 'Action', 'Blue Beetle': 'Action', 'Shrek': 'Animation',
        'Django Unchained': 'Western', 'Spider-Man: No Way Home': 'Action',
        'Frozen': 'Animation', 'Superman': 'Action', 'Interstellar': 'Sci-Fi',
        'Iron Man': 'Action', 'Twilight': 'Romance', 'Captain America: Civil War': 'Action',
        'Deadpool': 'Action', 'Mad Max: Fury Road': 'Action', 'Inside Out': 'Animation',
        'Us': 'Horror', 'Avengers: Endgame': 'Action', 'Insidious': 'Horror',
        'A Quiet Place': 'Horror', 'Zootopia': 'Animation', 'Big Hero 6': 'Animation',
        'Logan': 'Action', 'Birdman': 'Drama', 'The Conjuring': 'Horror',
        'Catch Me If You Can': 'Biography', 'Arrival': 'Sci-Fi', 'Ratatouille': 'Animation',
        'Inception': 'Sci-Fi', '12 Years a Slave': 'Biography'
    }
    
    # Country standardization
    country_corrections = {
        'USA': 'United States', 'UK': 'United Kingdom', 'US': 'United States'
    }
    
    # First, convert Excel to CSV (manual step)
    print("Please convert your Excel file to CSV format first.")
    print("1. Open your Excel file")
    print("2. Click 'File' > 'Save As'")
    print("3. Choose 'CSV (Comma delimited)' format")
    print("4. Save as 'movie_dataset_6000.csv'")
    input("Press Enter after you've converted the file to CSV...")
    
    # Read and clean the CSV file
    cleaned_data = []
    total_rows = 0
    cleaned_rows = 0
    
    try:
        with open('movie_dataset_6000.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Read header row
            cleaned_data.append(headers)
            
            for row in reader:
                total_rows += 1
                try:
                    title, genre, year, rating, votes, director, duration, country, box_office = row
                    
                    # Convert numeric values
                    try:
                        year = int(float(year))
                        rating = float(rating)
                        votes = int(float(votes))
                        duration = int(float(duration))
                        box_office = float(box_office)
                    except ValueError:
                        continue
                    
                    # Apply corrections
                    year = year_corrections.get(title, year)
                    genre = genre_corrections.get(title, genre)
                    country = country_corrections.get(country, country)
                    
                    # Data validation
                    if not (1900 <= year <= 2023):
                        continue
                    if not (1.0 <= rating <= 10.0):
                        continue
                    if not (30 <= duration <= 240):
                        continue
                    if votes < 0:
                        continue
                    if box_office < 0 or box_office > 3000:
                        continue
                    
                    # Add to cleaned data
                    cleaned_data.append([
                        title, genre, year, rating, votes, director, 
                        duration, country, box_office
                    ])
                    cleaned_rows += 1
                    
                except Exception as e:
                    continue
        
        # Write cleaned data to new CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(cleaned_data)
        
        print(f"Cleaning complete!")
        print(f"Original rows: {total_rows}")
        print(f"Cleaned rows: {cleaned_rows}")
        print(f"Saved to: {output_file}")
        
    except FileNotFoundError:
        print("Error: CSV file not found. Please make sure you converted the Excel file to CSV.")
    except Exception as e:
        print(f"Error: {e}")

# Run the cleaning
clean_movie_data('movie_dataset_6000.xlsx', 'movie_dataset_6000_cleaned.csv')

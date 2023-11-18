# Artist Lyrics Analysis

This Python script analyzes the lyrics of songs by a specific artist, identifies the most frequently used words, and outputs a word count file. It utilizes the `lyricsgenius` Python library, a wrapper for the Genius API, to fetch the lyrics and then processes them to create a detailed word frequency analysis.

## Features

- Fetches all the lyrics for a specified artist using the `lyricsgenius` library.
- Cleans and processes the lyrics to extract meaningful data.
- Generates a word count file, listing words based on their frequency in the artist's songs.

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3
- Required Python libraries: `pandas`, `lyricsgenius`

## Setup

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:Fredd124/Artist-Most-Said-Words.git
   cd Artist-Most-Said-Words
   ```
   
2. **Install Required Libraries**:
   ```bash
   pip install pandas lyricsgenius
   ```
   
3. **Set up Genius API Token**:
  1. **Obtain a Genius API token**.
     - Visit the [Genius API page](https://genius.com/developers) and follow the instructions to obtain an API token.
  
  2. **Create a `.env` file in the root directory**.
     - Add your Genius API token to the file you created. Use the following format:
  
       ```makefile
       TOKEN=your_genius_api_token_here
       ```

## Usage 

Run the script with Python from the terminal:

```bash
python artist_lyrics_analysis.py
```

Follow the prompt to enter the artist's name. The script will then process the lyrics and generate a file with the word count in the current directory.

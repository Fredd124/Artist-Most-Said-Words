# Artist Most Said Word Analysis

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
python artist_word_count.py
```

Follow the prompt to enter the artist's name. The script will then process the lyrics and generate a file with the word count in the current directory.

## Notes/Observations

While developing and using this script, there are several important observations and limitations to keep in mind:

1. **LyricsGenius Library Limitations**:
   - Since the script uses the `lyricsgenius` library to fetch song lyrics, it is bound by the functionalities and limitations of this library. As a result, not all desired data might be available or retrievable in the way expected.

2. **Handling Bands and Solo Artists**:
   - When working with bands, the script might discard some songs. This is due to the tags in the lyrics referencing individual artists rather than the band as a whole, making it challenging to determine if these songs belong to the band, since there is no information when making the request for the songs for what members the band is composed of.

3. **Performance with Popular Artists**:
   - Fetching songs of very popular artists with extensive discographies can be time-consuming. The script needs to retrieve and process a large amount of data, which might result in longer execution times.

4. **Artist Features**:
   - The script primarily focuses on the main songs of an artist. Songs where the artist is featured (artist feats) are not typically included in the analysis. This might result in a less comprehensive representation of the artist's lyrical usage.

These notes are based on the current implementation and behavior of the script and are subject to change with future updates and improvements.


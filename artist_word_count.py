import re
import json
import pandas as pd
from collections import Counter
import string
import os
import dotenv
import lyricsgenius as lg

def clean_first_line(text):
    """
    Removes everything before the first '[' and returns the cleaned text.
    """
    formatted_text = re.sub(r'.*?(?=\[)', '', text, 1, flags=re.DOTALL)
    return formatted_text.strip()

def clean_last_line(text):
    """
    Removes patterns like digits followed by 'Embed' at the end of the text.
    """
    pattern = re.compile(r'\s?\d*\s?Embed$')
    return re.sub(pattern, '', text)

def clean_might_also_like(text):
    """
    Removes "You might also like" from the text.
    """
    return text.replace("You might also like", "").strip()

def format_text(text):
    """
    Ensures that there is a newline before each tag in the text.
    """
    formatted_text = re.sub(r'(\[.*?\])', r'\n\1', text)
    return formatted_text.strip()

def keep_artist_paragraphs(text, artist_names_list):
    """
    Keeps only the sections of the text that are sang by the specified artist.
    """
    pattern = re.compile(r'(\[.*?\])', re.DOTALL)
    sections = re.split(pattern, text)

    keep_next_section = True
    filtered_sections = []

    for section in sections:
        if re.match(pattern, section):
            keep_next_section = any(artist_name.lower() in section.lower() for artist_name in artist_names_list) or (":" not in section)
            if keep_next_section:
                filtered_sections.append(section)
        elif keep_next_section:
            filtered_sections.append(section)

    return "".join(filtered_sections)

def remove_tags(text):
    """
    Removes tags (enclosed in square brackets) from the text.
    """
    pattern = re.compile(r'\[.*?\]\n?', re.DOTALL)
    return re.sub(pattern, '', text)

def remove_empty_lines(text):
    """
    Replaces multiple consecutive newline characters with a single newline.
    """
    return re.sub(r'\n\s*\n', '\n', text)

def clean_lyrics(lyrics, artist_names_list):
    """
    Cleans the lyrics text by applying various cleaning functions.
    """
    lines = lyrics.split('\n')
    
    if len(lines) > 1:
        lines = lines[1:]
    if lines:
        lines[len(lines)-1] = clean_last_line(lines[len(lines)-1])

    lines = [clean_might_also_like(line) for line in lines]
    formatted_lyrics = '\n'.join(lines)
    formatted_lyrics = keep_artist_paragraphs(formatted_lyrics, artist_names_list)
    formatted_lyrics = remove_tags(formatted_lyrics)
    formatted_lyrics = remove_empty_lines(formatted_lyrics)

    return formatted_lyrics

def fetch_lyrics(genius, artist_name):
    try:
        artist = genius.search_artist(artist_name)
        artist.save_lyrics()
        return artist
    except Exception as e:
        print(f'Error when searching for artist or saving lyrics: {e}')
        return None

def read_lyric_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'File not found: {filename}')
    except json.JSONDecodeError as e:
        print(f'Error decoding file {filename}: {e}')
    return None

def process_lyrics_data(data, artist_names):
    songs_data = [{'release_date': song.get('release_date'), 'lyrics': song.get('lyrics')} for song in data['songs']]
    df = pd.DataFrame(songs_data)
    df = df[df['release_date'].notna()]
    df['lyrics'] = df['lyrics'].apply(lambda lyrics: clean_lyrics(lyrics, artist_names) if lyrics else '')
    return df

def save_word_counts(df, artist_name):
    all_lyrics = ' '.join(df['lyrics']).lower()
    words = [''.join(c for c in w if c not in string.punctuation) for w in all_lyrics.split()]
    word_counts = Counter(words)

    words_df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Count'])
    words_df.sort_values(by='Count', ascending=False, inplace=True)
    words_df.to_csv(artist_name+'_word_counts.csv', index=False)

def main():
    dotenv.load_dotenv()
    genius_access_token = os.getenv('TOKEN')
    genius = lg.Genius(genius_access_token)

    chosen_artist = input('Enter the artist name: ')
    artist = fetch_lyrics(genius, chosen_artist)
    if not artist:
        return

    artist_name = artist.name.replace('\u200b', '').replace(' ', '')
    file_name = f'Lyrics_{artist_name}.json'

    data = read_lyric_data(file_name)
    if not data:
        return

    artist_names_list = data.get('alternate_names', []) + [artist_name]
    df = process_lyrics_data(data, artist_names_list)

    save_word_counts(df, artist_name)
    os.remove(file_name)

if __name__ == '__main__':
    main()
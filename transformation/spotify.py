import pandas as pd

def drop_columns_spotify(df):
    """
    This function drops the 'Unnamed: 0' column from DataFrame.

    Parameters:
    - df: Pandas DataFrame.
    
    Returns:
    - df: Pandas DataFrame without the 'Unnamed: 0' column.
    """
    df = df.drop(['Unnamed: 0'], axis=1)
    return df


def drop_track_id(df):
    """
    This function removes rows from a DataFrame where the 'track_id' column matches a specific value.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with rows removed where 'track_id' is '1kR4gIb7nGxHPI3D2ifs59'.
    """
    df = df[df['track_id'] != '1kR4gIb7nGxHPI3D2ifs59']
    return df


def drop_duplicate_rows(df):
    """
    This function removes duplicate rows from a DataFrame.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with duplicate rows removed.
    """
    df.drop_duplicates(inplace=True)
    return df


def assign_popularity_levels(df):
    """
    This function assigns popularity levels to each row in a DataFrame based on the 'popularity' column.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with a new column 'popularity_level' indicating the popularity level of each track.
    """
    interval_values = [0, 20, 40, 60, 80, 101]
    level_names = ['Very Low', 'Low', 'Medium', 'High', 'Very High']

    df['popularity_level'] = pd.cut(df['popularity'], bins=interval_values, labels=level_names, right=False)
    return df


def convert_duration(df):
    """
    This function converts the duration of songs from milliseconds to minutes and seconds format.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with a new column 'duration_min_sec' indicating the duration of each song in minutes and seconds format.
    """
    df['duration_min_sec'] = pd.to_datetime(df['duration_ms'], unit='ms').dt.strftime('%M:%S')
    return df


def categorize_danceability(df):
    """
    This function categorizes the danceability of songs into different levels.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with a new column 'danceability_category' indicating the danceability category of each song.
    """
    percentiles = [0, 0.25, 0.5, 0.75, 1.0]
    labels = ['Very Low', 'Low', 'Medium', 'High']

    df['danceability_category'] = pd.cut(df['danceability'], bins=percentiles, labels=labels, right=False)
    return df


def categorize_speechiness(df):
    """
    This function categorizes the speechiness of audio tracks into different categories.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with a new column 'speechiness_category' indicating the speechiness category of each audio track.
    """
    speechiness_bins = [0, 0.33, 0.66, 1.0]
    speechiness_labels = ['Music Only', 'Music and Speech', 'Speech Only']

    df['speechiness_category'] = pd.cut(df['speechiness'], bins=speechiness_bins, labels=speechiness_labels, right=False)
    return df


def assign_valence_categories(df):
    """
    This function assigns valence categories to each row in a DataFrame based on the 'valence' column.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with a new column 'valence_category' indicating the valence category of each track.
    """
    valence_bins = [0, 0.25, 0.5, 0.75, 1.0]
    valence_labels = ['Sad', 'Neutral', 'Happy', 'Euphoric']

    df['valence_category'] = pd.cut(df['valence'], bins=valence_bins, labels=valence_labels, right=False)
    return df


def assign_genre_categories(df):
    """
    This function assigns genre categories to each row in a DataFrame based on the 'track_genre' column.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with a new column 'genre' indicating the genre category of each track.
    """
    genre_mapping = {
        'instrumental': ['acoustic', 'classical', 'folk', 'guitar', 'piano', 'singer-songwriter', 'songwriter', 'world-music', 'opera', 'new-age'],
        'electronic': ['afrobeat', 'breakbeat', 'chicago-house', 'club', 'dance', 'deep-house', 'detroit-techno', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'house', 'idm', 'techno', 'minimal-techno', 'trance', 'hardstyle'],
        'rock and metal': ['alt-rock', 'alternative', 'british', 'grunge', 'hard-rock', 'indie', 'metal', 'metalcore', 'punk-rock', 'rock', 'rock-n-roll', 'black-metal', 'death-metal', 'hardcore', 'heavy-metal', 'industrial', 'psych-rock', 'rockabilly', 'goth', 'punk', 'j-rock', 'garage'],
        'pop': ['anime', 'cantopop', 'j-pop', 'k-pop', 'pop', 'power-pop', 'synth-pop', 'indie-pop', 'pop-film'],
        'urban': ['hip-hop', 'j-dance', 'j-idol', 'r-n-b', 'trip-hop'],
        'latino': ['brazil', 'latin', 'latino', 'reggaeton', 'salsa', 'samba', 'spanish', 'pagode', 'sertanejo', 'mpb'],
        'global sounds': ['indian', 'iranian', 'malay', 'mandopop', 'reggae', 'turkish', 'ska', 'dancehall', 'tango'],
        'jazz and soul': ['blues', 'bluegrass', 'funk', 'gospel', 'jazz', 'soul'],
        'varied themes': ['children', 'disney', 'forro', 'grindcore', 'kids', 'party', 'romance', 'show-tunes'],
        'mood': ['ambient', 'chill', 'happy', 'sad', 'sleep', 'study',  'comedy'],
        'single genre': ['country', 'progressive-house', 'swedish', 'emo', 'honky-tonk', 'french', 'german', 'drum-and-bass', 'groove', 'disco']
    }

    genre_to_category = {genre: category for category, genres in genre_mapping.items() for genre in genres}

    df['genre'] = df['track_genre'].map(genre_to_category)
    return df


def drop_columns_unnecessary(df):
    """
    This function drops unnecessary columns from a DataFrame.

    Parameters:
    - df: Pandas DataFrame.

    Returns:
    - df: Pandas DataFrame with unnecessary columns removed.
    """
    df = df.drop(['duration_ms', 'danceability', 'energy', 'key', 'mode', 'loudness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature'], axis=1)
    return df


def fill_null_values(df , columns, word) -> None:
    """
    This function fills null values in specified columns of a DataFrame with a given word.

    Parameters:
    - df: Pandas DataFrame.
    - columns: List of column names in which null values will be filled.
    - word: Word to fill null values with.

    Returns:
    - None
    """
    df[columns] = df[columns].fillna(word)
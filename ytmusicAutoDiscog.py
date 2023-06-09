import json
import os
from datetime import datetime
from ytmusicapi import YTMusic

# Initialize the YTMusic API object with your authentication headers
ytmusic = YTMusic('headers_auth.json')

# Function to get a list of followed artists by browsing the library
def get_followed_artists():
    artist_subs = []  # Initialize an empty list to store artist subscription objects
    continuation_token = None  # Initialize the continuation token for pagination
    while True:
        # Fetch the list of subscribed artists with a limit of 50 results per call
        artists = ytmusic.get_library_artists(limit=50, continuation_token=continuation_token)
        if not artists:  # If no more artists are returned, break the loop
            break
        artist_subs.extend(artists)  # Add the fetched artists to the list
        continuation_token = artists[-1]['browseId']  # Update the continuation token for the next call
    return [artist['browseId'] for artist in artist_subs]  # Return the list of artist browseIds

# Function to get all types of releases for an artist
def get_artist_releases(browse_id):
    artist_page = ytmusic.get_artist(browse_id)  # Fetch the artist's details and release sections
    # Get the list of albums if available, otherwise use an empty list
    albums = artist_page['albums']['results'] if 'albums' in artist_page else []
    # Get the list of singles if available, otherwise use an empty list
    singles = artist_page['singles']['results'] if 'singles' in artist_page else []
    # Get the list of EPs if available, otherwise use an empty list
    eps = artist_page['eps']['results'] if 'eps' in artist_page else []

    # Combine all types of releases (albums, singles, and EPs) into one list
    releases = albums + singles + eps

    # Get the list of features and featured on by checking the artist's songs section, if available
    features = artist_page['songs']['results'] if 'songs' in artist_page else []

    return releases + features  # Return the combined list of all releases and features

# Function to create a playlist for a specific artist
def create_playlist_for_artist(artist):
    name = f"{artist['name']} Discography"  # Generate the playlist name using the artist's name
    # Create the playlist with the given name and description
    playlist_id = ytmusic.create_playlist(name, description=f"Discography for {artist['name']}")
    return playlist_id  # Return the created playlist's ID

# Function to add releases to a playlist in the order of their release date
def add_releases_to_playlist(playlist_id, releases):
    # Sort releases by year and release date
    for release in sorted(releases, key=lambda a: (a['year'], datetime.strptime(a['release'], "%Y-%m-%d"))):
        release_id = release['browseId']  # Get the release's browseId
        tracks = ytmusic.get_album(release_id)['tracks']  # Fetch the list of tracks in the release
        track_ids = [track['videoId'] for track in tracks]  # Extract the videoId for each track
        ytmusic.add_playlist_items(playlist_id, track_ids)  # Add the tracks to the playlist

# Main execution
if __name__ == "__main__":
    # Get the list of followed artist browseIds
    followed_artist_ids = get_followed_artists()

    # Iterate through each followed artist
    for artist_id in followed_artist_ids:
        # Fetch the artist's details
        artist = ytmusic.get_artist(artist_id)
        # Print a message indicating the artist being processed
        print(f"Creating playlist for {artist['name']}...")

        # Get the list of all releases (albums, singles, EPs, features, etc.) for the artist
        releases = get_artist_releases(artist_id)
        # Create a playlist for the artist's discography
        playlist_id = create_playlist_for_artist(artist)

        # Add the artist's releases to the created playlist
        add_releases_to_playlist(playlist_id, releases)

        # Print a message indicating the playlist has been created
        print(f"Playlist created for {artist['name']}!")

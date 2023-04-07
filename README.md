# YouTubeMusicSelfUpdatingDiscographyPlaylist
YouTube Music Self Updating Discography Playlist

chatGPT prompts/program description:

"write a program that uses the ytmusic api to do the following:

get a list of all the artists a user follows
go through that list one by one and for each artist create a playlist, called "<artist's name> + < Discography>", that includes every release by that artist, in order of release date. in the case of two releases by the same artist having come out the same year, order the releases in the playlist chronologically by the date they were released on youtube music.
...
write the code but make sure to include all types of releases for the artist. anything their name is attached to in the youtube music collection. this includes albums, eps, singles, features, featured on, etc., look through the documentation at https://ytmusicapi.readthedocs.io/en/stable/* to check for the best way to include all different kinds of releases. make sure to add a comment for every line added explaining clearly what that line is doing

--------------------------------------------------------------------------------------------------

INSTRUCTIONS

To create a program that does this using the YTMusic API, you'll first need to install the ytmusicapi Python library, which you can do with the following command:

pip install ytmusicapi

Next, you'll need to authenticate with the YTMusic API. You can follow the steps in the documentation to set up the headers_auth.json file: https://ytmusicapi.readthedocs.io/en/latest/setup.html

Once you've set up the authentication, you can use the Python script to create playlists for each artist:

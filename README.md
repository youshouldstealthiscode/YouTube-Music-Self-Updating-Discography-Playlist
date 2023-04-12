# YouTubeMusicSelfUpdatingDiscographyPlaylist
YouTube Music Self Updating Discography Playlist

chatGPT prompts/program description:

"write a program that uses the ytmusic api to do the following:

get a list of all the artists a user follows
go through that list one by one and for each artist create a playlist, called "<artist's name> + < Discography>", that includes every release by that artist, in order of release date. in the case of two releases by the same artist having come out the same year, order the releases in the playlist chronologically by the date they were released on youtube music.
...
write the code but make sure to include all types of releases for the artist. anything their name is attached to in the youtube music collection. this includes albums, eps, singles, features, featured on, etc., look through the documentation at https://ytmusicapi.readthedocs.io/en/stable/* to check for the best way to include all different kinds of releases. make sure to add a comment for every line added explaining clearly what that line is doing
...
give me step by step instructions on how to set up the headers_auth.json file based on the information found at https://ytmusicapi.readthedocs.io/en/latest/setup.html

--------------------------------------------------------------------------------------------------

INSTRUCTIONS

To create a program that does this using the YTMusic API, you'll first need to install the ytmusicapi Python library, which you can do with the following command:

pip install ytmusicapi

Next, you'll need to authenticate with the YTMusic API. You can follow the steps in the documentation to set up the headers_auth.json file: https://ytmusicapi.readthedocs.io/en/latest/setup.html

Once you've set up the authentication, you can use the Python script to create playlists for each artist:

----

Here are the step-by-step instructions to set up the headers_auth.json file for the YTMusic API based on the information found at the provided link:

Open a new browser window in Incognito/Private mode.

For Chrome: Press Ctrl+Shift+N (Windows/Linux) or Cmd+Shift+N (Mac)
For Firefox: Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (Mac)
For Safari: Press Cmd+Shift+N
Navigate to https://music.youtube.com/ in the Incognito/Private browser window.

Log in to your Google account associated with your YouTube Music subscription.

Open the browser's Developer Tools.

For Chrome: Press Ctrl+Shift+I (Windows/Linux) or Cmd+Option+I (Mac)
For Firefox: Press Ctrl+Shift+I (Windows/Linux) or Cmd+Option+I (Mac)
For Safari: Press Cmd+Option+I
In the Developer Tools window, click the "Network" tab.

Refresh the YouTube Music page by pressing F5 (Windows/Linux) or Cmd+R (Mac).

In the Developer Tools' "Network" tab, find a request with a name like "browse?alt=..." or "guide?alt=...". You can filter the requests using the search bar, entering "browse?alt=" or "guide?alt=".

Click on the identified request, and then click on the "Headers" tab on the right side.

In the "Headers" tab, scroll down to the "Request Headers" section.

Locate the following headers: "cookie", "x-goog-authuser", and "x-goog-visitor-id". If "x-goog-authuser" is missing, it is likely that you are not using a Google Account with a YouTube Premium subscription.

Copy the values of these headers and create a new JSON file named headers_auth.json on your local machine. The JSON file should have the following format:

{
    "cookie": "YOUR_COOKIE_VALUE",
    "x-goog-authuser": "YOUR_X_GOOG_AUTHUSER_VALUE",
    "x-goog-visitor-id": "YOUR_X_GOOG_VISITOR_ID_VALUE"
}
Replace YOUR_COOKIE_VALUE, YOUR_X_GOOG_AUTHUSER_VALUE, and YOUR_X_GOOG_VISITOR_ID_VALUE with the corresponding values you copied from the Developer Tools.

I have added such a file with that exact code to the repo so you just have to find your necessary variables and insert them accordingly.

!!!Keep in mind that the "cookie" value may expire, so you might need to repeat this process in the future to obtain a new "cookie" value.!!


added these words as a test for my git control
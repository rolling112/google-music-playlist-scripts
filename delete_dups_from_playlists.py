#!/usr/bin/env python
from gmusicapi import Mobileclient
import sys


def find_and_remove_dups(api, tracks):
    track_set = set()
    for track in tracks:
        trackId = track['trackId']
        entryId = track['id']
        if trackId in track_set:
            print "    found duplicate with trackId: " + trackId + ", deleting"
            api.remove_entries_from_playlist(entryId)
        else:
            track_set.add(trackId)
            

if len(sys.argv) != 1:
    print "USAGE:"
    print "./delete_dups_from_playlists.py"
    print
    print "     Will delete all duplicate songs within each playlist" 
    exit(0)

api = Mobileclient()
# A valid android_id can be pulled from an mobile device authenticated
# on the google account used for this script
# It can be retrieved using the Device ID app and can sometimes be found
# under About Phone in Settings
logged_in = api.login('username', 'password', 'android_id')

if logged_in:
    print "Successfully logged in. Finding duplicates in playlists"
    playlists = api.get_all_user_playlist_contents()

    for playlist in playlists:
        print "Deleting duplicates from " + playlist['name'] + "..."
        tracks = playlist['tracks']
        find_and_remove_dups(api, tracks)
else:
    print "Login failed"
        
raw_input()


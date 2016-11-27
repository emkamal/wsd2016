import json

class Song:
    artist = "file"
    title = "not found"
    timestamp = "-1"
    track_id = "given_id" # should be whatever track_id was given
    tags = []
    similars = []

    def __init__(self, track_id):
        self.track_id = track_id

        # extract locations from track_id
        folders = list(track_id[2:5])

        # load file based on the location and read all the info to be populated
        file_location = "lastfm_subset/" + "/".join(folders) + "/" + track_id + ".json"

        with open(file_location) as json_data:
            data = json.load(json_data)
            self.artist = data['artist']
            self.title = data['title']
            self.timestamp = data['timestamp']
            self.tags = data['tags']
            self.similars = data['similars']

    def get_tags(self, limit=0):
        tags_name = []

        for tag in self.tags:
            if limit == 0:
                tags_name.append(tag[0])
            else:
                if(int(tag[1]) >= limit):
                    tags_name.append(tag[0])

        return tags_name

    def get_similars(self, limit=0):
        similars_id = []

        for similar in self.similars:
            if limit == 0:
                similars_id.append(similar[0])
            else:
                if(int(similar[1]) >= limit):
                    similars_id.append(similar[0])

        return similars_id

    def shared_tags(self, other_song_instance):
        shared_tags = []
        
        for tag in self.tags:
            for other_tag in other_song_instance.tags:
                if tag[0] == other_tag[0]:
                    shared_tags.append(tag[0])

        return shared_tags

    def combined_tags(self, other_song_instance):
        pass

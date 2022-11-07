
class Video:
    
    """Video class contains all the information about a video.
    
    Attributes:
    
        title (str): The title of the video.
    
        video_id (str): The video's unique id.
    
        tags (str): The video's tags.
    
    """
        
    def __init__(self, title, video_id, tags):
        self.title = title
        self.video_id = video_id
        self.tags = tags

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_video_id(self):
        return self.video_id

    def get_tags(self):
        return self.tags

    def set_title(self, title):
        self.title = title

    def set_video_id(self, video_id):
        self.video_id = video_id

    def set_tags(self, tags):
        self.tags = tags


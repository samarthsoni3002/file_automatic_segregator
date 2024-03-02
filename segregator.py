import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from urllib.parse import urlparse

downloads_path = r"/home/dheeraj/Downloads"
destination_base_path = r"/home/dheeraj/Downloads/Organized"
other_folder = "Other"

class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        if not file_path.endswith('.part'):  # Skip incomplete downloads
            try:
                self.organize_file(file_path)
            except Exception as e:
                print(f"Error organizing file {file_path}: {e}")

    def extract_source_from_url(self, url):
        # Extract source information from the URL
        source_keywords = {
            'whatsapp': 'WhatsApp',
            'instagram': 'Instagram',
            'facebook': 'Facebook',
            'twitter': 'Twitter',
            'linkedin': 'LinkedIn',
            'pinterest': 'Pinterest',
            'snapchat': 'Snapchat',
            'telegram': 'Telegram',
            'slack': 'Slack',
            'gmail': 'Gmail',
            'outlook': 'Outlook',
            'yahoo': 'Yahoo',
            'google_drive': 'Google Drive',
            'dropbox': 'Dropbox',
            'github': 'GitHub',
            'medium': 'Medium',
            'reddit': 'Reddit',
            'tumblr': 'Tumblr',
            'spotify': 'Spotify',
            'apple_music': 'Apple Music',
            'netflix': 'Netflix',
            'amazon_prime': 'Amazon Prime',
            'microsoft_teams': 'Microsoft Teams',
            'zoom': 'Zoom',
            'skype': 'Skype',
            'trello': 'Trello',
            'evernote': 'Evernote',
            'wordpress': 'WordPress',
            'behance': 'Behance',
            'dribbble': 'Dribbble',
        }

        for keyword, source in source_keywords.items():
            if keyword in url.lower():
                return source

        return 'Unknown'

    def extract_source_from_filename(self, filename):
        # Extract source information from the filename
        source_keywords = {
               'whatsapp': 'WhatsApp',
            'instagram': 'Instagram',
            'facebook': 'Facebook',
            'twitter': 'Twitter',
            'linkedin': 'LinkedIn',
            'pinterest': 'Pinterest',
            'snapchat': 'Snapchat',
            'telegram': 'Telegram',
            'slack': 'Slack',
            'gmail': 'Gmail',
            'outlook': 'Outlook',
            'yahoo': 'Yahoo',
            'google_drive': 'Google Drive',
            'dropbox': 'Dropbox',
            'github': 'GitHub',
            'medium': 'Medium',
            'reddit': 'Reddit',
            'tumblr': 'Tumblr',
            'spotify': 'Spotify',
            'apple_music': 'Apple Music',
            'netflix': 'Netflix',
            'amazon_prime': 'Amazon Prime',
            'microsoft_teams': 'Microsoft Teams',
            'zoom': 'Zoom',
            'skype': 'Skype',
            'trello': 'Trello',
            'evernote': 'Evernote',
            'wordpress': 'WordPress',
            'behance': 'Behance',
            'dribbble': 'Dribbble',
            'pdf': 'Documents',
            'jpeg': 'Images',
            'png': 'Images',
            'gif': 'Images',
            'mp3': 'Audio',
            'wav': 'Audio',
            'mp4': 'Videos',
            'mkv': 'Videos',
            'avi': 'Videos',
            'mov': 'Videos',
            'txt': 'Documents',
            'doc': 'Documents',
            'docx': 'Documents',
            'xls': 'Documents',
            'xlsx': 'Documents',
            'ppt': 'Documents',
            'pptx': 'Documents',
        }

        for keyword, source in source_keywords.items():
            if keyword in filename.lower():
                return source

        return 'Unknown'

    def get_extension(self, file_path):
        _, extension = os.path.splitext(file_path)
        return extension[1:].lower()  # Remove the leading dot

    def organize_file(self, file_path):
        url = urlparse(file_path).scheme
        source = self.extract_source_from_url(url)

        if source == 'Unknown':
            # If source is not detected from URL, try to extract from filename
            filename = os.path.basename(file_path)
            source = self.extract_source_from_filename(filename)

        if source == 'Unknown':
            source = other_folder

        source_folder = os.path.join(destination_base_path, source)
        if not os.path.exists(source_folder):
            os.makedirs(source_folder)

        extension = self.get_extension(file_path)
        extension_folder = os.path.join(source_folder, extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)

        filename = os.path.basename(file_path)
        destination_path = os.path.join(extension_folder, filename)
        shutil.move(file_path, destination_path)
        print(f"Moved: {file_path} to {destination_path}")

def watch_downloads():
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=downloads_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    watch_downloads()

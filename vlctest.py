import vlc
import time

class VLCPlayer1:
    def _init_(self, media_path):
        self.media_path=media_path
        self.instance = vlc.Instance('--no-xlib')  # Prevents crashes on Unix systems
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(self.media_path)
        self.player.set_media(self.media)

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.set_pause(0)

    def stop(self):
        self.player.stop()
        self.player.release()



# Example usage:
if __name__ == "__main__":
    video_path = "test.mp4"
    player = VLCPlayer1()
    player.play()
    time.sleep(5)  # Play for 5 seconds
    player.pause()
    time.sleep(2)  # Pause for 2 seconds
    player.resume()
    time.sleep(2)  # Resume for 2 seconds
    player.stop()  
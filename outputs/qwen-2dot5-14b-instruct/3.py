
def play_random_song_for_five_seconds():
    audio_files = find_all_audio_files()
    if not audio_files:
        print("No audio files found.")
        return
    random_file = audio_files[generate_random_number(0, len(audio_files))]
    play_audio_file(random_file)
    sleep(5)
    stop_audio_player()

play_random_song_for_five_seconds()

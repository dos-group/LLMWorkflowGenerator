
def play_random_song_for_5_seconds():
    audio_files = find_all_audio_files()
    if not audio_files:
        print("No audio files found.")
        return
    random_index = generate_random_number(0, len(audio_files))
    random_song = audio_files[random_index]
    play_audio_file(random_song)
    sleep(5)
    stop_audio_player()

play_random_song_for_5_seconds()

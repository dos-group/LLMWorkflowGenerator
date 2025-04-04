
def play_random_song_for_5_seconds():
    # Find all audio files
    audio_files = find_all_audio_files()
    
    # Check if there are any audio files
    if not audio_files:
        print("No audio files found.")
        return
    
    # Generate a random index to select a random song
    random_index = generate_random_number(0, len(audio_files))
    
    # Get the random song file path
    random_song = audio_files[random_index]
    
    # Play the random song
    play_audio_file(random_song)
    
    # Sleep for 5 seconds while the song plays
    sleep(5)
    
    # Stop the audio player after 5 seconds
    stop_audio_player()

# Execute the function
play_random_song_for_5_seconds()

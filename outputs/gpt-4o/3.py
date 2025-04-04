
def play_random_song_for_5_seconds():
    # Find all audio files
    audio_files = find_all_audio_files()
    
    # Check if there are any audio files
    if not audio_files:
        print("No audio files found.")
        return
    
    # Generate a random index to select a random audio file
    random_index = generate_random_number(0, len(audio_files))
    random_song = audio_files[random_index]
    
    # Play the selected random audio file
    play_audio_file(random_song)
    
    # Sleep for 5 seconds
    sleep(5)
    
    # Stop the audio player
    stop_audio_player()

# Call the function
play_random_song_for_5_seconds()


def play_random_song_for_five_seconds():
    # Find all audio files
    audio_files = find_all_audio_files()
    
    # Generate a random index to select a random audio file
    random_index = generate_random_number(0, len(audio_files))
    
    # Get the file path of the randomly selected audio file
    random_audio_file = audio_files[random_index]
    
    # Play the selected audio file
    play_audio_file(random_audio_file)
    
    # Sleep for 5 seconds
    sleep(5)
    
    # Stop the audio player
    stop_audio_player()

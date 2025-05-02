
def play_random_song():
    # Find all audio files
    audio_files = find_all_audio_files()
    
    # Generate a random index within the range of audio files
    random_index = generate_random_number(0, len(audio_files))
    
    # Get the file path of the randomly selected audio file
    random_song_path = audio_files[random_index]
    
    # Play the randomly selected audio file
    play_audio_file(random_song_path)
    
    # Sleep for 5 seconds
    sleep(5)
    
    # Stop the audio player
    stop_audio_player()

# Call the function
play_random_song()

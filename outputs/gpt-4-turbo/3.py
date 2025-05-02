
def play_random_song_for_5_seconds():
    # Find all audio files
    audio_files = find_all_audio_files()
    
    if not audio_files:
        print("No audio files found.")
        return
    
    # Generate a random index to select a song
    random_index = generate_random_number(0, len(audio_files))
    
    # Get the file path of the randomly selected song
    file_path = audio_files[random_index]
    
    # Play the selected audio file
    play_audio_file(file_path)
    
    # Sleep for 5 seconds while the song plays
    sleep(5)
    
    # Stop the audio player after 5 seconds
    stop_audio_player()

# Call the function to play a random song for 5 seconds
play_random_song_for_5_seconds()

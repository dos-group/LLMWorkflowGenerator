# Step 1: Find the file ID for the song "Beat It" by Michael Jackson
file_id = find_file_id("Beat It Michael Jackson")

# Step 2: Check if the file ID was found
if file_id is not None:
    # Step 3: Play the audio file using the found file ID
    play_audio_file(file_id)
else:
    # Step 4: If not found, ask a question or handle the error
    print_screen("Sorry, I couldn't find the song 'Beat It' by Michael Jackson.")

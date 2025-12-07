import random

def load_playlist(filename="playlist.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

def save_playlist(playlist, filename="playlist.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for song in playlist:
            f.write(song + "\n")
    print("💾 Playlist saved.\n")

def show_playlist(playlist):
    if not playlist:
        print("🎧 Playlist is empty.")
    else:
        print("\n🎧 Your Playlist:")
        for i, song in enumerate(playlist, start=1):
            print(f"{i}. {song}")
    print()


playlist = load_playlist()  
if not playlist:  
    playlist = ["born to die", "star shopping", "nuts", "freak", "high by the beach"]

while True:
    print("\n🎶 --- Playlist Manager --- 🎶")
    print("1. View playlist")
    print("2. Add a song")
    print("3. Remove a song")
    print("4. Shuffle playlist")
    print("5. Search songs")
    print("6. Save playlist")
    print("7. Exit")
    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        show_playlist(playlist)

    elif choice == "2":
        new_song = input("🎵 Enter the song to add: ").strip()
        if new_song:
            playlist.append(new_song)
            print(f"✅ '{new_song}' added.")
            save_playlist(playlist)   
        else:
            print("⚠️ No song entered.")

    elif choice == "3":
        show_playlist(playlist)
        remove_song = input("❌ Enter the song name to remove: ").strip()
        if remove_song in playlist:
            playlist.remove(remove_song)
            print(f"✅ '{remove_song}' removed.")
            save_playlist(playlist)
        else:
            print(f"⚠️ '{remove_song}' not found.")

    elif choice == "4":
        random.shuffle(playlist)
        print("🔀 Playlist shuffled!")
        show_playlist(playlist)
        save_playlist(playlist)

    elif choice == "5":
        query = input("🔎 Search (type part of the title): ").strip().lower()
        matches = [(i, s) for i, s in enumerate(playlist, start=1) if query in s.lower()]
        if matches:
            print("Found:")
            for i, s in matches:
                print(f"{i}. {s}")
        else:
            print("No matches found.")

    elif choice == "6":
        save_playlist(playlist)

    elif choice == "7":
        save_playlist(playlist)
        print("👋 Exiting. Bye!")
        break

    else:
        print("⚠️ Invalid option. Choose 1-7.")

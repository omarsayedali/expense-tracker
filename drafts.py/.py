songs = []

while True:
    song = input("Enter a song (type 'done' to save, 'stop' to exit): ")

    if song.lower() == "stop":
        print("Goodbye...")
        break

    elif song.lower() == "done":
        with open("todo.txt", "a") as file:
            file.write("🎵 Songs you saved:\n")
            for i, s in enumerate(songs, start=1):
                file.write(f"{i}. {s}\n")
            file.write("-" * 40 + "\n")

        print("\n✅ Songs saved successfully to todo.txt!")
        with open("todo.txt", "r") as file:
            content = file.read()
            print("\n📄 File content so far:\n")
            print(content)
        break  # exit after saving

    else:
        songs.append(song)
        print("\nYour current list:")
        for i, s in enumerate(songs, start=1):
            print(f"{i}. {s}")

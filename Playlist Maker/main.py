import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "youtube_videos.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL,
                link TEXT NOT NULL
    )
"""
)


def update_video_ids():
    cursor.execute("SELECT id FROM videos ORDER BY id")
    rows = cursor.fetchall()
    for index, row in enumerate(rows, start=1):
        cursor.execute("UPDATE videos SET id = ? WHERE id = ?", (index, row[0]))
    conn.commit()


def list_videos():
    print("\n" + "*" * 70)
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    print("\n" + "*" * 70)


def add_video():
    name = input("Enter video name: ")
    time = input("Enter duration: ")
    link = input("Enter link: ")
    cursor.execute(
        "INSERT INTO videos (name, time, link) VALUES (?, ?, ?)", (name, time, link)
    )
    conn.commit()
    print("Video added!")


def update_video():
    video_id = input("Enter video id to be updated: ")
    new_name = input("Enter new name: ")
    new_time = input("Enter new duration: ")
    new_link = input("Enter new video link: ")
    cursor.execute(
        "UPDATE videos SET name = ?, time = ?, link = ? WHERE id = ?",
        (new_name, new_time, video_id, new_link),
    )
    conn.commit()
    print("Video updated!")


def delete_video():
    video_id = input("Enter video id to be deleted: ")
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print("Video deleted!")
    update_video_ids()


def main():
    while True:
        print("\nYouTube manager app with SQLITE3")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                add_video()
                while True:
                    repeat = input("Do you want to add another video(y/n): ")
                    if repeat.lower() == "y":
                        add_video()
                    elif repeat.lower() == "n":
                        break
                    else:
                        print("Invalid choice!")
            case "3":
                list_videos()
                update_video()
                while True:
                    repeat = input("Do you want to update another video(y/n): ")
                    if repeat.lower() == "y":
                        update_video()
                    elif repeat.lower() == "n":
                        break
                    else:
                        print("Invalid choice!")
            case "4":
                list_videos()
                delete_video()
            case "5":
                print("Thank you, have a great day!")
                break
            case _:
                print("Invalid choice!!")

    conn.close()


if __name__ == "__main__":
    main()

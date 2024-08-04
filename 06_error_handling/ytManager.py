import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print("\n")
        print("*" * 70)
        print(f"{index}. {video['name']}, Duration: {video['time']}")

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print('Invalid index selected')

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print('Invalid index')

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager  |  Choose an Option")
        print("1. List your favorite videos")
        print("2. Add a YouTube video")
        print("3. Update YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos(videos)
        elif choice == '2':
            add_videos(videos)
        elif choice == '3':
            update_videos(videos)
        elif choice == '4':
            delete_videos(videos)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

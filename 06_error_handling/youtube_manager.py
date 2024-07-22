import json

def load_data(videos):
    try:
        with open ('youtube.txt','r') as file:
            json.load(file)
    except:
        pass

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update(videos):
    pass

def delete(videos):
    pass

def exit_app(videos):
    pass

def main():
    videos=load_data()

    while True:
        print('/n Youtube Manager')
        print('1. List your Favourite video ')
        print('2. Add a Youtube video ')
        print('3. Update details ')
        print('4. Delate ')
        print('5. Exit App ')
        choice= input("Enter Your Choice")

        #we can use if statement also (if (choice===1):)

        match choice :    #match is better option for checking multiple options
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update(videos)
            case '4':
                delete(videos)
            case '5':
                break
            case _:
                print('Invalid Choice')

if __name__== "__main()__":
    main()

'[{},{}]'
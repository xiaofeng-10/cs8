from song_functions import *

the_menu = {"L" : "List",
            "A" : "Add",
            "E" : "Edit",
            "D" : "Delete",
            "M" : "Show statistical data on",
            "S" : "Save the data to file",
            "R" : "Restore data from file",
            "Q" : "Quit this program"}# TODO 1: add the options from the instructions
opt = None
sub_menu = {"X" :"Delete all songs at once"}

all_songs = {
   "12332": {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
   },
   "14567": {
      "title": "Soul Meets Body",
      "artist": "Death Cab for Cutie",
      "length": "",
      "album": "Plans",
      "genre": ["indie pop", "indie rock"],
      "rating": 5,
      "released": "07/16/2005",
      "favorite": True,
      "uid": 14567
   },
   "78210": {
      "title": "Fake Love",
      "artist": "BTS",
      "length": "04:02",
      "album": "",
      "genre": ["hip hop", "electro pop", "Korean pop"],
      "rating": 3,
      "released": "05/18/2018",
      "favorite": False,
      "uid": 78210
   },
   "99105": {
      "title": "Foil",
      "artist": "'Weird Al' Yankovic",
      "length": "02:22",
      "album": "Mandatory Fun",
      "genre": ["pop", "parody"],
      "rating": 5,
      "released": "07/15/2014",
      "favorite": True,
      "uid": 99105
   }
}
    
list_menu = {
    "A": "all songs - full",
    "B": "all songs - titles only",
    "F": "favorite songs",
    "G": "songs of a specific genre"
}

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}

key_list = []
for key in all_songs.keys():
    key_list.append(key)

while True:
    print_main_menu(the_menu) # TODO 2: define the function, uncomment, and call with the menu as an argument
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters

    if opt not in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == "q" or opt == "Q": # TODO 4: quit the program
        print("Goodbye!\n")
        break # exit the main `while` loop

    elif opt == 'L':
        if all_songs == {}:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue

        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_songs(all_songs, rating_map, showid = True)
        elif subopt == 'B':
            print_songs(all_songs, rating_map, title_only = True)
        elif subopt == 'F':
            print_songs(all_songs, rating_map, fave = True)
        elif subopt == 'G':
            print_songs(all_songs, rating_map, get_genre = True)

    elif opt == 'D':
        continue_action = 'y'
        while continue_action == 'y':            
            print_songs(all_songs, rating_map, title_only = True, showid = True)
            print("Which song would you like to delete?")
            print("X - Delete all songs at once")
            print("::: OR Enter the number corresponding to the song ID")
            print("::: OR press 'M' to cancel and return to the main menu.")
            user_opt = input(">")
            if user_opt == 'X':
                print("::: WARNING! Are you sure you want to delete ALL songs?")
                print("::: Type Yes to continue the deletion.")
                confirmation = input("> ")
                if confirmation == "Yes":
                    print("Deleted all songs.")
                    all_songs.clear()
                    break
            elif len(user_opt) == 5:
                if user_opt not in all_songs:
                    print(f"WARNING: |{user_opt}| is an invalid song ID!")
                    print("::: Would you like to delete another song? Enter 'y' to continue.")
                    if user_opt == "y":
                        continue
                    elif user_opt =="n" or user_opt == "N":
                        break
                elif user_opt in all_songs:
                    print("Success!")
                    print(f"Deleted the song |{all_songs[user_opt]['title']}|")
                    all_songs.pop(user_opt)
                    print("::: Would you like to delete another song? Enter 'y' to continue.")
                    user_opt = input(">")
                    if user_opt == "n" or user_opt == "N":
                        break
                    elif user_opt == "y":
                        continue
            elif user_opt == 'M':
                break

    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            song_info = []
            print("::: Enter each required field:")
            # TODO: Get user inputs for all 9 song info fields (i.e. keys). 
            # Get *all* inputs as strings.
            key_list={
                input("Title: "),
                input("Artist: "), 
                input("Length (00:00 format): "),
                input("Album: "),
                input("Genre (separate them with commas): "),
                input("Rating (1-5): ") ,
                input("Release Date (MM/DD/YYYY format):"),
                input("Favorite (T/F): "), 
                input("Unique ID: ")
                }
            result = get_new_song(song_info, rating_map, key_list) # TODO: attempt to create a new song
            if type(result) == dict:
                all_songs.update(result) # TODO: add a new song to the list of songs
                print(f"Successfully added a new song!")
                print_song(result, rating_map, title_only = False, showid=False)
            elif type(result) == tuple:
                print(f"WARNING: invalid data!")
                print(f"Error: {result[0]}")

            print("::: Would you like to add another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower() 
            # ----------------------------------------------------------------

    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            result = save_to_csv(all_songs, filename) # TODO: Call the function with appropriate inputs and capture the output
            if result == -1: # TODO
                print(f"WARNING: |{filename}| is an invalid file name!") # TODO
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the songs to |{filename}|")
                continue_action = 'y'
    #--------------------------------------------------------------------------

    elif opt == 'R':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            user_opt = input("> ")
            if user_opt == "n" or user_opt == "N":
                break
            result = load_from_csv(user_opt, all_songs, rating_map, key_list)
            if result == -1:
                print(f"WARNING: invalid input - must end with '.csv'")
                continue_action= input("::: Would you like to try again? Enter 'y' to try again.")
            elif result == None:
                print(f"WARNING: |{user_opt}| was not found!")
                continue_action= input("::: Would you like to try again? Enter 'y' to try again.")
            elif result != -1:
                print(f"WARNING: |{user_opt}| contains invalid data!")
                print("The following rows from the file were not loaded:")
                print(result)
            elif result == []:
                print(f'Successfully restored all songs from |{user_opt}.csv|')
                continue_action= input("::: Would you like to try again? Enter 'y' to try again.")

    elif opt == 'E':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}: 
                print("WARNING: There is nothing to edit!")
                break
            print("::: Song list:")
            print_songs(all_songs, rating_map, title_only = True, showid = True)
            print("::: Enter the song ID you wish to edit.")
            user_option = input("> ")
            if songid in all_songs: # TODO - check to see if that ID is in the song dictionary
                subopt = get_selection("edit", all_songs[user_option], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") # TODO
                field_info = input("> ")
                result = edit_song(all_songs, user_option, rating_map, subopt, field_info, ...) #TODO
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")  # TODO
                    print_song(result, rating_map, title_only = False, showid=False)  # TODO
                else: # edit_song() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  # TODO
                    print(f"The song was not updated.")
            else: # song ID is incorrect/invalid
                print(f"WARNING: |{user_option}| is an invalid song ID!")  # TODO

            print("::: Would you like to edit another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      
            # ----------------------------------------------------------------

    elif opt == 'M':
        continue_action = 'y'
        while continue_action == 'y':
            sub_menu = {"A":"find the mean (average) of all song ratings values",
                        "B":"find the median of all song ratings values",
                        "C":"find the standard deviation of all song ratings values",
                        "D":"print out a histogram of all song ratings values"}
            print("::: What would you like to show statistical data on?")
            print("A - Mean value of all song ratings")
            print("B - Median value of all song ratings")
            print("C - Standard Deviation value of all song ratings")
            print("D - Histogram of all song ratings")
            print("::: Enter your selection")
            subopt = input("> ")
            if subopt =="A":
                print("You selected |A| to show statistical data on |mean value of all song ratings|.")
                do_stats(all_songs, A)
                print("::: Would you like to get different statistics? Enter 'y' to continue.")
                if user_opt == "y":
                    continue
                elif user_opt =="n" or user_opt == "N":
                    break
            elif subopt == "B":
                print("You selected |B| to show statistical data on |median value of all song ratings|.")
                do_stats(all_songs, B)
                print("::: Would you like to get different statistics? Enter 'y' to continue.")
                if user_opt == "y":
                    continue
                elif user_opt =="n" or user_opt == "N":
                    break
            elif subopt == "C":
                print("You selected |C| to show statistical data on |standard deviation value of all song ratings|.")
                do_stats(all_songs, C)
                print("::: Would you like to get different statistics? Enter 'y' to continue.")
                if user_opt == "y":
                    continue
                elif user_opt =="n" or user_opt == "N":
                    break
            elif subopt == "D":
                print("You selected |D| to show statistical data on |histogram of all song ratings|.")
                do_stats(all_songs, D)
                print("::: Would you like to get different statistics? Enter 'y' to continue.")
                if user_opt == "y":
                    continue
                elif user_opt =="n" or user_opt == "N":
                    break      
            
    # Pause before going back to the main menu
    input("::: Press Enter to continue")

print("Have a nice day!")

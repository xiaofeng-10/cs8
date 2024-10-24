def print_main_menu(the_menu):
    """
    print main menu
    """
    print(f"::: What would you like to list?")
    for letter,opt in the_menu.items():
        print(f'{letter} - {opt}')

######## LIST OPTION ########

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None

    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def get_written_date(date_list):
    """
    The function ...
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    # Finish the function
    for key,value in month_names.items():
        if int(date_list[0]) == key:
            month = value
            return f'{month} {int(date_list[1])}, {date_list[2]}'

def print_song(song, rating_map, title_only = False, showid=False):
    """
    param: song (dict) - a single song dictionary
    param: rating_map (dict) - a dictionary object that is expected
            to have the string keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed for the
            rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the name of the song is printed.
            Otherwise, displays the formatted song fields.
    param: showid (Boolean) - by default, set to False.
            If False, then the id number of the song is not displayed.
            Otherwise, displays the id number.

    returns: None; only prints the song values

    Helper functions:
    - get_written_date() to display the 'released' field
        You created a similar function in a previous lab.
    """
    # TO-DO: print some or all information of one song (dict),
    #              depending on the options in the parameters
    #    You have to ensure that you use f-strings with the following padding settings:
    #              pad your string labels with 9 spaces and justify right.
    #    To see what these should look like, see further below for example runs.

    sub_list = song['genre']
    sub_string = ', '.join(sub_list)
    genre_string = sub_string.title()
    rate = song['rating']
    rate = rating_map[str(song['rating'])]
    date = song['released'].split("/")
    
    if title_only == False and showid == True:
        print(f"{'ID:':>9} {song['uid']} |{'TITLE:':>9} {song['title']}")
        print(f"{'ARTIST:':>9} {song['artist']}")
        if song['length']=="":
            pass
        else:
            print(f"{'LENGTH:':>9} {song['length']}")
        if song['album']=="":
            pass
        else:
            print(f"{'ALBUM:':>9} {song['album']}")
        if song['genre'] == []:
            pass
        else:
            print(f"{'GENRE:':>9} {genre_string}")
        print(f"{'RATING:':>9} {rate}")
        if song['released'] =="":
            pass
        else:
            print(f"{'RELEASED:':>9} {get_written_date(date)}")
        print(f"{'FAVORITE:':>9} {song['favorite']}")
        print("*"*42)
    elif title_only == False and showid == False:
        print(f"{'TITLE:':>9} {song['title']}")
        print(f"{'ARTIST:':>9} {song['artist']}")
        if song['length']=="":
            pass
        else:
            print(f"{'LENGTH:':>9} {song['length']}")
        if song['album']=="":
            pass
        else:
            print(f"{'ALBUM:':>9} {song['album']}")
        if song['genre'] == []:
            pass
        else:
            print(f"{'GENRE:':>9} {genre_string}")
        print(f"{'RATING:':>9} {rate}")
        if song['released']=="":
            pass
        else:
            print(f"{'RELEASED:':>9} {get_written_date(date)}")
        print(f"{'FAVORITE:':>9} {song['favorite']}")
        print("*"*42)
    elif title_only == True and showid== False:
        print(f"{'TITLE:':>9} {song['title']}")
    elif title_only == True and showid == True:
        print(f"{'ID:':>9} {song['uid']} |{'TITLE:':>9} {song['title']}")
    

def print_songs(song_dict, rating_map, title_only = False, showid = False, fave = False, get_genre = False):
    """
    param: song_dict (dict) - a dictionary containing dictionaries with
            the song data
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the title of the song is printed.
            Otherwise, displays the formatted song fields.
    param: showid (Boolean) - by default, set to False.
            If False, then the key (unique ID number) of the song is not displayed.
            Otherwise, displays the id number.
    param: fave (Boolean) - by default, set to False, and prints all songs.
            Otherwise, if it is set to True, prints only the songs marked as favorite.
            This parameter is meant to be used exclusive of get_genre
            (i.e. if fave=True, then get_genre should be False, and vice versa).
    param: get_genre (Boolean) - by default, set to False, and prints all songs.
            If set to True, then the function should ask the user for a
            genre keyword (string) and print only those songs that contain that string in its genre value.
            This parameter is meant to be used exclusive of fave (i.e. if fave=True, then get_genre should be False, and vice versa).
            NOTE: If a song has multiple instances of that genre keyword, you should only print the song once.

    returns: None; only prints the song values from the song_list

    Helper functions:
    - print_song() to print individual songs
    """
    print("*"*42)
    
    # Check to see if get_genre is True, so that you can ask for the genre keyword
    if get_genre == True:
        print("Enter genre:: ")
    # Go through all the songs in the song dictionary:
    for song in song_dict:
        # if not asking for favorites or specific genres: print everything
        if fave == False and title_only == False:
            print_song(song_dict[song], rating_map, title_only = False, showid= False)

        elif title_only == True and showid == False:
            print_song(song_dict[song], rating_map, title_only = True, showid = False)

        elif title_only == True and showid == True:
            print_song(song_dict[song], rating_map, title_only = True, showid = True)
        
        # otherwise: if asking for favorites, print just those:
        elif fave == True and get_genre== False and showid == False:
            print_song(song_dict[song], rating_map, title_only = False, showid = False)
        
        # otherwise: if asking for a specific genre, print just those:
        elif get_genre:
            if fave == False and title_only == False and showid == False:
                genre_key = input("Enter genre:: ")
            # search all the songs' genres for the genre keyword
                for keys,values in song.items():
                    if keys == "genre":
                        if genre_key in values:
                            print_song(song_dict[song],rating_map, title_only = False, showid = False)
                        else:
                            continue
                    
            # and print only those songs where that keyword appears in the genre value
            # NOTE: You should only print a song *once* 
            # even if the genre keyword appears more than once in it
      

            
def delete_song(song_dict, songid):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: songid (str) - a string that is expected to
            contain the key to a song dictionary (i.e. same as its unique ID)

    The function first checks if the dictionary of songs is empty.
    The function then validates the song ID to verify
    that the provided ID key can access an element from song_dict
    On success, the function saves the item's "title" from song_dict
    and returns that string ("title" value)
    after the item is deleforted from song_dict.

    returns:
    If the input dict is empty, return 0.
    If the ID is not valid (i.e. not found in the song_dict), return -1.
    Otherwise, on success, the entire song is removed from song_dict
    and the function returns the title of the deleted song.
    """
    if len(song_dict) == 0:
        return 0
    elif songid not in song_dict:
        return -1
    else:
        delete = song_dict[songid]["title"]
        song_dict.pop(songid)
        return delete

def is_valid_addlist(new_song_list):
    """
    param: new_song_list is the list user entered
    The function check if the entire of list is made up of strings
    and the list length equal to 9
    """
    count = 0
    if len(new_song_list) == 9:
        for i in range(len(new_song_list)):
            if type(new_song_list[i]) == str:
                count = count+1
            if count == 9:
                return True
                break
        else:
            return False
    else:
        return False

def is_valid_title(name_str):
    """
    param: name_str is the name user entered
    The function check if the title is at least 2 characters
    and no longer than 40 characters
    """
    if len(name_str) >=2 and len(name_str)<= 40:
        return True
    else:
        return False

def is_valid_time(time_str):
    """
    param: time_str is the time input user enter
    The function check if the time is in 00:00 format
    """
    if type(time_str) == str:
        if len(time_str) == 5:
            if time_str[0:2].isdigit() == True and int(time_str[0:2])>=0 and int(time_str[0:2])<=99:
                if time_str[2] == ":":
                    if time_str[3:5].isdigit() == True and int(time_str[3:5])>=0 and int(time_str[3:5])<60:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
            

def is_valid_date(date_str):
    """
    param: date_str is the date user entered
    The function check if the date is valid in the format MM/DD/YYYY
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if "/" in date_str and date_str.count("/") == 2:
        if type(date_str) == str:
            if date_str[0:2].isdigit() and date_str[3:5].isdigit() and date_str[6:10].isdigit():
                if int(date_str[0:2])>=1 and int(date_str[0:2])<=12:
                    if int(date_str[3:5])>=1 and int(date_str[3:5])<= num_days[int(date_str[0:2])]:
                        if int(date_str[6:10])>1000:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def is_valid_uid(uid, key_list):
    """
    param: a is the string represents uid in new_song_list
    param: key_list is a list of all the keys in the song dictionary 
    The function check if the uid is valid and not exist in key_list yet
ana n dana    """
    if type(uid) ==str and len(uid) == 5:
        if uid.isdigit() == True:
            if int(uid)>= 10000 and int(uid)<= 99999:
                if uid not in key_list:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def get_new_song(new_song_list, rating_map, key_list):
    """
    param: a list of strings
    param: a dictionary (the rating map)
    param: a key_list of the songs dictionary (all_songs)
    The function check if new_song_list is valid by helper functions
    """

    if is_valid_addlist(new_song_list) == False:
        return ("Bad list. Found non-string, or bad length", 0)

    elif is_valid_time(new_song_list[2]) == False:
        return ("Invalid time format for Length", -2)

    elif len(new_song_list[5])!= 1 or new_song_list[5] not in "12345" or new_song_list[5].isdigit() == False:
        return ("Invalid Rating value", -3)

    elif is_valid_date(new_song_list[6]) == False:
        return ("Invalid date format for Release Date", -4)

    elif new_song_list[7][0] not in "TtFf":
        return ("Invalid value for Favorite", -5)

    elif is_valid_uid(new_song_list[8], key_list) == False:
        return ("Unique ID is invalid or non-unique", -6)

    elif is_valid_title(new_song_list[0]) == False:
        return ("Bad Title length", -1)

    elif new_song_list[7][0] in "TtFf":
        if new_song_list[7][0] in "Tt":
            new_song_list[7] = True
        else:
            new_song_list[7] = False
        newsong_dict={
                        "title": str(new_song_list[0]),  # str
                        "artist": str(new_song_list[1]), # str
                        "length": str(new_song_list[2]),  # str
                        "album": str(new_song_list[3]),  # str
                        "genre": new_song_list[4].split(','),  # list
                        "rating": int(new_song_list[5]) ,   # int
                        "released": str(new_song_list[6]), # str
                        "favorite": new_song_list[7],  # bool
                        "uid": int(new_song_list[8]) #int
                        }

    return newsong_dict

def load_from_csv(filename, in_dict, rating_map, allkeys):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_dict (dict of dict) - A dictionary of songs (dictionary objects) to which
            the songs read from the provided filename are added to.
            If in_dict is not empty, the existing songs are not dropped.
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new song using the `get_new_song()` function.
    - If the function `get_new_song()` returns a valid song object,
    it gets added to `in_dict`.
    - If the `get_new_song()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid song data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_dict` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_dict and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_dict`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_song().

    Helper functions:
    - get_new_song()
    """
    import csv
    import os

    if filename[-4:]!='.csv':
        return -1
    if not os.path.exists(filename):
        return None

    info_list = []
    info_dict = {}
    row_num = 0       
    with open(filename, 'r') as myfile:
        reader = csv.reader(myfile, delimiter = ",")
        for row in reader:
            row_num += 1
            result = get_new_song(row, rating_map, allkeys)
            if type(result) == dict:
                info_dict = {
                        "title": row[0],  
                        "artist": row[1],
                        "length": row[2],
                        "album": row[3],
                        "genre": row[4].split(','),  # str
                        "rating": int(row[5]) ,   
                        "released": str(row[6]), # str
                        "favorite": row[7],  
                        "uid": int(row[8])
                        }
                in_dict[row[8]] = info_dict
            else:
                info_list.append(row_num)
        return info_list

def save_to_csv(song_dict, filename):
    """
    param: song_dict(dict of dict) - The dictionary of songs stored 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the songs. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every song in the dictionary and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:

    * title
    * artist
    * length
    * album
    * genre (all element in the original list are converted to string
        joined with commas separating)
    * rating (converted to string)
    * released (written as string, i.e, "06/06/2022", NOT "June 6, 2022")
    * favorite (converted to string)
    * uid

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv

    if filename[-4:]!= '.csv':
        return -1
    
    with open(filename, 'w', newline='') as myfile:
        writer = csv.writer(myfile)
        for dictionary in song_dict:
            song_list = []
            for keys,values in song_dict[dictionary].items():
                if keys == "genre":
                    values = ",".join(song_dict[dictionary]['genre'])
                song_list.append(values)
                writer.writerow(song_list)
    return None
    
def edit_song(song_dict, songid, rating_map, field_key, field_info, allkeys):
    """
    param: song_dict (dict) - dictionary of all songs
    param: songid (str) - a string that is expected to contain the key of
            a song dictionary (same value as its unique id)
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: field_key (string) - a text expected to contain the name
            of a key in the song dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            song_dict[field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary.

    The function first calls some of its helper functions
    to validate the provided field.
    If validation succeeds, the function proceeds with the edit.

    return:
    If song_dict is empty, return 0.
    If the field_key is not a string, return -1.
    If the remainder of the validation passes, return the dictionary song_dict[songid].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions depending on the field_key:
    - is_valid_title()
    - is_valid_time()
    - is_valid_date()
    - is_valid_uid()
    """

    if song_dict == {}:
        return 0
    
    elif type(field_key) != str:
        return -1
    
    elif field_key == 'title':
        if is_valid_title(field_info)== False:
            return field_key
                
    elif field_key == 'length':
        if is_valid_time(field_info)== False:
            return field_key

    elif field_key == 'released':
        if is_valid_date(field_info)== False:
            return field_key

    elif field_key == 'uid':
        if is_valid_uid(field_info, songid) == False:
            return field_key

    song_dict[songid][field_key] = field_info  
    return song_dict[songid]

def do_stats(song_dict, opt):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: opt (str) - an option from the menu
    to do one of the following statistical calculations:
        "A" - find the mean (average) of all song ratings values
        "B" - find the median of all song ratings values
        "C" - find the standard deviation of all song ratings values
        "D" - print out a histogram of all song ratings values

    Helpful hint: see example on top of page in
    zyBook Ch. 8.4 to see how to do mean and stddev calculations.

    returns: Nothing! This function only PRINTS out results.    
    """
    rating_list = []
    for songid in song_dict:
        rate = song_dict[songid]['rating']
        rating_list.append(rate)
    rating_list.sort()

    if opt == "A":
        mean = sum(rating_list)/len(rating_list)
        print(f'The mean value of all ratings is: {mean:.2f}')
    
    if opt == "B":
        if len(rating_list)%2 == 0:
            median1 = rating_list[(len(rating_list))//2]
            median2 = rating_list[len(rating_list)//2-1]
            median = (median1 + median2)/2
            print(f'The median value of all ratings is: {median:.2f}')
        else:
            median = rating_list[n//2]
            print(f'The median value of all ratings is: {median:.2f}')

    if opt == "C":
        tmp = 0
        mean = sum(rating_list)/len(rating_list)
        for num in rating_list:
            tmp += (num - mean)**2
        std_dev = (tmp/len(rating_list))**0.5
        print(f'The standard deviation value of all ratings is: {std_dev:.2f}')

    if opt == "D":
      
        one = rating_list.count(1)
        symbol1 = "*"*one
        print(f'1 {symbol1}')
        
        two = rating_list.count(2)
        symbol2 = "*"*two
        print(f'2 {symbol2}')
        
        three = rating_list.count(3)
        symbol3 = "*"*three
        print(f'3 {symbol3}')

        four = rating_list.count(4)   
        symbol4 = "*"*four
        print(f'4 {symbol4}')

        five = rating_list.count(5)
        symbol5 = "*"*five
        print(f'5 {symbol5}')

        
        

    
    
        

    











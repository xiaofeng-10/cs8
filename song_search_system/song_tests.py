from song_functions import *
import csv
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

song = {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
   }

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}

key_list = all_songs.keys()

opt = {"A","B","C","D"}

print_song(song, rating_map, title_only = True, showid=True)
print_song(song, rating_map, title_only = False, showid=False)
print_song(song, rating_map, title_only = True, showid=False)
print_song(song, rating_map, title_only = False, showid=True)

assert delete_song(all_songs,"14567") == "Soul Meets Body"
assert delete_song([], "99105") == 0
assert delete_song(all_songs, "99999") == -1

addlist1 = ["Cardigan - Extended Version", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", "3", "07/27/2020", "True", "12333"]
addlist2 = ["Cardigan - Extended Version", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", 3, "07/27/2020", True, "12333"]
addlist3 = ["Cardigan - Extended Version", "Taylor Swift", "b7:59", "Folklore"]

print(get_written_date(["01", "01", "1970"]))
assert get_written_date(["01", "01", "1970"]) == "January 1, 1970"
assert get_written_date(["02", "03", "2000"]) == "February 3, 2000"
assert get_written_date(["10", "15", "2022"]) == "October 15, 2022"
assert get_written_date(["12", "31", "2021"]) == "December 31, 2021"

assert is_valid_addlist(addlist1) == True
assert is_valid_addlist(addlist2) == False
assert is_valid_addlist(addlist3) == False

assert is_valid_title("Love Story") == True
assert is_valid_title("") == False
assert is_valid_title("a") == False
assert is_valid_title(addlist1[0]) == True

assert is_valid_time(addlist1[2]) == True
assert is_valid_time(addlist3[2]) == False
assert is_valid_time("7:59") == False
assert is_valid_time("07:61") == False

assert is_valid_date(addlist1[6]) == True
assert is_valid_date("03022022") == False
assert is_valid_date("03/02/2022/") == False
assert is_valid_date("10/60/2022") == False
assert is_valid_date("03/02/999") == False

assert is_valid_uid(addlist1[8],key_list) == True
assert is_valid_uid(addlist2[8],key_list) == True
assert is_valid_uid("234",key_list) == False
assert is_valid_uid("2ab3",key_list) == False
assert is_valid_uid("12332",key_list) == False

print(get_new_song(addlist1, rating_map, key_list))
print(get_new_song(addlist2, rating_map, key_list))

assert get_new_song(addlist2, rating_map, key_list) !=("Invalid time format for Length", -2)
assert get_new_song(addlist1, rating_map, key_list) !=("Bad Title length", -1)
assert get_new_song(addlist3, rating_map, key_list) ==("Bad list. Found non-string, or bad length", 0)

assert load_from_csv("xfile", all_songs, rating_map, key_list) ==-1
assert load_from_csv("xfile.csv", all_songs, rating_map, key_list) != -1

assert save_to_csv(all_songs, "xfile") == -1
assert save_to_csv(all_songs, "xfile.csv") == None

field_key=""
field_key in ("title", "artist", "length", "album", "genre", "rating", "released", "favorite", "uid")
assert edit_song({}, "99105", rating_map, "rating", 3, key_list) == 0
assert edit_song(all_songs, "99105", rating_map, "uid", 78219, key_list) == "uid"


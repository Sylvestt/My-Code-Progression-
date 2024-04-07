   


from unittest import result


def anime():
    anime_list = ['steins gate', 'aot', 'one piece', 'nana', 'hunter x hunter']
    print(anime_list)
    while True:
        fav_anime = input('Which anime did Sion last watch?: ')
        if fav_anime.lower() == 'steins gate':
            print('Wow, you\'re correct!')
            return True
        else:
            print('Incorrect, try again.')

anime()


def characters():
    print('Ok, now you\'re going to get tested')
    character_list = ['Kurisu', 'Okabe', 'Mayuri', 'Daru', 'Suzuha']
    print(character_list)
    while True:
        fav_character = input('Which character was Sion\'s favorite?: ')
        if fav_character.lower() == 'kurisu':
            print('He couldn\'t resist her sassy tongue.')
            return True
        else:
            print('Sorry, you are incorrect. Try again.')

characters()






      


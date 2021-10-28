def song_decoder(song):

    v = [i for i in song.split('WUB') if i != '']
    a = ' '.join(v)

    return(a)


print(song_decoder('WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB'))

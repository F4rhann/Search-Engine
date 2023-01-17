import webbrowser

history = []

print("Search Engine!")
print("""You can search the following:
Facebook
Google
Discord
Mail
Youtube
Instagram
Twitter
Twitch""")

while True:

    search = input("Search: ")

    if search.lower() == "youtube":
        history.append(search)
        print("Opening youtube...")
        print(webbrowser.open_new_tab("https://youtube.com"))

    elif search.lower() == "google":
        history.append(search)
        print("Opening google...")
        print(webbrowser.open_new_tab("htpps://google.com"))

    elif search.lower() == "discord":
        history.append(search)
        print("Opening discord")
        print(webbrowser.open_new_tab("https://discord.com"))

    elif search.lower() == "mail":
        history.append(search)
        print("Openning mail")
        print(webbrowser.open_new_tab("https://mail.google.com"))

    elif search.lower() == "instagram":
        history.append(search)
        print("Openning instagram")
        print(webbrowser.open_new_tab("https://instagram.com"))

    elif search.lower() == "twitter":
        history.append(search)
        print("Openning twitter")
        print(webbrowser.open_new_tab("https://twitter.com"))

    elif search.lower() == "twitch":
        history.append(search)
        print("Openning twitch")
        print(webbrowser.open_new_tab("https://twitch.tv"))
    

    elif search.lower() == "history":
        print("History:",*history, sep=", ")
        history.append(search)
    else:
        print("Invalid search! You can only search google, mail, discord, instagram, history and youtube.")

import webbrowser

# List of favorite websites
favorite_websites = {
    'facebook': 'https://www.facebook.com/',
    'Netflix': 'https://www.netflix.com',
    'GitHub': 'https://www.github.com',
    'youtube ': 'https://www.youtube.com',
    'gmail': 'https://mail.google.com/mail/u/0/#inbox',
    
    
}

def open_website(url):
    webbrowser.open(url)
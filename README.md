# History importer from chrome to safari

I created this tool to import my browsing history from chrome to safari.

# Instructions

1. Locate and copy your chrome history file, eg. on a Mac computer, `cp "~/Library/Application Support/Google/Chrome/Default/History" .`
2. Run the program `python history.py History History.plist`
3. Convert the plist file to binary format `plutil -convert binary1 History.plist`
4. Backup your safari browsing history, eg. `cp ~/Library/Safari/History.plist{,.bak} && cp ~/Library/Safari/HistoryIndex.sk{,.bak}`
5. Overwrite safari history file and remove safari's HistoryIndex.sk file `mv History.plist ~/Library/Safari/History.plist && rm -f ~/Library/Safari/HistoryIndex.sk`
6. Done.

# TODO

1. I still don't understand what do the D and W fields in safari's history mean.
2. redirectURLs and lastVisitWasHTTPNonGet not implemented yet (and i think chrome doesn't store the information whether last visit is a HTTP GET or not)

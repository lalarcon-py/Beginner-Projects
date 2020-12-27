import pytube

video_list = []

print("Enter URLs (Terminate by 'STOP')")
while True:
    url = input("").lower()
    if url == 'STOP':
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(18)
    print(f"Downloading video {x}...")
    stream.download()
    print("Done.")
    ##NOTE: Upon launching this program you must copy and paste the youtube links into the command line separately, no limit to how many urls can be dumped in at once.
    ##When you're done simply type 'STOP' to terminate the program and download your video(s)

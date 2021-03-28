# Make a program that asks for the size of a file to download (in MB) and the speed of an Internet link (in Mbps),
# calculate and display the approximate download time of the file using this link (in minutes).

file_size = float(input("What is the size of the file you want to download in MB? "))
link = float(input("How fast is your internet in Mbps? "))

time_download_in_seconds = file_size / (link / 8)

minutes = 0

while True:
    if time_download_in_seconds > 60:
        minutes += 1
        time_download_in_seconds -= 60
    else:
        break

print(f"{minutes} minute(s) e {round(time_download_in_seconds)} second(s)")

# Faça um programa que pergunte o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e exiba o tempo aproximado de download do arquivo usando este link (em minutos).

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

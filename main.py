import subprocess

import PySimpleGUI as sg


def main():
    layout = [
        [sg.Button("Browse")],
        [sg.Text("", size=(40, 1), key="-OUTPUT-")],
        [sg.Text("Begin", size=(15, 1), font="Helvetica 20")],
        [sg.Input(key="-BEGIN-")],
        [sg.Text("End", size=(15, 1), font="Helvetica 20")],
        [sg.Input(key="-END-")],
        [sg.Button("Cancel")],
    ]

    window = sg.Window(
        "FFmpeg simple",
        layout,
        no_titlebar=False,
        location=(0, 0),
    )

    while True:
        # print(f"filename {filename}")
        event, values = window.read()
        # # See if user wants to quit or window was closed
        if event == "Cancel" or event is None:
            break 

        if event == "Browse":
            file = sg.popup_get_file("", no_window=True)
            if file == "":
                continue
            window["-OUTPUT-"].update(file)
            value_input_begin = values["-BEGIN-"]
            value_input_end = values["-END-"]
            new_filename = ""

            type_video = file.split(".")[1:2]
            if str(type_video[0]) == "ts":
                new_filename = ".".join(file.split(".")[0:-1]) + ".mp4"
            else:
                new_filename = ".".join(file.split(".")[0:-1]) + "_new.mp4"

            subprocess.run(
                [
                    "ffmpeg",
                    "-i",
                    file,
                    "-ss",
                    value_input_begin,
                    "-to",
                    value_input_end,
                    "-c:v",
                    "copy",
                    "-c:a",
                    "copy",
                    new_filename,
                ]
            )

            break

    window.close()


main()


# ffmpeg -i DVDES-513.ts -ss 0:35:40 -to 1:06:45 -c:v copy -c:a copy trimmedVideo.mp4

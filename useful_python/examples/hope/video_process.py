import sys

import ffmpeg


def remove_audio(in_file, out_file):
    (
        ffmpeg
            .input(in_file)
            .output(out_file, vcodec='copy', )
            .run()
    )


def merge_video_audio(in_video, in_audio, out_file):

    try:
        stream1 = ffmpeg.input(in_video)
        stream2 = ffmpeg.input(in_audio)
        stream3 = ffmpeg.output(stream1, stream2, 'merge.mp4', f='mp4')
        ffmpeg.run(stream3)
    except Exception as e:
        print(e.stderr.decode('gbk'), file=sys.stderr)


def set_bitrate(in_file, out_file):
    (
        ffmpeg
            .input(in_file)
            .output(out_file, video_bitrate=1000 * 1000)
            .run()
    )


if __name__ == '__main__':
    try:

        remove_audio(r'F:\work\useful\examples\hope\a.mp4', 'video.mp4')

        # merge_video_audio(r'F:\work\useful\examples\hope\video.mp4',
        #                   r'F:\work\useful\examples\hope\b.mp3',
        #                   'merge.mp4')
        # set_bitrate(r'F:\work\useful\examples\hope\merge.mp4', 'out.mp4')
    except Exception as e:
        # print(e.stderr.decode('gbk'), file=sys.stderr)
        # sys.exit(1)
        pass

import os
import random
import shutil
import subprocess
from moviepy.editor import VideoFileClip

from pydub import AudioSegment


def remove_audio(in_file, out_file):
    subprocess.call(
        'ffmpeg.exe -i {0}   -vcodec copy -an  {1}'.format(in_file, out_file))


def merge_video_audio(in_video, in_audio, out_file):
    subprocess.call(
        'ffmpeg.exe -i {0} -i {1}   {2}'.format(in_video, in_audio, out_file))


def set_bitrate(in_file, out_file):
    subprocess.call(
        'ffmpeg.exe -i {0}  -b:v 2000k {1}'.format(in_file, out_file))


def get_file_times(filename):
    u"""
    获取视频时长（s:秒）
    """
    clip = VideoFileClip(filename)
    file_time = clip.duration
    # print(dir(clip))
    clip.close()
    return file_time


def cut_mp3(filename, start, end, outname='cut.mp3'):
    # clip = AudioSegment.from_mp3(r'C:\Users\pugui\Desktop\鞋\music\Ehrling - Champagne Ocean.mp3')
    clip = AudioSegment.from_mp3(filename)  # 打开mp3文件
    clip[start * 1000:end * 1000].fade_in(3000).fade_out(3000).export(outname,
                                                                      format="mp3")  # 17.5


def up_video(filename):
    subprocess.call("ffmpeg -i %s -af 'volume=2' output.mp4" % (filename))


def auto_process(video_path, audio_path):
    if os.path.exists('cut.mp3'):
        os.remove('cut.mp3')
    if os.path.exists('merge.mp4'):
        os.remove('merge.mp4')
    if os.path.exists('out.mp4'):
        os.remove('out.mp4')
    if os.path.exists('video.mp4'):
        os.remove('video.mp4')

    dir_list = os.listdir(video_path)
    file_name = ''
    _type = ''
    for dr in dir_list:
        temp = dr.split('.')
        if len(temp) < 2:
            continue
        temp = temp[1]
        if temp not in ['mov', 'avi', 'mp4', 'MOV']:
            continue
        file_name = dr
        _type = temp
        break
    if _type == '':
        return

    if os.path.exists(os.path.join(video_path, 'origin.' + _type)) == False:
        os.rename(os.path.join(video_path, file_name),
                  os.path.join(video_path, 'origin.' + _type))
    video_path_c = os.path.join(video_path, 'origin.' + _type)

    dir_list = os.listdir(audio_path)
    file_name = ''
    _type = ''
    r = random.randint(0, len(dir_list))
    for index, dr in enumerate(dir_list):
        if index == r:
            file_name = dr

    audio_path_c = os.path.join(audio_path, file_name)

    video_time = get_file_times(video_path_c)
    cut_mp3(audio_path_c, 0, video_time)
    remove_audio(video_path_c, 'video.mp4')
    merge_video_audio(r'video.mp4',
                      r'cut.mp3',
                      r'merge.mp4')
    shutil.copy('merge.mp4', video_path)

    # set_bitrate(r'merge.mp4', 'out.mp4')
    # up_video('out.mp4')


if __name__ == '__main__':
    # clip = AudioSegment.from_mp3(r'C:\Users\pugui\Desktop\鞋\music\Ehrling - Champagne Ocean.mp3')
    # cut_mp3(r'C:\Users\pugui\Desktop\鞋\music\Ehrling - Champagne Ocean.mp3', 0, 10)

    auto_process(r'C:\Users\pugui\Desktop\鞋\new\py5530帆布鞋缺视频',
                 r'C:\Users\pugui\Desktop\鞋\music')

    # video_time = get_file_times(r'F:\work\useful\examples\hope\a.mp4')
    # cut_mp3('b.mp3', 0, video_time)
    # remove_audio(r'F:\work\useful\examples\hope\a.mp4', 'video.mp4')
    # merge_video_audio(r'F:\work\useful\examples\hope\video.mp4',
    #                   r'F:\work\useful\examples\hope\cut.mp3',
    #                   'merge.mp4')
    # set_bitrate(r'F:\work\useful\examples\hope\merge.mp4', 'out.mp4')

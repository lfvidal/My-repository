from moviepy.editor import VideoFileClip

def convert_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    print(f'Conversión completada: {output_path}')

# Uso
test_input = 'video_original.avi'  # Reemplázalo con tu video
output_format = 'mp4'
convert_video(test_input, f'video_convertido.{output_format}')

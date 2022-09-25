# from deoldify import device
# from deoldify.device_id import DeviceId
# #choices:  CPU, GPU0...GPU7
# device.set(device=DeviceId.GPU0)
#
# from deoldify.visualize import *
# plt.style.use('dark_background')
# import warnings
# warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")
#
# colorizer = get_video_colorizer()
#
# #NOTE:  Max is 44 with 11GB video cards.  21 is a good default
# render_factor=21
#
# file_name = "IMG_8360"
# file_name_ext = 'test_images/' + file_name + '.mov'
#
# result_path = None
#
# colorizer.colorize_from_file_name(file_name_ext, render_factor=render_factor)
#NOTE:  This must be the first call in order to work properly!
from deoldify import device
from deoldify.device_id import DeviceId
#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)

from deoldify.visualize import *
plt.style.use('dark_background')
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_video_colorizer()

#NOTE:  Max is 44 with 11GB video cards.  21 is a good default
render_factor=21
#NOTE:  Make source_url None to just read from file at ./video/source/[file_name] directly without modification
source_url='https://twitter.com/silentmoviegifs/status/1116751583386034176'
file_name = 'DogShy1926'
file_name_ext = file_name + '.mp4'
result_path = None

if source_url is not None:
    result_path = colorizer.colorize_from_url(source_url, file_name_ext, render_factor=render_factor)
else:
    result_path = colorizer.colorize_from_file_name(file_name_ext, render_factor=render_factor)

# print(result_path)
show_video_in_notebook(result_path)
for i in range(10,45,2):
    colorizer.vis.plot_transformed_image('video/bwframes/' + file_name + '/00001.jpg', render_factor=i, display_render_factor=True, figsize=(8,8))
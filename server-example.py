from tempfile import NamedTemporaryFile
import urllib.request  # Use urllib.request in Python 3
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

# load Source Sans 3 from google fonts
github_url = 'https://github.com/google/fonts/blob/main/ofl/sourcesans3/SourceSans3%5Bwght%5D.ttf'
url = github_url + '?raw=true'  # You want the actual file, not some HTML
# Open the URL and read the font file
response = urllib.request.urlopen(url)
f = NamedTemporaryFile(delete=False, suffix='.ttf')
f.write(response.read())
f.close()
font_entry = fm.FontProperties(fname=f.name)
fm.fontManager.addfont(f.name)
# uzh plotting style
plt.style.use('https://raw.githubusercontent.com/benckj/mpl_style/main/uzh.mplstyle')
plt.rcParams['font.family'] = font_entry.get_name()  # Set it as the default font

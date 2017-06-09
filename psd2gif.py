#!/usr/bin/python3

import os

def makegif(psd, gif='', delay=10, onlyvisible=False):
    _psd = PSDImage.load(psd)
    
    psddir = os.path.dirname(os.path.abspath(psd));
    
    if gif == '':
      gif = os.path.splitext(psd)[0]+'.gif'
    else:
      gif = os.path.splitext(gif)[0]+'.gif'
      if (not os.path.isabs(gif)):
        gif = psddir + '/' + gif

    layers = [l for l in _psd.layers if l.bbox.x1 > 0 and (l.visible!=False or not onlyvisible)]
    images = [l.as_PIL() for l in layers]
    if not os.path.exists('temp'):
      os.makedirs('temp')
    i = 0
    for img in images:
	#pixels = img.load() #for y in xrange(img.size[1]): #     for x in xrange(img.size[0]): #	     pixels[x, y] = (pixels[x, y][0] * pixels[x, y][3] / 255 + (255 - pixels[x, y][3]), pixels[x, y][1] * pixels[x, y][3] / 255 + (255 - pixels[x, y][3]), pixels[x, y][0] * pixels[x, y][2] / 255 + (255 - pixels[x, y][3]), 255)
      newimg = Image.new("RGB", (_psd.header.width, _psd.header.height), (255,)*4)
      newimg.paste(img, (layers[i].bbox.x1, layers[i].bbox.y1, layers[i].bbox.x1+img.size[0], layers[i].bbox.y1+img.size[1]))
      newimg.save('temp/frame_' + str(len(images) - i) + '.png')
      i = i + 1
    os.system("convert -delay " + str(delay) + " -loop 0 temp/frame_*.png '" + gif + "'")
    shutil.rmtree('temp')

if __name__ == '__main__':
  if os.path.dirname(os.path.abspath(__file__)) == "/usr/bin":
    import fire
    import shutil
    from psd_tools import PSDImage
    from PIL import Image
    fire.Fire(makegif)
  else:
    input('Do you want to install me?\n- If yes, just press enter')
    if os.getuid() != 0:
      print('run me with "sudo" please')
      pass

    import sys
    os.system('pip3 install Pillow')
    os.system('pip3 install psd_tools')
    os.system('pip3 install fire')
    os.system('cp ' + __file__ + ' /usr/bin/psd2gif')
    os.system('chmod +x /usr/bin/psd2gif')
    print('\n\n\n\x1b[1;33;42mInstallation is completed, thank you for using my script \x1b[1;31;42m❤ \x1b[;1m')
    print('\x1b[1;33mUSING: \x1b[1;34mpsd2gif --psd \x1b[1;32mSOURCE_FILE\x1b[1;34m [--gif \x1b[1;32mOUTPUT_FILE\x1b[1;34m] [--delay \x1b[1;32mDELAY_IN_MS\x1b[1;34m] [\x1b[1;32m--onlyvisible\x1b[1;34m]\x1b[;1m')
    print('\x1b[1;33mOr simply:\x1b[1;34m psd2gif \x1b[1;32mSOURCE\x1b[1;34m [\x1b[1;32mOUTPUT\x1b[1;34m] [\x1b[1;32mDELAY\x1b[1;34m] [\x1b[1;32m--onlyvisible\x1b[1;34m]\x1b[;1m')
    sys.stdout.write("\033[0;0m")

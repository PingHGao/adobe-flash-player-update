#!/usr/local/bin
# -*- coding: UTF-8 -*-

import os, sys
import subprocess
import urllib, urllib2
import re

def read_url(url, headers):
    req = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(req).read()
    return content

def get_link(url, headers, rep, link_pre=None):
    content = read_url(url, headers)
    link = (re.findall(rep, content))[0]
    if link_pre is not None:
        link = link_pre + link[:-1]
    return link

def download_process(count, block_size, total_size):
    len_processbar = 50.0
    num_arrows = len_processbar * count * block_size / total_size
    data = '[' + '>'*int(num_arrows) + '-'*int(len_processbar - int(num_arrows)) +\
            ']' + '%.2f' % (num_arrows * 2) + '%\r'
    sys.stdout.write(data)
    sys.stdout.flush()
    if count * block_size / total_size >= 0.9999:
        processbar_done()

def processbar_done(words='done'):
    print ''
    print words

def install(download_path, download_filename, download_file_type):
    download_file = download_path + download_filename + download_file_type
    print ''
    print 'extracting'
    command = 'tar -xvf ' + download_file + ' -C ' + download_path
    subprocess.call(command, shell=True)

    print ''
    so_src = download_path + 'libflashplayer.so'
    so_dst = '/usr/lib/mozilla/plugins/'
    usr_scr = download_path + 'usr/*'
    if not os.path.exists(so_dst):
        print 'Can not find', so_dst
        sys.exit(0)
    command = 'chmod +x ' + so_src
    print 'add executable to .so'
    subprocess.call(command, shell=True)
    command = 'sudo cp ' + so_src + ' ' + so_dst
    print command
    subprocess.call(command, shell=True)

    print ''
    command = 'sudo cp -r ' + usr_scr + ' /usr/'
    print command
    subprocess.call(command, shell=True)

if __name__=='__main__':

    url = 'https://get.adobe.com/flashplayer/'
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) Firefox/54.0'}
    download_path = '/tmp/flashplayer/'
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    download_filename = 'installer'
    download_file_type = '.tar.gz'
    download_file = download_path + download_filename + download_file_type

    download_page_link_pattern = '\/flashplayer\/download\/\?installer=.*_for_Linux_64-bit_\(\.tar\.gz\)_-_.*"'
    download_page_link_pre = 'https://get.adobe.com'
    download_page_link = get_link(url, headers, download_page_link_pattern, download_page_link_pre)

    print 'getting download link from', download_page_link
    print ''
    download_link_pattern = 'https:\/\/fpdownload\.adobe\.com\/get\/flashplayer\/pdc\/.*\/flash_player_npapi_linux.x86_64.tar.gz'
    download_link = get_link(download_page_link, headers, download_link_pattern)

    print 'downloading from url:', download_link
    urllib.urlretrieve(download_link, filename=download_file, reporthook=download_process)

    install(download_path, download_filename, download_file_type)



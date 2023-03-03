# coding=utf-8
import os


def handler(event, context):
    if not os.path.exists("/mnt/auto/.dujiaoka"):
        os.system(
            "wget https://github.com/assimon/dujiaoka/releases/download/2.0.6/2.0.6-antibody.tar.gz -O /mnt/auto/2.0.6-antibody.tar.gz")
        os.system(
            "cd /mnt/auto && tar xzf 2.0.6-antibody.tar.gz && mv dujiaoka .dujiaoka && rm 2.0.6-antibody.tar.gz && cd -")
    return "nas init"

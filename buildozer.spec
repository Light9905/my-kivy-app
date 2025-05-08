[app]
title = Cua App
package.name = cuaapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
entrypoint = main.py
android.archs = armeabi-v7a, arm64-v8a
log_level = 2
android.api = 33
android.minapi = 21
android.sdk = 30
android.ndk = 23b

[buildozer]
log_level = 2
warn_on_root = 1
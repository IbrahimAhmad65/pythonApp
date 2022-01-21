#pyenv shell 3.8.12
rm -rf dist
pyinstaller --noconsole ~/python/pythonApp/main.py
cp -r ~/python/pythonApp/files/ ~/python/pythonApp/dist/main/
#~/python/pythonApp/dist/main/main

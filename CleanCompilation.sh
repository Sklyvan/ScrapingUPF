rm build/ -R -v
rm dist/ -R -v
rm MainWindow.spec
rm src/MainWindow
pyinstaller src/MainWindow.py --onefile


Setup environment with::

  mkvirtualenv --no-site-packages testpres
  git clone git://github.com/godber/Python-Testing-Presentation.git
  cd Python-Testing-Presentation/
  pip install -r requirements.txt

Build presentation with, or just read the PDF::

  sudo apt-get update && sudo apt-get install make rst2pdf
  make


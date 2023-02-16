# VQGAN + RUCLIP Image generator

Image generator based on Sber-Ai networks. Hugely inspired by Katherine Crow image generation notebooks

Works in multilanguage mode so u can generate

    A picture of a красный кот. 
    Рисунок of a red cat

# Installation

First install `torch` you like, preferrably with cuda support. Find your version here https://pytorch.org/get-started/locally/
   
    pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

Now install `gantenna`

    pip install git+https://[repo url]

Keep in mind that ruclip requires Rust compiler for some reasons so you better intall it for windows and linux too

# Use

Check `jupyters` folder for `synth6.ipynb`
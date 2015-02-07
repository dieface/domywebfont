### What is it?

A tool helps make your custom font only contains the characters you want!

Based on [behdad/fonttools](https://github.com/behdad/fonttools) and [noto](https://code.google.com/p/noto)

### Requirements

- python 2.7+
- [fonttools](https://github.com/behdad/fonttools)

### Usage

Put 'coverage.py' and 'domywebfont.py' in the same folder, and execute the command below:  
```$ python domywebfont.py <input_font> <output_font> <word_list>```

ex.  
```$ python domywebfont.py NotoSansCJKtc-Light.otf NotoSansCJKtc-Light-min.otf words_to_keep_list.txt```

- \<input_font\>: original font file name/path. (ex. NotoSansCJKtc-Light.otf)
- \<output_font\>: custom font file output name/path. (ex. NotoSansCJKtc-Light-min.otf)
- \<word_list\>: file keep words you want as one character each line. (ex. words_to_keep_list.txt)

You can go into 'example' folder and execute the command above to give it a try!  
![Alt text](/example/example_result.png)

### License

See "LICENSE.md" for licensing information.



Do your web font!  
p.s. Please don't use it on license protected font. (請勿用在有版權的字體上) 

Bruce Lee <brucelee.ntu@gmail.com>

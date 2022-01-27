# Streamlit Demo App: GeneSpeak 🧬

Short URL: https://tinyurl.com/genespeak-demo
App URL: https://share.streamlit.io/sugatoray/genespeak/master/apps/demo/streamlit_app/app.py

## Folder Structure

The following folder/files are used for this app.

```sh
app.py                  # main app file
appfactory.py           # collection of top-level functions that are used in app.py
utils.py                # app building blocks for better abstraction
visualization.py        # dna-visualization related code
requirements.txt        # python dependencies for the app
packages.txt            # non-python, apt based packages (if necessary)
.streamlit              # app-settings
README.md               # readme file explaining anything that needs some documentation
```

## FAQs

1. What is necessary to use `pyperclip` package on Streamlit Cloud?

   Streamlit Cloud runs linux while serving/hosting the apps. The python
   package [`pyperclip`](https://pypi.org/project/pyperclip/) uses
   apt-based package `xclip` as a dependency, installed on the app hosting
   OS.

   ```sh
   sudo apt-get install xclip
   ```

   On Streamlit Cloud such `apt` based packages can be installed using an
   additional file `packages.txt` (alike `requirements.txt`).

1. Why is a `packages.txt` necessary for non-python dependencies?

   See here: [Streamlit Cloud - App dependencies][#stcloud-app-deps]

   [#stcloud-app-deps]: https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app/app-dependencies

   **Relevant Forum Discussions**:

   - [`@anfanilo` asnwer to *​When does it become a requirement to add packages.txt file in your repo?*](https://discuss.streamlit.io/t/when-does-it-become-a-requirement-to-add-packages-txt-file-in-your-repo/12711/2?u=sugatoray)
   - [`@randyzwitch` answer to *TA-Lib Streamlit Deploy Error*](https://discuss.streamlit.io/t/ta-lib-streamlit-deploy-error/7643/4?u=sugatoray)
   - [`@snehankekre` answer to *OSError: sndfile library not found*](https://discuss.streamlit.io/t/oserror-sndfile-library-not-found/12473/14?u=sugatoray)

1. How to deploy an app on Streamlit Cloud?

   See the docs here: [Streamlit Cloud - Deploy an App][#stcloud-app-deploy]

   [#stcloud-app-deploy]: https://docs.streamlit.io/streamlit-cloud/get-started/deploy-an-app#apt-get-dependencies

1. If you have multiple apps in a repository, how to add app-specific streamlit theme settings?

   Add a `.streamlit` folder in the same location as the `app.py` file, and create a file `config.toml` inside the folder `.streamlit`. While running the app, just make sure the `streamlit run app.py` command is issued from the directory where the app resides.

   A sample `.streamlit/config.toml` file.

   ```toml
   [theme]
   base="light"
   primaryColor="#4baaff"
   textColor="#31333f"
   backgroundColor="#ffffff"
   secondaryBackgroundColor="#f0f2f6"
   font="sans serif"
   ```

1. How to get installed `gtk` version on linux?

   Run this command.

   ```sh
   dpkg -s libgtk-3-0|grep '^Version'
   ```

   Or,

   ```sh
   gtk-launch --version
   ```

   Source: https://stackoverflow.com/a/13098607/8474894

1. How to skip formatting with black in certain parts of a file?

   See here: https://stackoverflow.com/questions/58584413/black-formatter-ignore-specific-multi-line-code

   The following block of code is left untouched by black by adding `# fmt: on` and `# fmt: off` before and after the code block.

   ```python
   # fmt: off
   np.array(
      [
         [1, 0, 0, 0],
         [0, -1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, -1],
      ]
   )
   # fmt: on
   ```

   For inline skipping, use `# fmt: skip`.

   ```python
   from typing import Dict, List, Tuple, Optional, Union  # fmt: skip
   ```

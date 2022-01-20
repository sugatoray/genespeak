# Streamlit Demo App: GeneSpeak 🧬

Short URL: https://tinyurl.com/genespeak-demo
App URL: https://share.streamlit.io/sugatoray/genespeak/master/apps/demo/streamlit_app/app.py

## Folder Structure

The following folder/files are used for this app.

```sh
app.py                  # main app file
utils.py                # app building blocks for better abstraction
requirements.txt        # python dependencies for the app
packages.txt            # non-python, apt based packages (if necessary)
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
